---
title: "Tracking de tête temps réel dans Unreal Engine"
date: 2026-08-06
description: "Le but de ce projet est de tracker la position de la tête d'un utilisateur avec le système OptiTrack du Motion-Lab, et d'exploiter ces données dans Unreal Engine pour créer un…"
summary: "Le but de ce projet est de tracker la position de la tête d'un utilisateur avec le système OptiTrack du Motion-Lab, et d'exploiter ces données dans Unreal Engine pour créer un…"
categories:
  - "Projets P3"
statuts:
  - "Idea"
---

Le but de ce projet est de tracker la position de la tête d'un utilisateur avec le système OptiTrack du Motion-Lab, et d'exploiter ces données dans Unreal Engine pour créer un effet de perspective immersif.

## Contexte

Le Motion-Lab dispose d'un système de capture de mouvement OptiTrack composé de 14 caméras, capable de suivre avec précision des objets rigides en 6 degrés de liberté (position et orientation). L'objectif de ce projet est de concevoir et tracker un support léger (par exemple une paire de lunettes équipée de marqueurs) pour récupérer en temps réel la position de la tête d'un utilisateur. Ces données seront utilisées dans Unreal Engine pour contrôler la caméra et ajuster la perspective, offrant une sensation de profondeur et d'immersion 3D lorsque l'utilisateur se déplace devant l'écran.

## Pipeline

OptiTrack (Motive) → Transmission temps réel via Live Link → Unreal Engine (contrôle caméra) → Affichage immersif sur écran.

## Objectifs

### Principaux

- Concevoir et calibrer un objet rigide (lunettes ou équivalent) pour le tracking de tête dans OptiTrack.
- Transmettre les données de position/orientation en temps réel vers Unreal Engine via Live Link.
- Contrôler la caméra dans Unreal Engine pour adapter la perspective aux mouvements réels de l'utilisateur.

### Secondaires

- Implémenter un filtrage pour réduire le jitter et améliorer la stabilité du rendu.
- Créer une petite scène 3D fixe permettant de démontrer clairement l'effet d'immersion.
- Expérimenter des extensions (stéréoscopie, ajout d'objets virtuels fixes dans l'espace).

## Références

> **Note :** cette section a été générée par Claude (assistant IA) à partir de recherches web, et n'a pas été relue ni vérifiée en détail. Les liens et les affirmations sont à contrôler avant de s'en servir.

Les sections 1 à 5 couvrent le périmètre du projet (tracking d'un rigid body OptiTrack et transmission dans Unreal). Les sections 6 et 7 concernent les extensions (perspective immersive).

### 1. Conception du support et placement des marqueurs

- [Rigid Body Tracking (Motive)](https://docs.optitrack.com/motive/rigid-body-tracking) : 4 à 12 marqueurs, placement asymétrique, espacement maximal pour la précision en orientation, formes non congruentes, placement du pivot.
- Mots-clés : *marker placement*, *marker asymmetry*, *rigid body definition*, *pivot point*, *retroreflective markers*, *occlusion robustness*.

### 2. Calibration et repères

- [Data Streaming (Motive)](https://docs.optitrack.com/motive/data-streaming) : axe Up, ground plane, conversion vers un repère main gauche.
- [OptiTrack Unreal Engine Plugin](https://docs.optitrack.com/plugins/optitrack-unreal-engine-plugin) : options de pivot et d'origine côté client.
- [A Low-Cost Approach to Fish Tank VR with Semi-Automatic Calibration Support](https://ieeexplore.ieee.org/document/9090626/), IEEE 2020 : calibration écran/volume, utile pour la suite.
- Mots-clés : *calibration wand*, *ground plane*, *coordinate system conversion*, *Y-up right-handed vs Z-up left-handed*, *tracking volume*.

### 3. Qualité du tracking : jitter, latence, filtrage

- [Properties Pane: Rigid Body (Motive)](https://docs.optitrack.com/motive-ui-panes/properties-pane/properties-pane-rigid-body) : Smoothing (double exponentiel) et Prediction.
- [Settings: Live Pipeline (Motive)](https://docs.optitrack.com/motive-ui-panes/settings/settings-live-pipeline) : réglages de la chaîne temps réel.
- Casiez, Roussel, Vogel, [1€ Filter](https://dl.acm.org/doi/10.1145/2207676.2208639), CHI 2012, avec [implémentations](https://github.com/casiez/OneEuroFilter).
- Teather et al., [Effects of Tracking Technology, Latency, and Spatial Jitter on Object Movement](https://www.csit.carleton.ca/~rteather/pdfs/3dui09.pdf), 3DUI 2009 : base pour définir des critères de mesure.
- Mots-clés : *tracking jitter*, *positional noise*, *motion-to-photon latency*, *end-to-end latency measurement*, *double exponential smoothing*, *1€ filter*, *adaptive low-pass filter*, *prediction / dead reckoning*.

### 4. Transmission réseau

- [Data Streaming (NatNet)](https://docs.optitrack.com/motive/data-streaming) : UDP unicast/multicast, choix des données streamées.
- [Settings: Streaming (Motive)](https://docs.optitrack.com/motive-ui-panes/settings/settings-streaming).
- [NatNet SDK](https://docs.optitrack.com/developer-tools/natnet-sdk) : client custom C++/Python, utile pour mesurer la latence hors Unreal.
- Mots-clés : *NatNet*, *UDP multicast*, *unicast*, *streaming frame rate*, *timecode*.

### 5. Intégration Unreal Engine

- [Unreal Engine: OptiTrack Live Link Plugin](https://docs.optitrack.com/plugins/optitrack-unreal-engine-plugin/unreal-engine-optitrack-live-link-plugin) : installation, source Live Link, Live Link Controller component.
- [Unreal Engine: Live Link Camera Stream Setup](https://docs.optitrack.com/plugins/optitrack-unreal-engine-plugin/unreal-engine-optitrack-live-link-plugin/unreal-engine-live-link-camera-stream-setup) : variante si l'objet déplacé est une caméra.
- [VRPNLiveLink](https://github.com/max-verem/VRPNLiveLink) : exemple de source Live Link custom.
- Mots-clés : *Live Link*, *Live Link source*, *Live Link Controller component*, *transform role*, *Blueprint*, *actor transform*.

### 6. Édition de la matrice de projection (projection hors-axe)

Maths de base :

- Kooima, [Generalized Perspective Projection](https://www.semanticscholar.org/paper/Generalized-Perspective-Projection-Kooima/14d1b312aba825bcce17edd67e3fdc139f1a76a2), 2008 : trois coins de l'écran et position de l'œil en entrée, matrice de projection asymétrique et matrice de vue en sortie.
- [DisplayXR/kooima-projection](https://github.com/DisplayXR/kooima-projection) : implémentation compacte réutilisable en C++.
- [Wikibooks: Projection for Virtual Reality](https://en.wikibooks.org/wiki/Cg_Programming/Unity/Projection_for_Virtual_Reality) et [Off-axis projection in Unity](https://medium.com/try-creative-tech/off-axis-projection-in-unity-1572d826541e) : explications pas à pas, transposables.
- [Projection Matrices in Unreal Engine (Geodesic)](https://geodesic.tech/projection-matrices-in-unreal-engine/) : conventions Unreal (reversed-Z, main gauche, Z-up).

Points d'entrée dans Unreal :

- **Sous-classe de `ULocalPlayer`** : surcharger `GetProjectionData` ou `CalcSceneView`. Doc [ULocalPlayer::GetProjectionData](https://docs.unrealengine.com/5.0/en-US/API/Runtime/Engine/Engine/ULocalPlayer/GetProjectionData/). Approche du plugin [fweidner/UE4-Plugin-OffAxis](https://github.com/fweidner/UE4-Plugin-OffAxis), branche UE5. Fil de référence : [Howto modify the projection matrix](https://forums.unrealengine.com/t/howto-modify-the-projection-matrix/287457), qui mentionne aussi la variante `SceneViewExtension`, plus propre.
- **`USceneCaptureComponent2D` avec `bUseCustomProjectionMatrix`** : [doc API](https://docs.unrealengine.com/4.27/en-US/API/Runtime/Engine/Components/USceneCaptureComponent2D/bUseCustomProjectionMatrix/). Simple à mettre en place, mais la matrice custom n'affecte pas le culling et des problèmes d'ombres sont rapportés ([No shadows with custom projection matrix](https://forums.unrealengine.com/t/no-shadows-with-custom-projection-matrix/369804)). Tutoriel : [UE5 Camera vs SceneCapture: Maintain Axis, Frustum Math, Projection Pipeline](https://dev.epicgames.com/community/learning/tutorials/98yn/unreal-engine-ue5-camera-vs-scenecapture-maintain-axis-frustum-math-projection-pipeline).
- **nDisplay, politique « Simple »** : [Projection Policies in nDisplay](https://dev.epicgames.com/documentation/en-us/unreal-engine/projection-policies-in-ndisplay-in-unreal-engine). Rectangle écran + View Origin, nDisplay calcule le frustum hors-axe. Le View Origin est piloté par Live Link. Exemple complet : [HeadTracked-3D-Screen-Unreal-nDisplay](https://github.com/cormacmadden/HeadTracked-3D-Screen-Unreal-nDisplay). Tutoriel : [Off-Axis Projection nDisplay (byowls)](https://byowls.com/off-axis-projection-ndisplay/). Pièges : [Head tracking with CAVE using nDisplay](https://forums.unrealengine.com/t/head-tracking-with-cave-using-ndisplay-does-not-work/262435).
- Mots-clés : *off-axis projection*, *asymmetric frustum*, *generalized perspective projection*, *custom projection matrix*, *ULocalPlayer*, *SceneViewExtension*, *SceneCaptureComponent2D*, *nDisplay simple projection policy*, *View Origin*, *reversed-Z*, *screen corners calibration*.

### 7. Contexte scientifique et culture du sujet

- Deering, *High Resolution Virtual Reality*, SIGGRAPH 1992 : premier système écran plat + tracking de tête stéréo. [Référence via ACM](https://dl.acm.org/doi/abs/10.1145/311535.311587).
- Ware, Arthur, Booth, [Fish Tank Virtual Reality](https://dl.acm.org/doi/10.1145/169059.169066), INTERCHI 1993 : définit le terme, montre que le couplage tête compte plus que la stéréo. [PDF UNH](https://scholars.unh.edu/ccom/178/).
- Cruz-Neira et al., [Surround-screen projection-based virtual reality: the CAVE](https://dl.acm.org/doi/10.1145/166117.166134), SIGGRAPH 1993.
- Rekimoto, [A vision-based head tracker for fish tank VR](https://ieeexplore.ieee.org/document/512484/), VRAIS 1995.
- Fafard, Stavness et al., [FTVR in VR: Evaluation of 3D Perception With a Simulated Volumetric Fish-Tank VR Display](https://doi.org/10.1109/tvcg.2019.2898742), IEEE TVCG 2019.
- Zhou, Fels et al., [Design and implementation of a multi-person fish-tank virtual reality display](https://dl.acm.org/doi/10.1145/3281505.3281540), VRST 2018.
- [Head-tracked off-axis perspective projection improves gaze readability of 3D virtual avatars](https://dl.acm.org/doi/10.1145/3283254.3283271), SIGGRAPH Asia 2018.
- [Generalized Projection Matrices](https://arxiv.org/pdf/2208.09549), arXiv 2022 : généralisation récente de Kooima.
- Johnny Lee, [Head Tracking for Desktop VR Displays using the Wii Remote](https://www.youtube.com/watch?v=Jd3-eiid-Uw), 2007 : la démo canonique de l'effet visé, à montrer aux étudiants.
- Mots-clés : *head-coupled perspective*, *fish tank VR (FTVR)*, *motion parallax*, *window-on-world*, *desktop VR*, *viewer-centered projection*, *CAVE*.
