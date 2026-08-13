---
title: "HE-Arc 360°"
date: 2026-08-13
description: "Une visite de la HE-Arc dans le navigateur, construite à partir de vidéos 360° : on se déplace de zone en zone en cliquant, et des points d'intérêt ouvrent des panneaux d'information."
summary: "Une visite de la HE-Arc dans le navigateur, construite à partir de vidéos 360° : on se déplace de zone en zone en cliquant, et des points d'intérêt ouvrent des panneaux d'information."
categories:
  - "P3 HES d'été"
statuts:
  - "Idea"
---

Filmer la HE-Arc avec une caméra 360° et en faire une visite jouable dans le navigateur
avec [Babylon.js](https://www.babylonjs.com/) : on regarde autour de soi, on clique pour
passer à la zone suivante, et des points d'intérêt ouvrent des panneaux d'information.

## Contexte

Le principe de navigation est celui de *Myst* : le visiteur n'est pas libre de ses
déplacements, il occupe une position fixe depuis laquelle il regarde dans toutes les
directions, et il passe d'un point à un autre en cliquant sur une zone du décor. La
visite est donc un **graphe de zones** reliées entre elles, pas un espace continu.

La différence avec les visites virtuelles habituelles, qui reposent sur des photos
panoramiques figées, tient au support : ici chaque zone est une **vidéo 360°**. Un
couloir n'est plus une image morte, il montre des gens qui passent, un écran allumé,
une machine qui tourne. C'est ce qui distingue une visite d'école vivante d'une plaquette
en trois dimensions.

Techniquement, une vidéo 360° est une vidéo équirectangulaire projetée sur l'intérieur
d'une sphère autour de la caméra. Babylon.js fournit ce qu'il faut pour cela, et permet
d'y superposer les éléments interactifs.

## Projet pilote

Un premier prototype a été réalisé en projet P3 en 2021 :
<https://gitlab-etu.ing.he-arc.ch/isc/2021/projet-p3/226/360-he-arc>

Le reprendre est le point de départ : identifier ce qui fonctionne, ce qui a vieilli
(versions de Babylon.js, formats vidéo, compatibilité navigateur) et ce qui manque.

## Objectifs

### Principaux

- Capturer les zones de l'école à la caméra 360° et établir la chaîne de traitement des
  rushes jusqu'au format diffusable sur le web.
- Implémenter le lecteur : projection de la vidéo 360° dans Babylon.js, contrôle du
  regard à la souris et au tactile.
- Implémenter les **zones cliquables** qui font passer d'une zone à une autre, avec une
  transition lisible pour que le visiteur ne se perde pas.
- Implémenter les **points d'intérêt** : un élément cliquable ancré dans la scène qui
  ouvre un panneau d'information (texte, image, lien).
- Décrire la visite en données — le graphe des zones, la position des points d'intérêt et
  leur contenu — hors du code, pour qu'on puisse la modifier sans recompiler.

### Secondaires

- Fournir un outil d'édition permettant de placer les points d'intérêt et les zones
  cliquables directement dans la vue, sans éditer les coordonnées à la main.
- Gérer plusieurs langues pour les panneaux d'information.
- Ajouter le son, éventuellement spatialisé selon la direction du regard.
- Prendre en charge les casques de réalité virtuelle via WebXR.
- Proposer un plan de l'école situant la zone courante et permettant d'y naviguer.

## Critères d'évaluation

À définir.

## Points d'attention

- **Le poids des vidéos.** En 360°, le visiteur ne voit qu'une fraction de l'image à la
  fois : il faut une définition source élevée pour un rendu correct, ce qui pèse sur le
  temps de chargement. Le compromis définition / poids / temps de démarrage est une
  question de conception, pas un réglage de fin de projet.
- **L'ancrage des éléments interactifs.** Un point d'intérêt est posé en coordonnées
  sphériques et doit rester collé à l'objet qu'il désigne quand le visiteur tourne la
  tête.
- **La continuité entre les zones.** C'est ce qui fait qu'une visite est agréable ou
  désorientante : direction du regard conservée d'une zone à l'autre, transition, repères
  visuels.
