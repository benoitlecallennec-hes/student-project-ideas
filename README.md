# Idées de projets étudiants — HE-Arc Ingénierie

Site Hugo public présentant les idées de projets proposées aux étudiants : projets de
semestre (P1/P2/P3), travaux de Bachelor, Ra&D, sujets liés à des cours.

- Production : <https://benoitlecallennec-hes.github.io/student-project-ideas/>
- Thème : [Blowfish](https://blowfish.page/) 2.84.0, **vendoré** (voir `themes/blowfish/VENDORED.md`)
- Déploiement : GitHub Actions → GitHub Pages (`.github/workflows/gh-pages.yml`)

`content/` est la **source de vérité**. Les fiches ont été importées une seule fois
depuis `3282.1-P3-TB/projets` ; les deux dépôts ont divergé depuis. Voir `tools/README.md`.

## Développer

```bash
hugo server
```

Le site est servi sur <http://localhost:1313/student-project-ideas/> — `hugo server`
conserve le chemin du `baseURL`, ce qui reproduit les conditions de production.

`buildFuture = false` : une fiche dont la `date` est dans le futur **disparaît
silencieusement** du build. En édition, utiliser `hugo server -F`.

## Structure

```
content/
  _index.md                 accueil
  projects/                 les 57 fiches, un seul répertoire  → /projects/
  categories/               branch bundle pour corriger un slug de terme
  statuts/completed/        branch bundle : titre de la page « Projets réalisés »
layouts/
  _default/list.html        liste de section (remplace celle du thème)
  _default/term.html        page de terme, même rendu que la liste de section
  _default/index.json       index de recherche Fuse.js
  partials/project-item.html    une entrée de liste
  partials/project-filters.html barre de filtres
assets/
  css/custom.css            styles du catalogue, écrits à la main
  css/schemes/hearc.css     palette HE-Arc
  css/compiled/main.css     Tailwind précompilé et committé
  js/filters.js             filtrage client
i18n/fr.yaml                libellés du catalogue
tools/import_projets.py     script d'import one-shot (archive, ne pas relancer)
```

## Ajouter une fiche

Créer `content/projects/<slug>.md` (slug kebab-case ASCII) :

```markdown
---
title: "Titre du sujet"
date: 2026-08-11
description: "Une phrase : sert de meta description et de résumé de liste."
summary: "Une phrase : sert de meta description et de résumé de liste."
categories:
  - "TB"
  - "Projets P3"
statuts:
  - "Idea"
tags:
  - "Python"
nature: "Enseignement"
---

Une phrase d'accroche.

## Contexte

## Objectifs

### Principaux

### Secondaires
```

- **Pas de `# H1` dans le corps** : le thème rend déjà `title` en `<h1>`. Commencer aux `##`.
- **`summary` omis** ⇒ la liste affiche « Sujet à préciser » à la place du résumé.
  C'est voulu pour les esquisses ; le renseigner dès que la fiche a du contenu.
- `statuts` (au pluriel, liste d'un élément) : `Idea`, `Next Up`, `Prospection`,
  `In Progress`, `Completed`, `OnHold`, `WontDo`. **C'est la seule chose à changer quand
  un projet est livré** : passer le statut à `Completed` suffit, la fiche apparaît alors
  sur `/statuts/completed/` et son URL ne bouge pas. Rien à déplacer.
- `categories` : `TB`, `Projets P1`, `Projets P2`, `Projets P3`, `P3 HES d'été`,
  `Cours GELO`, `Cours Infographie`, `Cours C`, `Algos + SdD`, `Ra&D`, `Python`,
  `General`, `Non classé`. Les puces de filtre se construisent automatiquement depuis
  les valeurs présentes — aucune liste à maintenir ailleurs.
- `nature` (optionnel) : `Enseignement` ou `Ra&D`. **Ne jamais utiliser `type`** :
  c'est une clé réservée par Hugo qui change le layout utilisé.
- Lien vers une autre fiche : `[Titre]({{< relref "/projects/autre-slug" >}})`. Un lien
  cassé fait échouer le build, ce qui est le comportement voulu.
- **Aucun nom de personne** sur le site : c'est une règle éditoriale du site, appliquée
  à l'import et vérifiée à la relecture. Le contact passe par la page d'accueil.
- Aucune URL Notion : le workflow de déploiement échoue si `content/` en contient une.

## CSS

`assets/css/compiled/main.css` est un build Tailwind **figé et committé** : il ne
contient que les classes utilisées au moment de sa génération. Une classe utilitaire
nouvelle écrite dans un layout n'aura **aucun effet** tant que Tailwind n'est pas
recompilé. C'est pourquoi les styles du catalogue sont du CSS écrit à la main dans
`assets/css/custom.css`.

Pour recompiler (rarement nécessaire) :

```bash
npm ci && npm run css:build
```

puis committer `assets/css/compiled/main.css`.

## Déploiement

Push sur `main`. Le workflow épingle Hugo 0.143.1 (le thème déclare
`max = "0.145.0"`), vérifie l'absence d'URL Notion dans `content/`, construit avec le
`baseURL` fourni par GitHub Pages et publie. Pages doit être configuré avec
**source = GitHub Actions**.
