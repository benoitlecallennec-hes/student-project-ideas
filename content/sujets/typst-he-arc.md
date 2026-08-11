---
title: "Typst à la HE-Arc : déploiement et templates"
date: 2026-08-11
description: "Déployer Typst à la HE-Arc, y porter les templates de rapport de TB, de poster et de cahier des charges, et héberger un serveur PlantUML interne."
summary: "Déployer Typst à la HE-Arc, y porter les templates de rapport de TB, de poster et de cahier des charges, et héberger un serveur PlantUML interne."
categories:
  - "P3 HES d'été"
statuts:
  - "Idea"
---

Mettre Typst à disposition des étudiants et des enseignants de la HE-Arc, avec les
gabarits de documents de l'école déjà portés, et sans dépendance à un service de
rendu de diagrammes externe.

## Contexte

[Typst](https://typst.app/) est un système de composition de documents qui vise le
même terrain que LaTeX avec une syntaxe et des messages d'erreur nettement plus
abordables, et une compilation quasi instantanée. Les documents produits pendant un
projet ou un travail de Bachelor (cahier des charges, rapport, poster) suivent des
gabarits imposés : les porter en Typst supprimerait une bonne part de la friction que
les étudiants rencontrent aujourd'hui avec LaTeX.

Les diagrammes UML de ces documents sont souvent produits avec PlantUML, dont le
serveur de rendu public n'est pas une dépendance acceptable pour des documents de
l'école. Un serveur hébergé en interne règle à la fois la disponibilité et la
confidentialité.

## Objectifs

### Principaux

- Évaluer Typst pour l'usage de l'école et décider du mode de mise à disposition
  (installation locale documentée, image de conteneur, instance web hébergée).
- Porter le template de **rapport de travail de Bachelor** et valider le rendu par
  rapport au gabarit de référence.
- Porter le template de **poster**.
- Porter le template de **cahier des charges**.
- Héberger un **serveur PlantUML** interne à l'école et documenter son utilisation
  depuis Typst.

### Secondaires

- Mettre en place une compilation automatique des documents (CI) produisant le PDF
  à chaque modification.
- Documenter la migration d'un document LaTeX existant vers Typst.
- Fournir un jeu d'exemples minimal par template (figures, tableaux, bibliographie,
  citations, références croisées).
- Évaluer l'intégration d'un éditeur en ligne pour les étudiants.
