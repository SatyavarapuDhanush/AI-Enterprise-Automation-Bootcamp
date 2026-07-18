import tempfile
import unittest
from pathlib import Path

import organizer


class OrganizerTests(unittest.TestCase):
    def test_create_destination_folder(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            base_folder = Path(tmpdir)
            destination_folder = base_folder / "Documents"

            organizer.create_destination_folder(destination_folder)

            self.assertTrue(destination_folder.exists())
            self.assertTrue(destination_folder.is_dir())


if __name__ == "__main__":
    unittest.main()
