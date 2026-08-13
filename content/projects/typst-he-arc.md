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

[Typst](https://typst.app/) est un système de composition de documents (comme LaTeX) avec une syntaxe et des messages d'erreur simples, et une compilation quasi instantanée.

Les documents produits pendant un projet ou un travail de Bachelor (cahier des charges, rapport, poster) suivent des gabarits imposés : les porter en Typst supprimerait une bonne part de la friction que les étudiants rencontrent aujourd'hui avec LaTeX ou avec Word.

Les diagrammes UML de ces documents sont souvent produits avec PlantUML, soit en local, soit sur un serveur externe. 
L'installation locale de planteuml est possible, mais requiert en particulier Java et Graphviz.
L'utilisation d'un serveur public de rendu PlantUML est possible, mais pose des problèmes de confidentialité dans certains cas (projets Ra&D).


## Objectifs

### Principaux

- Évaluer Typst pour l'usage de l'école et décider du mode de mise à disposition sur une instance hébergée. Si ce n'est pas possible, il faudra le justifier, et proposer des alternatives acceptables (installation locale documentée, image de conteneur, etc.).
- Héberger un **serveur PlantUML** interne à l'école et documenter son utilisation depuis Typst. De la même manière, si ce n'est pas possible, il faudra le justifier et proposer des alternatives acceptables.
- Porter les template de **rapport de travail de Bachelor**, ainsi que le template de **cahier des charges** en Typst, et documenter leur utilisation.
- Fournir une CLI (python) permettant d'abstraire toutes les commandes pour Typst et PlantUML, et de générer un projet minimal prêt à l'emploi avec les templates de l'école.
- Documenter la mise en place d'un projet Typst avec les templates de l'école, et fournir un exemple minimal de projet prêt à l'emploi.

### Secondaires

- Porter le template de **poster**.
- Mettre en place une compilation automatique des documents (CI) produisant le PDF à chaque modification grâce à la CLI fournie.
- Fournir un jeu d'exemples minimal par template (figures, tableaux, bibliographie, citations, références croisées).
- Évaluer l'intégration d'un éditeur en ligne pour les étudiants.

## Critères d'évaluation

Les critères sont chiffrés et, autant que possible, mesurés **sans évaluateur humain**.
Ce qui reste subjectif est évalué par des personnes **extérieures à l'encadrement**.

Les critères suivants ne sont que des suggestions.
Il faut les revoir, et les ajuster le cas échéant.

### Mesures automatiques

- Fidélité du gabarit rapport de TB : **≥ 98 %** de lignes identiques au PDF de référence, par extraction du texte puis `diff` — J8
- Compilation d'un rapport de 40 pages : **< 2 s**, moyenne de 5 exécutions — J8
- Installation depuis zéro : **≤ 3 commandes** et **< 5 min**, chronométré sur une machine virtuelle vierge — J6
- **0** étapes manuelles entre `new` et le PDF généré — J6
- **0** commandes `typst` ou `plantuml` brutes dans la documentation — J9
- Types de diagrammes rendus : **5 sur 5** (classes, séquence, cas d'utilisation, activité, composants), chacun **< X s** — J4
- Rendu avec l'accès Internet sortant coupé : **5 sur 5** réussis — J4
- Reprise après redémarrage de l'hôte : **< 60 s** et **0 intervention** — J4

### Panel de X étudiants extérieurs au projet

Ni les étudiants du projet, ni aucun enseignant.
Critère d'inclusion : **n'avoir jamais utilisé Typst** (ou presque).

**Protocole.** Chacun reçoit une machine vierge et la seule documentation, et doit produire un cahier des charges de 3 pages contenant une figure, un tableau et un diagramme UML.
Chronomètre lancé, **aucune aide** : l'observateur note sans intervenir.
Échec au-delà de 30 minutes.

- Terminent le document sans aide : **≥ 5 sur 6**, en **< 20 min**
- Temps médian jusqu'à la première compilation réussie : **< 10 min**
- Sorties de la documentation (recherche web, question posée) : **≤ 1** en moyenne
- « Je saurais refaire seul », note de 1 à 5 : **moyenne ≥ 4**
- « Comparé à Word ou LaTeX », note de 1 à 5 : **moyenne ≥ 4**

### Enseignants

- Revue de mise en production du serveur PlantUML : **0 remarque bloquante**
- Documentation d'exploitation : **≤ 2 pages**, jugée suffisante pour reprendre le service sans ses auteurs
- **0** flux sortants vers Internet mesurés sur 24 h
- Conformité des gabarits : **0 écart majeur** et **≤ 2 écarts mineurs**
