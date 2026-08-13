---
title: "YouTube pour l'animation 3D"
date: 2026-08-11
description: "Une plateforme de publication et de consultation d'animations 3D, où l'on parcourt et prévisualise des mouvements comme on parcourt des vidéos."
summary: "Une plateforme de publication et de consultation d'animations 3D, où l'on parcourt et prévisualise des mouvements comme on parcourt des vidéos."
categories:
  - "P3 HES d'été"
statuts:
  - "Idea"
---

Une plateforme de publication et de consultation d'animations 3D, où l'on parcourt et
prévisualise des mouvements comme on parcourt des vidéos sur YouTube.

## Contexte

Une animation 3D ne se consulte pas comme une vidéo : il faut un moteur de rendu, un
squelette, parfois un format propriétaire. Résultat, un fonds d'animations reste
difficile à explorer — on ne sait pas ce qu'un fichier contient sans l'ouvrir dans un
logiciel dédié. L'idée est d'appliquer à l'animation 3D les codes qui rendent une
plateforme vidéo consultable : vignette, aperçu au survol, lecteur intégré, recherche,
suggestions.

## Objectifs

### Principaux

- Concevoir le modèle de publication : dépôt d'un fichier d'animation, métadonnées,
  génération automatique d'une vignette et d'un aperçu.
- Implémenter un lecteur web permettant de rejouer une animation 3D dans le navigateur.
- Implémenter la navigation : liste, recherche, filtres, page de détail par animation.

### Secondaires

- Suggérer des animations proches (par similarité de mouvement, tags ou métadonnées).
- Gérer les comptes et les droits de publication.
- Permettre le partage par lien et l'intégration du lecteur dans une page externe.
- Évaluer les performances sur un fonds de plusieurs centaines d'animations.

## À rapprocher

Le sujet recoupe [MoCap Asset Manager]({{< relref "/projects/mocap-asset-manager" >}})
pour la génération des vignettes et des aperçus, et
[BdD de Motion Capture]({{< relref "/projects/bdd-de-motion-capture" >}}) pour
l'indexation et la recherche. À arbitrer : sujet distinct, ou couche de présentation
au-dessus de ces deux-là.
