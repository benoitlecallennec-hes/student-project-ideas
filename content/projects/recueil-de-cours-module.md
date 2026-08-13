---
title: "Recueil de descriptifs de module"
date: 2026-02-13
description: "Générer un site statique des descriptifs de modules depuis les fichiers JSON, avec un CMS headless pour que chaque professeur mette à jour son cours, et un graphe des compétences."
summary: "Générer un site statique des descriptifs de modules depuis les fichiers JSON, avec un CMS headless pour que chaque professeur mette à jour son cours, et un graphe des compétences."
categories:
  - "Cours GELO"
  - "P3 HES d'été"
statuts:
  - "Prospection"
tags:
  - "Python"
  - "SmartData"
---
Voir projet pilote : https://gitlab-etu.ing.he-arc.ch/isc/2025-26/niveau-2/2245.2-g-nie-logiciel-2-isc2id-ie/modex

## Technologies
Site statique : Hugo (Go), contenu en markdown.
CMS Headless : Sveltia CMS

## Contexte
Le recueil des descriptifs de modules fourni un ensemble de fichiers PDF.
Les informations initiales sont stockées sous forme de fichiers Word qui doivent être mis à jour chaque année.
À partir des informations des modules en Json (voir projet pilote), générer un site statique avec Hugo, et un graphe des compétences.
Chaque cours devra avoir une page dédiée, avec les tags associés (niveau, filière, type de cours, etc.).
Le site devra contenir un graphe des compétences.
Enfin, chaque professeur devra pouvoir mettre à jour les informations de son cours via un CMS headless (Sveltia CMS).

## Objectifs principaux
1. Générer un site statique à partir des fichiers Json existants
2. Mettre en place un CMS headless pour permettre aux professeurs de mettre à jour les informations de leur cours
3. Générer un graphe des compétences à partir des informations des cours en intégrant les dépendances entre les compétences et les cours
4. Mettre en place un workflow CI/CD pour automatiser la génération du site statique et du graphe des compétences à chaque mise à jour des informations des cours

## Objectifs secondaires
1. Mettre en place un système de recherche et de filtrage des cours sur le site statique
2. Mettre en place un système de validation des informations des cours avant leur publication sur le site statique
3. Mettre en place un système de notifications pour informer les professeurs des mises à jour de leurs cours

## Critères d'évaluation

Les critères sont chiffrés et, autant que possible, mesurés **sans évaluateur humain**.
Ce qui reste subjectif est évalué par des personnes **extérieures à l'encadrement**.

Les critères suivants ne sont que des suggestions.
Il faut les revoir, et les ajuster le cas échéant.

Les valeurs notées **N**, **X**, **Y** et **T** sont à calibrer par l'équipe projet, puis
à faire valider : **N** modules dans le recueil, un panel de **X** professeurs dont **Y**
doivent réussir, **T** minutes de temps imparti par tâche.

### Mesures automatiques

- Couverture : **100 %** des **N** modules des fichiers JSON ont une page générée, **0** page en erreur
- Fidélité : **0 écart** entre les champs du JSON et ceux affichés, par comparaison champ par champ sur les **N** modules
- **0** module publié avec un champ obligatoire manquant
- Codes et nommage des modules : **100 %** conformes au format attendu, vérifié par la suite de tests
- Graphe des compétences : **0 cycle** de dépendances, et **0 référence orpheline** — toute dépendance déclarée pointe vers un cours ou une compétence qui existe
- Régénération sans modification : **0 diff** produit, la chaîne est idempotente
- Publication après une mise à jour dans le CMS : **< T min** et **0 intervention manuelle**
- Suite de tests : **100 %** verte, **0 régression** tolérée sur les contraintes de nommage et de codes
- Génération du site complet : **< T min**
- Affichage d'une page de module : **< 1 s** ; recherche et filtrage sur les **N** modules : **< 200 ms**

### Panel de X professeurs extérieurs au projet

C'est le critère décisif : un CMS que les professeurs n'utilisent pas ne sert à rien.
Ni les étudiants du projet, ni les enseignants encadrants.
Critère d'inclusion : **n'avoir jamais utilisé le CMS**.

**Protocole.** Chacun reçoit ses identifiants et la seule documentation, et doit mettre à
jour un champ du descriptif de son propre module, puis vérifier la modification en ligne.
Chronomètre lancé, **aucune aide** : l'observateur note sans intervenir.
Échec au-delà de **T** minutes.

- Publient leur modification sans aide dans le temps imparti : **Y sur X**
- Ont eu besoin d'accéder au dépôt Git, à la ligne de commande ou de connaître Markdown : **0** — c'est la raison d'être d'un CMS headless
- Temps médian jusqu'à la modification visible en ligne : **< T / 2**
- « Je mettrais à jour mon module ainsi plutôt qu'en renvoyant un fichier Word », note de 1 à 5 : **moyenne ≥ 4**

### Panel d'étudiants extérieurs au projet

**Protocole.** Chacun reçoit une question du type « quel module couvre tel sujet ? » ou
« quels sont les prérequis de tel module ? », et doit y répondre à partir du site seul.

- Trouvent la bonne réponse dans le temps imparti : **≥ 80 %** du panel
- Temps médian de réponse, comparé au recueil de PDF actuel sur les mêmes questions : **réduit de ≥ 50 %**
- Identifient correctement les prérequis d'un module depuis le graphe des compétences : **≥ 80 %** du panel

### Responsable de filière

- Graphe des compétences jugé fidèle aux dépendances réelles du plan d'études : **0 erreur bloquante**
- Descriptifs publiés jugés utilisables tels quels pour la communication officielle : **0 remarque bloquante**
- Documentation d'exploitation : **≤ 2 pages**, jugée suffisante pour reprendre le service sans ses auteurs
