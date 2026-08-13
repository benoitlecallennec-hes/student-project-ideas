---
title: "YouTube pour l'animation 3D"
date: 2026-08-11
description: "Une plateforme de publication et de consultation des animations 3D du Motion-Lab : génération automatique de vignettes et d'aperçus depuis les fichiers BVH, lecteur web, recherche."
summary: "Une plateforme de publication et de consultation des animations 3D du Motion-Lab : génération automatique de vignettes et d'aperçus depuis les fichiers BVH, lecteur web, recherche."
categories:
  - "P3 HES d'été"
  - "TB"
statuts:
  - "Idea"
aliases:
  - "/projects/mocap-asset-manager/"
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

Le Motion-Lab de la HE-Arc produit et stocke un grand nombre de fichiers de capture de
mouvement, en particulier au format BVH. Ce sont eux qui servent de fonds de départ : la
plateforme doit générer ses vignettes et ses aperçus automatiquement à partir de ces
fichiers, sans qu'un opérateur ait à ouvrir quoi que ce soit.

## Objectifs

### Principaux

- Générer automatiquement, à partir d'un fichier BVH, une **vignette** et un **aperçu animé** exploitables dans une galerie web.
- Concevoir le modèle de publication : dépôt d'un fichier d'animation, métadonnées, déclenchement de la génération.
- Implémenter un lecteur web permettant de rejouer une animation 3D dans le navigateur.
- Implémenter la navigation : liste, recherche, filtres, page de détail par animation.

### Secondaires

- Suggérer des animations proches (par similarité de mouvement, tags ou métadonnées).
- Gérer les comptes et les droits de publication.
- Permettre le partage par lien et l'intégration du lecteur dans une page externe.
- Prendre en charge d'autres formats de capture que le BVH.

## Critères d'évaluation

Les critères sont chiffrés et, autant que possible, mesurés **sans évaluateur humain**.
Ce qui reste subjectif est évalué par des personnes **extérieures à l'encadrement**.

Les critères suivants ne sont que des suggestions.
Il faut les revoir, et les ajuster le cas échéant.

Les valeurs notées **N**, **X**, **Y**, **T** et **S** sont à calibrer par l'équipe
projet, puis à faire valider : un fonds de référence de **N** fichiers BVH, **X**
participants au panel dont **Y** doivent réussir, **T** minutes de temps imparti par
tâche, **S** secondes de génération maximale pour un aperçu.

### Mesures automatiques

- Ingestion du fonds de référence de **N** fichiers BVH : **≥ 98 %** traités sans intervention manuelle, chaque échec journalisé avec sa cause
- Génération d'une vignette et d'un aperçu : **< S s** par fichier, moyenne sur les **N** fichiers
- **0** étape manuelle entre le dépôt d'un fichier et son apparition dans la galerie
- Poids d'un aperçu : **≤ 500 ko**, ce qui conditionne la consultation sur un réseau lent
- Affichage de la galerie complète : **< 2 s** jusqu'au premier rendu utile, sur les **N** animations
- Latence de recherche et de filtrage sur le fonds complet : **< 200 ms**
- Lecteur web : **≥ 30 images/s** sur une machine de milieu de gamme, mesuré sur les 5 animations les plus lourdes du fonds
- Rendu des squelettes : **0 régression** sur un jeu de référence, par comparaison d'images avec des rendus validés
- Fonctionnement avec l'accès Internet sortant coupé : **100 %** des fonctions — les données de capture ne quittent pas le réseau de l'école

### Panel de X utilisateurs extérieurs au projet

Ni les étudiants du projet, ni aucun enseignant : des utilisateurs réels du fonds
d'animations.

**Protocole.** Chacun reçoit la plateforme et la description d'un mouvement, et doit
retrouver l'animation correspondante puis dire ce qu'elle contient, **sans ouvrir aucun
logiciel 3D et sans aide**. Chronomètre lancé, l'observateur note sans intervenir.
Échec au-delà de **T** minutes.

- Retrouvent l'animation décrite dans le temps imparti : **Y sur X**
- Décrivent correctement le mouvement à partir du seul aperçu : **Y sur X**
- Temps médian pour identifier le contenu d'une animation : **< T / 2**
- « Je l'utiliserais plutôt que d'ouvrir les fichiers dans un logiciel 3D », note de 1 à 5 : **moyenne ≥ 4**

### Équipe du Motion-Lab

- Métadonnées affichées jugées suffisantes pour décider d'utiliser ou non une animation, sans ouvrir le fichier : **0 remarque bloquante**
- Licences et droits d'utilisation visibles sur **100 %** des animations publiées
- Documentation d'exploitation : **≤ 2 pages**, jugée suffisante pour reprendre le service sans ses auteurs

## À rapprocher

Ce sujet absorbe l'ancienne fiche « MoCap Asset Manager », qui ne couvrait que la
génération des vignettes et des aperçus : elle en est devenue le premier objectif.

Il recoupe encore [BdD de Motion Capture]({{< relref "/projects/bdd-de-motion-capture" >}})
pour l'indexation et la recherche. À arbitrer : sujet distinct, ou couche de présentation
au-dessus de cette base de données.
