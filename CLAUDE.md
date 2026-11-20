# readme-stats

> **Socle commun** : les règles partagées par toutes les apps de Thibault
> (attribution, identité git, PR, relecture, qualité, textes, CI, Linear)
> sont dans le dépôt `7IBO/socle` : lis son CLAUDE.md, puis le fichier du
> sujet. Ce fichier ne garde que ce qui est propre à ce dépôt et gagne en
> cas d'écart.

Public GitHub Action that writes a user's inlinr stats into their README
(`action.yml`, `update.py`). Python standard library only, tests in
`tests/` (`python3 -m unittest discover -s tests -v`).

- Public repository: no internal path, host, ticket id or private detail in
  code, commits or pull requests.
- Release: change `VERSION` in a pull request; its merge to main tags and
  releases (`.github/workflows/release.yml`).
- The server side (the API it reads) lives in `inlinrhq/inlinr-web`.
