# Blowfish — copie vendorée

- **Version** : 2.84.0
- **Upstream** : https://github.com/nunocoracao/blowfish (tag `v2.84.0`)
- **Nature de la copie** : partielle. Seuls les répertoires lus par Hugo sont présents
  (`archetypes/`, `assets/`, `config/`, `data/`, `i18n/`, `layouts/`, `static/`) plus
  `config.toml`, `theme.toml`, `tailwind.config.js`, `package.json`, `LICENSE`.

Volontairement absents : `exampleSite/` (49 Mo), `images/`, `.github/`, `README.*`,
`netlify.toml`, `lighthouserc.js`, `go.mod`, `gen*.js`, `processUsers.js`,
`findMissingTranslations.js`, `release-versions/`, `package-lock.json`.

## Mettre à jour le thème

Pas de submodule ni de Hugo Module : la mise à jour est manuelle.

1. Récupérer le tag voulu depuis l'upstream.
2. Remplacer les répertoires listés ci-dessus.
3. Vérifier `[hugoVersion]` dans `themes/blowfish/config.toml` et aligner
   `config/_default/module.toml` et `HUGO_VERSION` dans `.github/workflows/gh-pages.yml`.
4. Relire les overrides du site (`layouts/_default/list.html`, `layouts/_default/index.json`,
   `layouts/partials/project-*.html`) : ils dépendent de partials du thème.
5. Recompiler le CSS : `npm ci && npm run css:build`, puis committer
   `assets/css/compiled/main.css`.

## Modification locale

Aucune. Le thème est intact ; toutes les personnalisations vivent dans `layouts/`,
`assets/` et `i18n/` à la racine du site.
