import random


class Room:
    # a class that represents one room in the dungeon.
    # todo add items to the dictionary for room descriptions.
    dict_contents = {0: "A block made of ice", 1: "A skull with flaming eyes."}

    def __init__(self, contents_str=None):

        # todo create a file so the values of the contents dictionary can have many values.
        # todo call an OpenAI API so it can fill in the description of the room's contents.

        self.contents = random.choice(list(Room.dict_contents))

        if type(contents_str) is not None:
            self.contents = contents_str

        # the wall's contents.

        self.dict_room_walls = {"North": "Blank", "South": "Blank", "East": "Blank", "West": "Blank"}

        # determining the values of the sides of the rooms.

    def whats_in_room(self):
        return self.contents

    def whats_on_walls(self, wall):
        return self.dict_room_walls[wall]

    def move_that_direction(self, direction):
        # Make sure that the direction chosen has an exit.

        pass


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
        # Call add_room from the map

        # Increment the number of steps upward.
        self.take_step()


class Map:
    # representing a collection of rooms.

    dict_directions = {"North": 1, "South": -1, "East": 1, "West": -1}

    def __init__(self):
        # initialize a list of rooms.
        self.instance_map = [[]]
        self.x_coordinate = 0
        self.y_coordinate = 0
        self.instance_map[0].append(Room())

    def move_room(self, direction):
        # create the new coordinate
        if direction == "East" or direction == "West":
            self.x_coordinate = self.x_coordinate + Map.dict_directions[direction]
            self.add_room_x()
        if direction == "North" or direction == "South":
            self.y_coordinate = self.y_coordinate + Map.dict_directions[direction]
            self.add_room_y()

    def current_room(self):
        return [self.x_coordinate, self.y_coordinate]

    def add_room_x(self):

        if isinstance(self.instance_map[self.x_coordinate][self.y_coordinate], Room):
            return None

        # need to figure out how to have a negative coordinate that doesn't count from the back of the list

        self.instance_map[self.x_coordinate] = Room()

    def add_room_y(self):

        if isinstance(self.instance_map[self.x_coordinate][self.y_coordinate], Room):
            return None

        self.instance_map[self.x_coordinate] = Room()


'''

This is a basic version of the Adventure game. It is completely text-based.
In this version of the game, users can move about through different rooms within a single setting,
and based on the user input, it will provide descriptions for each room. This is one of the
interesting python projects.

Movement direction is crucial here – you must create walls and set the directions in which the
users can move through the rooms, set movement restrictions, and also include a tracker that can
track how far a user has walked or moved in the game.

'''

if __name__ == '__main__':

    entered_commands = ["contents", "walls", "north", "south", "east", "west", "exit"]
    # Creates both the map and the first room.
    player_map = Map()
    player = Player()

    player_entry = input("Please enter a command (For list of commands, enter command): ").lower()

    while player_entry not in entered_commands:
        print("That is not a valid command.")
        player_entry = input("Please enter a command (For list of commands, enter command): ")

    # if the player exits, then the whole thing is over.
    # if player_entry == "exit":
        # break

    if player_entry in entered_commands[2:5]:
        player.move_person(player_map, player_entry)

    # Pass the direction of travel to the Person, who moves in that direction.

    # create a room
    # new_room = Room(coordinate_x, coordinate_y)

# todo Room instances should have values for the walls for N, S, E, W.
# todo The value for a wall should be either a blank wall or a passage.
# todo the room should contain something of note.
# todo The user should provide input for choosing a direction.
# todo upon choosing a direction, the program should create a new room.
# todo new room creation needs to have a passage that connects back to the previous.
# todo an option for the player should be to display the map.
# todo rooms should contain passages that connect to existing room.
