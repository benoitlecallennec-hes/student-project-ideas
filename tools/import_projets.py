#!/usr/bin/env python3
"""Convert the fiches in 3282.1-P3-TB/projets/*.md into Hugo content.

Usage: python tools/import_projets.py <path/to/projets> [--dry-run]

One-shot script: it was run once to bootstrap content/, which has been the source
of truth ever since and is edited by hand. Running it again overwrites everything
under content/sujets and content/realisations. See tools/README.md.

No external dependency, same convention as build_dashboard.py in the source repo.
"""
import os
import re
import sys

DONE_STATUS = "Completed"
SECTION_SUBJECTS = "sujets"
SECTION_DELIVERED = "realisations"
DEFAULT_CATEGORY = "Non classé"
LIST_KEYS = {"categories", "tags"}
SUMMARY_MAX = 180

# Leftovers from the Notion migration: they point at a private page, meaningless here.
MIGRATION_BLOCKQUOTES = (
    "*Image d'illustration non migrée — voir la page Notion d'origine.*",
    "*Cette page Notion contenait un ou plusieurs bookmarks (aperçus de liens) non exportables.*",
)

# Sections dropped entirely: they list people, and the public site carries no names.
DROPPED_SECTIONS = ("Mandants",)

DROPPED_LINES = ("Voir proto Python / Jupyter fait pour Emma.",)

# Flags what a human must rewrite: the script does not guess these.
REVIEW_PATTERNS = (
    (re.compile(r"\bEmail\b|\bMuller\b|\bAubry\b|\bEmma\b"), "leftover personal name"),
    (re.compile(r"suivi/\d{4}-\d{4}"), "internal path into the tracking repo"),
    (re.compile(r"gitlab-etu|\.ing\.he-arc\.ch"), "internal HE-Arc URL"),
    (re.compile(r"^- \[[ x]\]", re.M), "internal task checklist"),
)

LOCAL_LINK = re.compile(r"\[([^\]]+)\]\(([a-z0-9][a-z0-9-]*)\.md\)")
NON_PARAGRAPH_BLOCK = re.compile(r"^(#{1,6} |>|[-*+] |\d+\. |\||```|\{\{)")
INLINE_MARKDOWN = (
    (re.compile(r"\[([^\]]+)\]\([^)]*\)"), r"\1"),
    (re.compile(r"\*\*([^*]+)\*\*"), r"\1"),
    (re.compile(r"(?<!\w)[*_]([^*_]+)[*_](?!\w)"), r"\1"),
    (re.compile(r"`([^`]+)`"), r"\1"),
)


def split_list(inner):
    items, buf, quote, escaped = [], "", None, False
    for ch in inner:
        if escaped:
            buf += ch
            escaped = False
        elif quote and ch == "\\":
            escaped = True
        elif quote:
            if ch == quote:
                quote = None
            else:
                buf += ch
        elif ch in "\"'":
            quote = ch
        elif ch == ",":
            items.append(buf.strip())
            buf = ""
        else:
            buf += ch
    items.append(buf.strip())
    return [i for i in items if i]


def parse_value(raw, as_list=False):
    raw = raw.strip()
    if as_list:
        return split_list(raw[1:-1]) if raw.startswith("[") and raw.endswith("]") else [raw]
    if len(raw) > 1 and raw[0] == raw[-1] and raw[0] in "\"'":
        return raw[1:-1].replace('\\"', '"').replace("\\\\", "\\")
    return raw


def parse_file(path):
    with open(path, encoding="utf-8") as f:
        text = f.read().replace("\r\n", "\n").replace("\r", "\n")
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.S)
    if not m:
        raise ValueError(f"{os.path.basename(path)}: missing or malformed frontmatter")
    meta = {}
    for line in m.group(1).splitlines():
        if not line.strip() or line.strip().startswith("#"):
            continue
        key, sep, val = line.partition(":")
        if not sep:
            raise ValueError(f"{os.path.basename(path)}: line without a colon: {line!r}")
        key = key.strip()
        meta[key] = parse_value(val, key in LIST_KEYS)
    return meta, m.group(2)


def yaml_scalar(value):
    return '"' + str(value).replace("\\", "\\\\").replace('"', '\\"') + '"'


def emit_frontmatter(fields):
    lines = ["---"]
    for key, value in fields.items():
        if value is None or value == [] or value == "":
            continue
        if isinstance(value, list):
            lines.append(f"{key}:")
            lines.extend(f"  - {yaml_scalar(v)}" for v in value)
        elif key == "date":
            lines.append(f"{key}: {value}")
        else:
            lines.append(f"{key}: {yaml_scalar(value)}")
    lines.append("---")
    return "\n".join(lines)


def strip_h1(body, title):
    """Blowfish already renders .Title as an <h1>; keeping the body one gives two."""
    lines = body.split("\n")
    for i, line in enumerate(lines):
        if not line.strip():
            continue
        if line.startswith("# "):
            if line[2:].strip() != title:
                raise ValueError(f"h1 {line[2:].strip()!r} != title {title!r}")
            return "\n".join(lines[:i] + lines[i + 1:])
        break
    raise ValueError(f"no leading h1 for {title!r}")


def strip_migration_lines(body):
    """Line by line: rotors-geometric-algebra carries both blockquotes."""
    dropped = 0
    kept = []
    for line in body.split("\n"):
        stripped = line.strip()
        if any(stripped == "> " + a for a in MIGRATION_BLOCKQUOTES):
            dropped += 1
            continue
        if stripped in DROPPED_LINES:
            dropped += 1
            continue
        kept.append(line)
    return "\n".join(kept), dropped


def strip_sections(body, titles):
    """Drop a `## Title` and its content, up to the next heading of level <= 2."""
    lines = body.split("\n")
    kept, dropped = [], []
    i = 0
    while i < len(lines):
        m = re.match(r"^(#{1,2}) +(.+?) *$", lines[i])
        if m and m.group(2) in titles:
            dropped.append(m.group(2))
            level = len(m.group(1))
            i += 1
            while i < len(lines):
                following = re.match(r"^(#{1,6}) +", lines[i])
                if following and len(following.group(1)) <= level:
                    break
                i += 1
            continue
        kept.append(lines[i])
        i += 1
    return "\n".join(kept), dropped


def rewrite_local_links(body, sections_by_slug, source_slug):
    rewritten = []

    def replace(m):
        label, target = m.group(1), m.group(2)
        section = sections_by_slug.get(target)
        if section is None:
            raise ValueError(f"{source_slug}: link to {target}.md, unknown fiche")
        rewritten.append(f"{source_slug} -> {section}/{target}")
        return f'[{label}]({{{{< relref "/{section}/{target}" >}}}})'

    return LOCAL_LINK.sub(replace, body), rewritten


def normalize_blank_lines(body):
    return re.sub(r"\n{3,}", "\n\n", body).strip("\n")


def first_paragraph(body):
    block = []
    for line in body.split("\n"):
        stripped = line.strip()
        if not stripped:
            if block:
                break
            continue
        if NON_PARAGRAPH_BLOCK.match(stripped):
            if block:
                break
            continue
        block.append(stripped)
    text = " ".join(block)
    for pattern, replacement in INLINE_MARKDOWN:
        text = pattern.sub(replacement, text)
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) > SUMMARY_MAX:
        cut = text[:SUMMARY_MAX].rsplit(" ", 1)[0]
        text = cut.rstrip(" ,;:.") + "…"
    return text


def convert(path, sections_by_slug, report):
    slug = os.path.basename(path)[:-3]
    meta, body = parse_file(path)
    title = meta["titre"]
    status = meta["statut"]
    section = SECTION_DELIVERED if status == DONE_STATUS else SECTION_SUBJECTS

    body = strip_h1(body, title)
    body, migration_lines = strip_migration_lines(body)
    body, dropped_sections = strip_sections(body, DROPPED_SECTIONS)
    body, links = rewrite_local_links(body, sections_by_slug, slug)
    body = normalize_blank_lines(body)

    report["migration_lines"] += migration_lines
    report["dropped_sections"] += len(dropped_sections)
    report["links"].extend(links)

    summary = first_paragraph(body)
    if summary:
        description = summary
    else:
        description = f"{title} — idée de projet étudiant proposée à la HE-Arc Ingénierie."
        report["without_summary"].append(f"{section}/{slug}")

    categories = meta.get("categories") or [DEFAULT_CATEGORY]
    if not meta.get("categories"):
        report["without_category"].append(f"{section}/{slug}")

    fields = {
        "title": title,
        "date": meta["cree"],
        "description": description,
        "summary": summary,
        "categories": categories,
        "statuts": [status],
        "tags": meta.get("tags"),
        # `type` is reserved by Hugo (it drives layout lookup), hence `nature`.
        "nature": meta.get("type"),
    }

    for pattern, label in REVIEW_PATTERNS:
        if pattern.search(body):
            report["needs_review"].append(f"{section}/{slug}.md — {label}")

    document = emit_frontmatter(fields)
    if body:
        document += "\n\n" + body
    return section, slug, document + "\n"


def main():
    # The report has accents and arrows; the Windows console defaults to cp1252.
    sys.stdout.reconfigure(encoding="utf-8")
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    dry_run = "--dry-run" in sys.argv
    if len(args) != 1:
        sys.exit(__doc__)
    source = args[0]
    paths = sorted(
        os.path.join(source, f) for f in os.listdir(source) if f.endswith(".md")
    )
    if not paths:
        sys.exit(f"no .md found in {source}")

    # slug -> section table built first: the cross-fiche links depend on it.
    sections_by_slug = {}
    for path in paths:
        meta, _ = parse_file(path)
        slug = os.path.basename(path)[:-3]
        sections_by_slug[slug] = (
            SECTION_DELIVERED if meta["statut"] == DONE_STATUS else SECTION_SUBJECTS
        )

    report = {
        "migration_lines": 0,
        "dropped_sections": 0,
        "links": [],
        "without_summary": [],
        "without_category": [],
        "needs_review": [],
    }
    results = [convert(p, sections_by_slug, report) for p in paths]

    root = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "content")
    if not dry_run:
        for section in (SECTION_SUBJECTS, SECTION_DELIVERED):
            folder = os.path.join(root, section)
            os.makedirs(folder, exist_ok=True)
            for name in os.listdir(folder):
                if name.endswith(".md") and name != "_index.md":
                    os.remove(os.path.join(folder, name))
        for section, slug, document in results:
            target = os.path.join(root, section, slug + ".md")
            with open(target, "w", encoding="utf-8", newline="\n") as f:
                f.write(document)

    per_section = {}
    for section, _, _ in results:
        per_section[section] = per_section.get(section, 0) + 1

    print(f"{len(results)} fiches converted" + (" (dry run)" if dry_run else ""))
    for section, count in sorted(per_section.items()):
        print(f"  content/{section}/: {count}")
    print(f"migration blockquotes and lines dropped: {report['migration_lines']}")
    print(f"sections dropped ({', '.join(DROPPED_SECTIONS)}): {report['dropped_sections']}")
    print(f"cross-fiche links rewritten as relref: {len(report['links'])}")
    for link in report["links"]:
        print(f"  {link}")
    print(f"fiches without a category -> {DEFAULT_CATEGORY}: {len(report['without_category'])}")
    for name in report["without_category"]:
        print(f"  {name}")
    print(f"fiches without a summary (stubs): {len(report['without_summary'])}")
    for name in report["without_summary"]:
        print(f"  {name}")
    print(f"NEEDS MANUAL REVIEW: {len(report['needs_review'])}")
    for name in report["needs_review"]:
        print(f"  {name}")


if __name__ == "__main__":
    main()
