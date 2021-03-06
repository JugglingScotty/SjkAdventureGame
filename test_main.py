import unittest
import main


class TestRoom(unittest.TestCase):
    def test_contents(self):
        test_room = main.Room("Test contents.")
        contents = test_room.whats_in_room()
        self.assertEqual(contents, "Test contents.")

    def test_whats_on_walls(self):
        # todo need to change this unit test so it reflects what is in the dictionary.
        test_room = main.Room("Test contents.")
        contents = test_room.whats_on_walls("North")
        self.assertEqual(contents, "Blank")

    def test_add_room_no_room(self):
        pass

    def test_add_room_room_present(self):
        pass


class TestPlayer(unittest.TestCase):
    def test_take_step(self):
        test_player = main.Player()
        test_player.take_step()
        self.assertEqual(test_player.num_steps(), 1)


class TestMap(unittest.TestCase):
    def test_map_creation(self):
        test_map = main.Map()
        self.assertIsInstance(test_map.instance_map[0][0], main.Room)


if __name__ == '__main__':
    unittest.main()
