import unittest

import main


class TestRoom(unittest.TestCase):
    def test_contents(self):
        test_room = main.Room("Test contents.")
        contents = test_room.whats_in_room()
        self.assertEqual(contents, "Test contents.")


class TestPlayer(unittest.TestCase):
    def test_take_step(self):
        test_player = main.Player()
        test_player.take_step()
        self.assertEqual(test_player.num_steps(), 1)


if __name__ == '__main__':
    unittest.main()
