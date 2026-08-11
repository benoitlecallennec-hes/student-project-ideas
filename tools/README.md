# tools/

## `import_projets.py`

Script **one-shot**, exécuté une seule fois le **2026-08-11** sur
`D:\HE-Arc_WorkingFilesSYNC\COURS\3282.1-P3-TB\projets` (53 fichiers) pour amorcer
`content/`.

**Ne pas le relancer.** Il supprime et réécrit tous les `.md` de `content/sujets/` et
`content/realisations/`, ce qui effacerait les corrections apportées à la main depuis
l'import. `content/` est la source de vérité du site ; les deux dépôts ont divergé.

```bash
python tools/import_projets.py <chemin/vers/projets> --dry-run   # journal sans rien écrire
```

### Ce qu'il a fait

Front matter : `titre`→`title`, `cree`→`date`, `statut`→`statuts` (liste, valeur
anglaise conservée), `categories` inchangées (`[]` → `Non classé`), `tags` inchangés,
`type`→`nature` (`type` est réservé par Hugo : il pilote le lookup des layouts).
`notion` et `priorite` sont **supprimés** — l'URL Notion est privée et le dépôt est
public ; la correspondance slug ↔ Notion reste dans le dépôt source.

Corps : retrait du H1 de tête (Blowfish rend déjà `.Title` en `<h1>`), des deux
familles de blockquotes laissées par la migration Notion, des sections `## Mandants`
(aucun nom de personne sur le site public) et de la ligne mentionnant une étudiante ;
réécriture des liens `](slug.md)` en `{{< relref "/section/slug" >}}`.

`summary` et `description` sont dérivés du premier paragraphe (≤ 180 car.). Quand il
n'y en a pas, `summary` est **omis** — c'est ce qui déclenche la mention « Sujet à
préciser » dans la liste — et `description` reçoit une phrase générique.

### Reprises manuelles après l'import

Le script signale ce qu'il ne sait pas réécrire. Quatre fiches ont été corrigées à la
main ensuite :

| Fiche | Correction |
|---|---|
| `sujets/geexlab-skeletal-animation.md` | `## Voir Email Christophe Muller` supprimé, `## À FAIRE` devenu `## Objectifs`, checklist `- [ ]` convertie en liste, intro ajoutée |
| `realisations/spatialisation-sonos-era-300.md` | nom d'étudiant et chemin `suivi/2025-2026/P3/` retirés de `## Réalisation` |
| `sujets/watwen-v2.md` | URL GitLab interne remplacée par une mention |
| `content/_index.md` | `TODO-CONTACT` à remplacer par l'adresse de contact |

### Encore à relire

Environ 6 fiches où le premier paragraphe fait un résumé médiocre (lien brut ou note
de service) : `chaos-of-legends`, `kinect-unity-vfx-graph`, `paint-your-town`,
`udimu-lattice-boltzmann`, `gamifying-c-programming-learning`,
`gamifier-le-calcul-mental`. Corriger le champ `summary` directement dans `content/`.
