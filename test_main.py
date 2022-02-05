import unittest

import main


class TestRoom(unittest.TestCase):
    def test_contents(self):
        test_room = main.Room(1, 1)
        contents = test_room.whats_in_room()
        self.assertEqual(contents, "A skull with flaming eyes.")


if __name__ == '__main__':
    unittest.main()
