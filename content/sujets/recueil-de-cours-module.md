---
title: "Recueil de cours / module"
date: 2026-02-13
description: "1241.1 Langage C : \\<1ère année\\> \\<SA\\> \\<ISC\\> \\<Langage C\\> Voir https://he-arc.github.io/imagerie-portfolio/"
summary: "1241.1 Langage C : \\<1ère année\\> \\<SA\\> \\<ISC\\> \\<Langage C\\> Voir https://he-arc.github.io/imagerie-portfolio/"
categories:
  - "Cours GELO"
  - "P3 HES d'été"
statuts:
  - "Prospection"
tags:
  - "Python"
  - "SmartData"
---

1. Scraper les PDFs depuis le site
2. Extraire les informations, pour chaque cours (testé, ça fonctionne à 90%)
3. Uniformiser les données pour chaque cours + corrections
4. Mise en forme (json, yaml, etc.). Les fichiers deviendront la base de données de référence
5. Générer un site statique : une page, un cours, avec les tags associés.
   1241.1 Langage C : \<1ère année\> \<SA\> \<ISC\> \<Langage C\>
   Voir [https://he-arc.github.io/imagerie-portfolio/](https://he-arc.github.io/imagerie-portfolio/)
6. Pour chaque ajout / modification, lancer tous les tests pour vérifier que la nouvelle version respecte toutes les contraintes demandées (nommage, code cours, etc.)
7. Créer un graphe des compétences avec difficulté, dépendances, etc.

## Workflow

### One-shot

Site web → PDFs → fichiers texte

### CI/CD

→ fichiers texte → génération markdown (Hugo) → génération site web statique → génération graphe de compétences
