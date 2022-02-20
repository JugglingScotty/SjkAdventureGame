import random
import csv
import shutil


class Room:
    # a class that represents one room in the dungeon.
    dict_contents = {}

    def __init__(self):

        all_contents = list(Room.dict_contents.values())
        self.contents = random.choice(all_contents)

        self.dict_room_walls = {"north": "a door", "south": "a door", "east": "a door", "west": "a door"}

        # determining the values of the sides of the rooms.

    @classmethod
    def set_room_dict(cls):
        # make a copy of the existing file.
        original = "contents.csv"

        with open(original, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    print(f'Column names are {", ".join(row)}')
                    line_count += 1
                this_room_key = row["room_key"]
                this_descr = row["descr"]
                line_count += 1
                cls.dict_contents[this_room_key] = this_descr

    def whats_in_room(self):
        return "The room contains: " + self.contents

    def whats_on_walls(self):
        north_wall = ("The north wall contains " + self.dict_room_walls["north"])
        south_wall = ("The south wall contains " + self.dict_room_walls["south"])
        east_wall = ("The east wall contains " + self.dict_room_walls["east"])
        west_wall = ("The west wall contains " + self.dict_room_walls["west"])
        return north_wall, south_wall, east_wall, west_wall

    def can_player_move_that_direction(self, direction):
        # Make sure that the direction chosen has an exit.
        if self.dict_room_walls[direction] == "Blank":
            return False
        else:
            return True

    def map_str(self):
        return "╬"


class Player:
    # contains the number of steps moved so far.

    def __init__(self):
        self.steps = 0

    def take_step(self):
        self.steps += 1

    def num_steps(self):
        return self.steps

    def move_person(self, p_map, direction):

        # Call Move that direction from the room.
        p_map.move_room(direction)
        # Present the contents of the next room.
        # current_r = p_map.current_room()
        room_contents = p_map.current_room().whats_in_room()
        print(room_contents)
        self.take_step()

class Map:
    # representing a collection of rooms.

    dict_directions = {"north": 1, "south": -1, "east": 1, "west": -1}

    def __init__(self):
        # initialize a list of rooms.
        self.x_coordinate = 0
        self.y_coordinate = 0
        self.instance_map = {self.x_coordinate: {}}
        self.add_room()

    def move_room(self, direction):

        # todo figure out why north on the map adds boxes to the right.

        if not self.current_room().can_player_move_that_direction(direction):
            print("Player cannot move that direction.")
            return None

        # up the the counter to the new coordinate
        if direction == "east" or direction == "west":
            self.x_coordinate = self.x_coordinate + Map.dict_directions[direction]
            self.add_x()
        if direction == "north" or direction == "south":
            self.y_coordinate = self.y_coordinate + Map.dict_directions[direction]
            self.add_room()

    def current_room(self):
        return self.instance_map[self.x_coordinate][self.y_coordinate]

    def add_x(self):

        try:
            if isinstance(self.instance_map[self.x_coordinate], dict):
                return None
        except KeyError:
            self.instance_map[self.x_coordinate] = {}
            self.add_room()

    def add_room(self):

        new_room = Room()
        try:
            if isinstance(self.instance_map[self.x_coordinate][self.y_coordinate], Room):
                return None
        except KeyError:
            self.instance_map[self.x_coordinate][self.y_coordinate] = new_room

    def show_map(self):

        map_for_printing = ""

        x_lowest_value = 0
        x_highest_value = 0
        y_lowest_value = 0
        y_highest_value = 0

        for x_dict_key in self.instance_map.keys():
            if x_lowest_value > x_dict_key:
                x_lowest_value = x_dict_key
            if x_highest_value < x_dict_key:
                x_highest_value = x_dict_key

        for x_dict_values in self.instance_map.keys():
            for y_dict_values in self.instance_map[x_dict_values].keys():
                if y_lowest_value > y_dict_values:
                    y_lowest_value = y_dict_values
                if y_highest_value < y_dict_values:
                    y_highest_value = y_dict_values

        for x in range(y_lowest_value, y_highest_value + 1):
            for y in range(x_lowest_value, x_highest_value+1):
                try:
                    map_for_printing = map_for_printing + self.instance_map[x][y].map_str()
                except KeyError:
                    map_for_printing = map_for_printing + " "

            map_for_printing = map_for_printing + "\n"

        # todo need to improve the formatting on the map
        return map_for_printing


'''

This is a basic version. of the Adventure game. It is completely text-based.
In this version of the game, users can move about through different rooms within a single setting,
and based on the user input, it will provide descriptions for each room. This is one of the
interesting python projects.

Movement direction is crucial here – you must create walls and set the directions in which the
users can move through the rooms, set movement restrictions, and also include a tracker that can
track how far a user has walked or moved in the game

'''

if __name__ == '__main__':

    Room.set_room_dict()

    viable_commands = ["contents", "walls", "north", "south", "east", "west", "steps", "map", "exit"]
    # Creates both the map and the first room.
    player_map = Map()
    player = Player()

    print("You find yourself in a room.")
    current_room = player_map.current_room()
    contents = current_room.whats_in_room()
    print(contents)

    while True:

        player_entry = None
        while player_entry not in viable_commands:
            if player_entry is not None:
                print("That is not a valid command.")
            player_entry = input("Please enter a command: ").lower()

        # if the player exits, then the whole thing is over.
        if player_entry == "exit":
            break

        if player_entry == viable_commands[0]:
            current_room = player_map.current_room()
            contents = current_room.whats_in_room()
            print(contents)

        if player_entry == viable_commands[1]:
            # display the content of all the walls
            current_room = player_map.current_room()
            north, south, east, west = current_room.whats_on_walls()
            print(north)
            print(south)
            print(east)
            print(west)

        if player_entry in viable_commands[2:6]:
            # move the person in the direction they indicated.
            player.move_person(player_map, player_entry)
        if player_entry == viable_commands[6]:
            # output the number of steps traveled
            print("The number of steps taken is: ", player.num_steps())
        if player_entry == viable_commands[7]:
            # method for displaying the map
            print_map = player_map.show_map()
            print(print_map)
        if player_entry == viable_commands[-1]:
            break

# improvement option - make having a door randomized.
# improvement option - detect whether an adjacent room has a door into the current room.
# improvement option - new room creation needs to have a passage that connects back to the previous.
