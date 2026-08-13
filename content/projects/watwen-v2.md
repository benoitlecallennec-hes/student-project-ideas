---
title: "WatWen V2"
date: 2025-12-18
description: "WatWen est une application web et mobile de gestion d'événements."
summary: "WatWen est une application web et mobile de gestion d'événements."
categories:
  - "TB"
statuts:
  - "Prospection"
nature: "Enseignement"
---

WatWen est une application web et mobile de gestion d'événements.

## Contexte

Quels cours sont prévus aujourd'hui ? Dans quelle salle ? Que puis-je faire ce week-end à Neuchâtel ?
WatWen permet de répondre à toutes ces questions. Un 1er prototype est déjà disponible : [démo vidéo](https://youtu.be/rYUEK1rYmeg?si=uSlcHSA_KaFaZGng). Le dépôt du prototype est interne à la HE-Arc et sera communiqué au démarrage du projet.

**Le but de ce projet est de continuer le développement de l'application WatWen et de la rendre production-ready (Web et Mobile).**

## Objectifs

### Principaux

- **[App Web et App Mobile]** Prendre connaissance de la version existante, de sa conception, et analyser les pistes d'amélioration. En particulier, il faudra revoir et valider l'UX avec l'expert.
- **[App Web]** Porter les fonctionnalités de l'App Mobile vers l'App Web.
- **[App Web]** Implémenter un système de collecte de données à partir de fichiers. Ces fichiers seront par exemple les horaires de cours de la HE-Arc.
- **[App Web]** Implémenter un système permettant d'extraire les événements à partir d'emails. Les événements extraits seront ensuite stockés en attendant d'être relus, puis publiés.

### Secondaires (à choix)

- Implémenter un système de collecte de données à partir de sites web (sites de la HES-SO — HE-Arc compris —, cinémas, salles de concerts, clubs de foot, etc.).
- Implémenter un système permettant de connecter ses calendriers (Outlook, Google Calendar, etc.).
- Concevoir, implémenter et valider un système de détection de doublons (parfois similaires mais présentés de manière différente).
- Implémenter un système de modération / reporting pour vérifier que les données collectées sont toujours valides.
- Concevoir un système de liaison entre appareils par QR code (comme WhatsApp).
- Concevoir un système de partage d'événements (ou d'ensembles d'événements) par QR code.
- Investiguer la possibilité de publier l'App Mobile sur les app stores classiques.
