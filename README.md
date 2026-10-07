# Tongtong Liang’s homepage

Jekyll academic website published at https://tongtongliang.github.io.

## Editing content

- `_pages/about.md`: biography and homepage paper list.
- `_pages/experience.md`: education and experience.
- `_data/papers.json`: shared paper titles, authors, venues, links and abstracts. The homepage and Papers page both read this file. Use `section: preprints` or `section: publications`; optional `spotlight: true` adds a badge.
- `_pages/papers.md`: paper sections and mathematics notes.
- `files/`: the four PDF notes linked from Papers.
- `_config.yml`: site identity and sidebar links.
- `_data/navigation.yml`: top navigation.
- `images/profile.jpg`: profile photograph.

The old `/publications/` and two `/publication/...` URLs redirect to `/papers/`. The XML sitemap is generated automatically. Sample blogs, CVs, talks, teaching records, portfolios and their tools have been removed.

## Residual-Stream Burden project page

`residual-stream-burden/` contains the published HTML and assets from the paper
repository's `docs/` directory. It is served unchanged as a static page at
`https://tongtongliang.github.io/residual-stream-burden/`. Its link is shared by
the homepage and Papers page through `_data/papers.json`.

After updating the page in the paper repository, sync the latest GitHub version:

```sh
python3 scripts/sync_residual_project.py
```

To use an existing checkout instead, pass `--source /path/to/residual-stream-burden`.
The source commit is recorded in `residual-stream-burden/.upstream.json`.
Edit the blog in its original writing project and publish it to the paper repo
before syncing here; a sync overwrites the copied page and assets.

## Local preview

Install Ruby and Bundler, then run:

```sh
bundle install
bundle exec jekyll serve
```

Open http://localhost:4000. To check a production build, run `bundle exec jekyll build`.

MathJax loads only on pages declaring `mathjax: true`. JavaScript source and build scripts remain available; run `npm install` then `npm run build:js` after changing `assets/js/_main.js`. Keep `assets/js/theme.js`, which is imported by the shared script.

## Theme

Based on Academic Pages and Minimal Mistakes. The original MIT license is retained in `LICENSE`.
