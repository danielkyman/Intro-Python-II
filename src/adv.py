from room import Room
from player import Player
from item import Item
import os

# items

items = {
    "rock": Item("Rock", "A large useless rock"),
    "dagger": Item("Dagger", "A dull rusty dagger"),
    "sword": Item("Sword", "A sharp heavy broadsword"),
}

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [items["rock"], items["dagger"]]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

new_player = Player("DANNY", room['outside'])


def current_room_name():
    return print(f"\nLocation: {new_player.current_room.name}")


def current_room_desc():
    print(f"Description: {new_player.current_room.description}")
    if new_player.current_room.items:
        item_logic()


def item_logic():
    print(
        f"\n!!!ITEM!!!")
    for item in new_player.current_room.items:
        print(f"{item.name}")
        item_answer = input(
            "Would you like to pick up the item[1]? or leave it [0]?")
        if int(item_answer) == 1:
            add_item(item)


def add_item(item):
    new_player.inventory.append(item)
    print(f"\nYou have added the {item.name} to your inventory!")


def user_input():
    print("\nWhich direction would you like to go? Enter one of the following:")
    print("[n] North")
    print("[e] East")
    print("[s] South")
    print("[w] West")
    print("[q] Quit")
    print("[i] Inventory")
    return input("Where would you like to go?")


def user_direction(dir):
    if dir.lower() == 'n':
        try:
            new_room = new_player.current_room.n_to
            new_player.current_room = new_room
        except AttributeError:
            print("\nYou cannot go any further in this direction")
    elif dir.lower() == 'e':
        try:
            new_room = new_player.current_room.e_to
            new_player.current_room = new_room
        except AttributeError:
            print("\nYou cannot go any further in this direction")
    elif dir.lower() == 's':
        try:
            new_room = new_player.current_room.s_to
            new_player.current_room = new_room
        except AttributeError:
            print("\nYou cannot go any further in this direction")
    elif dir.lower() == 'w':
        try:
            new_room = new_player.current_room.w_to
            new_player.current_room = new_room
        except AttributeError:
            print("\nYou cannot go any further in this direction")
    elif dir.lower() == 'i':
        if len(new_player.inventory):
            print(f"\nYou are currently carrying:")
            for item in new_player.inventory:
                print(f"A {item.name}")
        else:
            print(f"\nYou aren't carrying any items!")
    else:
        print("\nInput a valid direction")


choice = ""

while choice != "q":

    current_room_name()
    current_room_desc()
    choice = user_input()
    user_direction(choice)


print("\nThanks for playing")
