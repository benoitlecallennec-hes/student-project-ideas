#!/usr/bin/env python3
"""Convertit les fiches de 3282.1-P3-TB/projets/*.md en contenu Hugo.

Usage : python tools/import_projets.py <chemin/vers/projets> [--dry-run]

Script one-shot : il a été exécuté une seule fois pour amorcer content/, qui est
depuis la source de vérité et s'édite à la main. Le relancer écrase content/sujets
et content/realisations. Voir tools/README.md.

Aucune dépendance externe (même convention que le build_dashboard.py du repo source).
"""
import os
import re
import sys

STATUT_REALISE = "Completed"
SECTION_SUJETS = "sujets"
SECTION_REALISATIONS = "realisations"
CATEGORIE_DEFAUT = "Non classé"
CLES_LISTE = {"categories", "tags"}
RESUME_MAX = 180

# Traces de la migration Notion : renvoient à une page privée, aucun sens ici.
BLOCKQUOTES_ARTEFACT = (
    "*Image d'illustration non migrée — voir la page Notion d'origine.*",
    "*Cette page Notion contenait un ou plusieurs bookmarks (aperçus de liens) non exportables.*",
)

# Sections retirées : noms de personnes, le site public ne doit en porter aucun.
SECTIONS_RETIREES = ("Mandants",)

LIGNES_RETIREES = ("Voir proto Python / Jupyter fait pour Emma.",)

# Signale ce qui doit être relu à la main : le script ne devine pas la réécriture.
MOTIFS_A_RELIRE = (
    (re.compile(r"\bEmail\b|\bMuller\b|\bAubry\b|\bEmma\b"), "mention nominative résiduelle"),
    (re.compile(r"suivi/\d{4}-\d{4}"), "chemin interne du repo de suivi"),
    (re.compile(r"gitlab-etu|\.ing\.he-arc\.ch"), "URL interne HE-Arc"),
    (re.compile(r"^- \[[ x]\]", re.M), "checklist de tâches internes"),
)

LIEN_LOCAL = re.compile(r"\[([^\]]+)\]\(([a-z0-9][a-z0-9-]*)\.md\)")
BLOC_NON_PARAGRAPHE = re.compile(r"^(#{1,6} |>|[-*+] |\d+\. |\||```|\{\{)")
MARKDOWN_INLINE = (
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
        raise ValueError(f"{os.path.basename(path)} : frontmatter absent ou mal délimité")
    meta = {}
    for line in m.group(1).splitlines():
        if not line.strip() or line.strip().startswith("#"):
            continue
        key, sep, val = line.partition(":")
        if not sep:
            raise ValueError(f"{os.path.basename(path)} : ligne sans deux-points : {line!r}")
        key = key.strip()
        meta[key] = parse_value(val, key in CLES_LISTE)
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


def strip_h1(body, titre):
    """Blowfish rend déjà .Title en <h1> ; garder celui du corps ferait deux h1."""
    lines = body.split("\n")
    for i, line in enumerate(lines):
        if not line.strip():
            continue
        if line.startswith("# "):
            if line[2:].strip() != titre:
                raise ValueError(f"H1 {line[2:].strip()!r} != titre {titre!r}")
            return "\n".join(lines[:i] + lines[i + 1:])
        break
    raise ValueError(f"aucun H1 en tête pour {titre!r}")


def strip_artifact_lines(body):
    """Retrait ligne à ligne : rotors-geometric-algebra porte les deux blockquotes."""
    retires = 0
    kept = []
    for line in body.split("\n"):
        stripped = line.strip()
        if any(stripped == "> " + a for a in BLOCKQUOTES_ARTEFACT):
            retires += 1
            continue
        if stripped in LIGNES_RETIREES:
            retires += 1
            continue
        kept.append(line)
    return "\n".join(kept), retires


def strip_sections(body, titres):
    """Retire un `## Titre` et son contenu, jusqu'au prochain titre de niveau <= 2."""
    lines = body.split("\n")
    kept, retirees = [], []
    i = 0
    while i < len(lines):
        m = re.match(r"^(#{1,2}) +(.+?) *$", lines[i])
        if m and m.group(2) in titres:
            retirees.append(m.group(2))
            niveau = len(m.group(1))
            i += 1
            while i < len(lines):
                suivant = re.match(r"^(#{1,6}) +", lines[i])
                if suivant and len(suivant.group(1)) <= niveau:
                    break
                i += 1
            continue
        kept.append(lines[i])
        i += 1
    return "\n".join(kept), retirees


def rewrite_local_links(body, sections_par_slug, source_slug):
    reecrits = []

    def remplacer(m):
        libelle, cible = m.group(1), m.group(2)
        section = sections_par_slug.get(cible)
        if section is None:
            raise ValueError(f"{source_slug} : lien vers {cible}.md, fiche inconnue")
        reecrits.append(f"{source_slug} → {section}/{cible}")
        return f'[{libelle}]({{{{< relref "/{section}/{cible}" >}}}})'

    return LIEN_LOCAL.sub(remplacer, body), reecrits


def normalize_blank_lines(body):
    return re.sub(r"\n{3,}", "\n\n", body).strip("\n")


def first_paragraph(body):
    bloc = []
    for line in body.split("\n"):
        stripped = line.strip()
        if not stripped:
            if bloc:
                break
            continue
        if BLOC_NON_PARAGRAPHE.match(stripped):
            if bloc:
                break
            continue
        bloc.append(stripped)
    texte = " ".join(bloc)
    for motif, remplacement in MARKDOWN_INLINE:
        texte = motif.sub(remplacement, texte)
    texte = re.sub(r"\s+", " ", texte).strip()
    if len(texte) > RESUME_MAX:
        coupe = texte[:RESUME_MAX].rsplit(" ", 1)[0]
        texte = coupe.rstrip(" ,;:.") + "…"
    return texte


def convert(path, sections_par_slug, journal):
    slug = os.path.basename(path)[:-3]
    meta, body = parse_file(path)
    titre = meta["titre"]
    statut = meta["statut"]
    section = SECTION_REALISATIONS if statut == STATUT_REALISE else SECTION_SUJETS

    body = strip_h1(body, titre)
    body, n_artefacts = strip_artifact_lines(body)
    body, sections_retirees = strip_sections(body, SECTIONS_RETIREES)
    body, liens = rewrite_local_links(body, sections_par_slug, slug)
    body = normalize_blank_lines(body)

    journal["artefacts"] += n_artefacts
    journal["sections_retirees"] += len(sections_retirees)
    journal["liens"].extend(liens)

    resume = first_paragraph(body)
    if resume:
        description = resume
    else:
        description = f"{titre} — idée de projet étudiant proposée à la HE-Arc Ingénierie."
        journal["sans_resume"].append(f"{section}/{slug}")

    categories = meta.get("categories") or [CATEGORIE_DEFAUT]
    if not meta.get("categories"):
        journal["sans_categorie"].append(f"{section}/{slug}")

    fields = {
        "title": titre,
        "date": meta["cree"],
        "description": description,
        "summary": resume,
        "categories": categories,
        "statuts": [statut],
        "tags": meta.get("tags"),
        # `type` est réservé par Hugo (lookup des layouts) : renommé en `nature`.
        "nature": meta.get("type"),
    }

    for motif, libelle in MOTIFS_A_RELIRE:
        if motif.search(body):
            journal["a_relire"].append(f"{section}/{slug}.md — {libelle}")

    contenu = emit_frontmatter(fields)
    if body:
        contenu += "\n\n" + body
    return section, slug, contenu + "\n"


def main():
    # Le journal contient des accents et des flèches ; la console Windows est en cp1252.
    sys.stdout.reconfigure(encoding="utf-8")
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    dry_run = "--dry-run" in sys.argv
    if len(args) != 1:
        sys.exit(__doc__)
    source = args[0]
    fichiers = sorted(
        os.path.join(source, f) for f in os.listdir(source) if f.endswith(".md")
    )
    if not fichiers:
        sys.exit(f"aucun .md dans {source}")

    # Table slug → section construite d'abord : les liens inter-fiches en dépendent.
    sections_par_slug = {}
    for path in fichiers:
        meta, _ = parse_file(path)
        slug = os.path.basename(path)[:-3]
        sections_par_slug[slug] = (
            SECTION_REALISATIONS if meta["statut"] == STATUT_REALISE else SECTION_SUJETS
        )

    journal = {
        "artefacts": 0,
        "sections_retirees": 0,
        "liens": [],
        "sans_resume": [],
        "sans_categorie": [],
        "a_relire": [],
    }
    resultats = [convert(p, sections_par_slug, journal) for p in fichiers]

    racine = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "content")
    if not dry_run:
        for section in (SECTION_SUJETS, SECTION_REALISATIONS):
            dossier = os.path.join(racine, section)
            os.makedirs(dossier, exist_ok=True)
            for nom in os.listdir(dossier):
                if nom.endswith(".md") and nom != "_index.md":
                    os.remove(os.path.join(dossier, nom))
        for section, slug, contenu in resultats:
            cible = os.path.join(racine, section, slug + ".md")
            with open(cible, "w", encoding="utf-8", newline="\n") as f:
                f.write(contenu)

    par_section = {}
    for section, _, _ in resultats:
        par_section[section] = par_section.get(section, 0) + 1

    print(f"{len(resultats)} fiches converties" + (" (dry-run)" if dry_run else ""))
    for section, n in sorted(par_section.items()):
        print(f"  content/{section}/ : {n}")
    print(f"blockquotes et lignes d'artefact retirés : {journal['artefacts']}")
    print(f"sections retirées ({', '.join(SECTIONS_RETIREES)}) : {journal['sections_retirees']}")
    print(f"liens inter-fiches réécrits en relref : {len(journal['liens'])}")
    for lien in journal["liens"]:
        print(f"  {lien}")
    print(f"fiches sans catégorie → {CATEGORIE_DEFAUT} : {len(journal['sans_categorie'])}")
    for f in journal["sans_categorie"]:
        print(f"  {f}")
    print(f"fiches sans résumé (esquisses) : {len(journal['sans_resume'])}")
    for f in journal["sans_resume"]:
        print(f"  {f}")
    print(f"À RELIRE À LA MAIN : {len(journal['a_relire'])}")
    for f in journal["a_relire"]:
        print(f"  {f}")


if __name__ == "__main__":
    main()
