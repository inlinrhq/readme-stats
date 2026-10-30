# inlinr README stats

Your coding stats from [inlinr](https://inlinr.com) in your GitHub profile
README, refreshed every day: time coded, the share with an AI assistant,
languages, editors, your days. Text, a card, or both.

- **No secret, no token.** It reads your public profile at
  `inlinr.com/u/<handle>/readme.md` and commits with the repository's own
  `GITHUB_TOKEN`.
- **Options live in inlinr**, under Settings → README: text or card, period,
  lists, style. Change them there; this workflow never changes.
- **Your public profile is the ceiling.** Only what you chose to show in
  Settings → Sharing can appear. Never the hour you code, never a private
  project.
- **One commit only when the figures change.** No "last updated" date.

## Use it

1. In the README of your profile repository (`<you>/<you>`), put these two
   lines where the stats should go:

   ```markdown
   <!--START_SECTION:inlinr-->
   <!--END_SECTION:inlinr-->
   ```

2. Add `.github/workflows/inlinr.yml`:

   ```yaml
   name: inlinr stats
   on:
     schedule:
       - cron: "17 5 * * *"
     workflow_dispatch:
   permissions:
     contents: write
   jobs:
     update:
       runs-on: ubuntu-latest
       steps:
         - uses: inlinrhq/readme-stats@v1
   ```

3. Run it once from the Actions tab (Run workflow).

You need an inlinr account with public stats turned on (Settings → Sharing).
The editor extension or the Claude Code plugin sends the time.

## Inputs

| Input | Default | What it does |
|---|---|---|
| `handle` | the repository's owner | Your GitHub handle, as on inlinr. |
| `path` | `README.md` | The file holding the markers. |
| `commit-message` | `Update coding stats` | The commit's message. |
| `checkout` | `true` | `false` when an earlier step already checked the repository out. |
| `commit` | `true` | `false` to commit in a later step (with the `changed` output). |

Output: `changed` is `"true"` when the file changed.

## Coming from waka-readme-stats

Replace the step that uses `anmol098/waka-readme-stats` (or
`athul/waka-readme`) with `uses: inlinrhq/readme-stats@v1`, and delete the
`WAKATIME_API_KEY` and `GH_TOKEN` secrets: nothing replaces them. Your
markers change to the two above. What the block shows is chosen in inlinr.

## When it fails

- *no public stats*: turn them on in inlinr, Settings → Sharing, then save
  your choices in Settings → README.
- *no inlinr section*: the two marker lines are missing from the file.
- *could not reach inlinr.com*: nothing was changed; the next run tries again.
