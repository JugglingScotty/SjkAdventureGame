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


class Player:
    # contains the number of steps moved so far.

    def __init__(self):
        self.steps = 0

    def take_step(self):
        self.steps += 1

    def num_steps(self):
        return self.steps


class Map:
    # representing a collection of rooms.
    def __init__(self):
        # initialize a list of rooms.
        pass

    def add_room(self, room):
        # check if the room shares a wall .
        # add the room to the end of the list.
        pass


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

    coordinate_x = 0
    coordinate_y = 0

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
