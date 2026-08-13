---
title: "Web Viewer pour insectes"
date: 2025-12-19
description: "Le projet SwissCollNet s'inscrit dans une démarche de valorisation et d'exploitation scientifique de collections naturalistes numérisées, en particulier des insectes photo-scannés…"
summary: "Le projet SwissCollNet s'inscrit dans une démarche de valorisation et d'exploitation scientifique de collections naturalistes numérisées, en particulier des insectes photo-scannés…"
categories:
  - "TB"
statuts:
  - "Prospection"
---

## Contexte

Le projet SwissCollNet s'inscrit dans une démarche de valorisation et d'exploitation scientifique de collections naturalistes numérisées, en particulier des insectes photo-scannés en haute résolution. Actuellement, l'outil de visualisation et de mesure 3D développé par la HE-Arc repose sur Unity, offrant une application performante mais nécessitant une installation locale et un environnement spécifique.

L'évolution des technologies web, et en particulier l'émergence de **WebGPU**, ouvre la possibilité de proposer une solution de visualisation 3D avancée directement dans le navigateur, sans compromis majeur sur les performances graphiques. WebGPU permet un accès bas niveau aux capacités GPU modernes (compute shaders, pipelines explicites, gestion fine des buffers), rapprochant les performances web des applications natives.

Ce projet vise à porter l'outil SwissCollNet vers le web à l'aide d'un moteur 3D web moderne tel que **Babylon.js**, afin de proposer un outil multiplateforme, accessible, durable et mieux intégré aux écosystèmes muséaux.

## Objectifs

### Principaux

- Implémenter l'upload de scans HD permettant le calcul de vignettes basse définition ainsi que du modèle 3D. Le modèle 3D sera calculé en utilisant la technique du Gaussian Splatting.
- Concevoir et implémenter une version WebGPU allégée de l'outil de visualisation SwissCollNet. Il faudra en particulier reproduire les fonctionnalités clés comme :
  - navigation et interaction 3D,
  - affichage instantané des thumbnails,
  - affichage progressif des scans HD,
  - affichage du modèle 3D
- Assurer le streaming des données en arrière-plan. En particulier, le modèle 3D et les vignettes basse définition devront être chargés au démarrage. Les scans HD devront être chargés à la demande.

### Secondaires

- Mettre en place une base de données et une API utilisable par le viewer.
- Mettre en place un catalogue de spécimens disponibles accessibles directement depuis l'application.
- Implémenter un système de recherche de spécimens.
- Implémenter les fonctionnalités d'édition des informations liées aux spécimens.
