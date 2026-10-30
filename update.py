"""Replace the inlinr section of a README with /u/<handle>/readme.md.

What the block holds (text, the card or both, the period, the lists) is
chosen in inlinr, Settings > README: this script only copies it in, so a
change of option never means editing the workflow.
"""

import os
import re
import sys
import urllib.error
import urllib.request

START = "<!--START_SECTION:inlinr-->"
END = "<!--END_SECTION:inlinr-->"
ORIGIN = "https://inlinr.com"
# GitHub's own rule for a user name.
HANDLE = re.compile(r"^[A-Za-z0-9](?:[A-Za-z0-9-]{0,37}[A-Za-z0-9])?$")


def fail(message):
    print(f"::error::{message}")
    sys.exit(1)


def fetch_block(handle):
    url = f"{ORIGIN}/u/{handle}/readme.md"
    request = urllib.request.Request(
        url, headers={"User-Agent": "inlinr-readme-stats/1"}
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return response.read().decode("utf-8").strip()
    except urllib.error.HTTPError as e:
        if e.code == 404:
            fail(
                f"@{handle} has no public stats on inlinr. Turn them on in "
                f"{ORIGIN}/dashboard/settings?section=sharing, then save your "
                f"choices in Settings > README."
            )
        fail(f"{url} answered {e.code}. Nothing was changed.")
    except urllib.error.URLError as e:
        fail(f"Could not reach {ORIGIN}: {e.reason}. Nothing was changed.")


def replace_section(readme, block):
    """The README with the block between the markers; None without them."""
    if START not in block or END not in block:
        fail("inlinr answered without its markers. Nothing was changed.")
    pattern = re.escape(START) + r".*?" + re.escape(END)
    if not re.search(pattern, readme, flags=re.S):
        return None
    return re.sub(pattern, lambda _: block, readme, count=1, flags=re.S)


def main():
    handle = os.environ.get("INLINR_HANDLE", "").strip()
    path = os.environ.get("INLINR_PATH", "README.md")
    if not HANDLE.match(handle):
        fail(f"'{handle}' is not a GitHub handle.")
    try:
        with open(path, encoding="utf-8") as f:
            readme = f.read()
    except FileNotFoundError:
        fail(f"{path} does not exist in this repository.")
    updated = replace_section(readme, fetch_block(handle))
    if updated is None:
        fail(
            f"{path} has no inlinr section. Add these two lines where the "
            f"stats should go, then run the workflow again:\n{START}\n{END}"
        )
    changed = updated != readme
    if changed:
        with open(path, "w", encoding="utf-8") as f:
            f.write(updated)
    print("Stats updated." if changed else "Stats unchanged.")
    output = os.environ.get("GITHUB_OUTPUT")
    if output:
        with open(output, "a", encoding="utf-8") as f:
            f.write(f"changed={'true' if changed else 'false'}\n")


if __name__ == "__main__":
    main()
