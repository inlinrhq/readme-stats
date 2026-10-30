import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import update  # noqa: E402

BLOCK = f"{update.START}\n### Coding stats\n{update.END}"


class ReplaceSection(unittest.TestCase):
    def test_replaces_only_between_the_markers(self):
        readme = f"Hi\n\n{update.START}\nold\n{update.END}\n\nBye\n"
        self.assertEqual(
            update.replace_section(readme, BLOCK), f"Hi\n\n{BLOCK}\n\nBye\n"
        )

    def test_none_without_markers(self):
        self.assertIsNone(update.replace_section("Hi\n", BLOCK))

    def test_backslashes_in_the_block_stay_as_they_are(self):
        block = f"{update.START}\n| a \\| b |\n{update.END}"
        readme = f"{update.START}\n{update.END}"
        self.assertEqual(update.replace_section(readme, block), block)

    def test_handles(self):
        self.assertTrue(update.HANDLE.match("7IBO"))
        self.assertTrue(update.HANDLE.match("a-b"))
        self.assertFalse(update.HANDLE.match("-a"))
        self.assertFalse(update.HANDLE.match("a/b"))
        self.assertFalse(update.HANDLE.match("../x"))


if __name__ == "__main__":
    unittest.main()
