#!/usr/bin/env python3

import sys


verbose = False


class Room:
    def __init__(self, name, contents=None):
        self.name = name
        self.contents = [] if contents == None else contents
   
    def __str__(self):
        return self.name


class FloorPlan:
    rooms = []  # All the rooms that have been created.
    room_connections = {} # Dict keys are (room_name, direction) pairs; Values are rooms
    TREASURE = "A calendar that's missing half of April and all of May"
    WINNING_ROOM_NAME = ''

    def connect_rooms(room_a, dir_a_to_b, dir_b_to_a, room_b):
        """Add a two-way connection between to already existing rooms"""
        name_a = room_a.name
        name_b = room_b.name
        if not FloorPlan.is_room_name_in_floorplan(name_a):
            print('ERROR: Unknown room: {0:s}'.format(name_a))
            sys.exit(-1)
        if not FloorPlan.is_room_name_in_floorplan(name_b):
            print('ERROR: Unknown room: {0:s}'.format(name_b))
            sys.exit(-1)
        # Q: What happens if a connection is formed that goes
        #    from 'Room A' in the direction 'West' to 'Room B',
        #    and then another connection is formed with the same room & direction,
        #    but this time it connects to 'Room C'?
        if verbose:
            print('INFO: Adding connection from {0:s}->({1:s})->{2:s}'
                .format(name_a, dir_a_to_b, name_b))
        FloorPlan.room_connections[(room_a.name, dir_a_to_b)] = room_b
        if verbose:
            print('INFO: Adding connection from {0:s}->({1:s})->{2:s}'
                .format(name_b, dir_b_to_a, name_a))
        FloorPlan.room_connections[(room_b.name, dir_b_to_a)] = room_a

    def create_room(name):
        # The name must be original, i.e., not used before.
        if not FloorPlan.is_room_name_original(name):
            print('ERROR: Duplicate room name: {0:s}'.format(name))
            sys.exit(-1)
        room = Room(name)
        FloorPlan.rooms.append(room)
        if verbose:
            print('INFO: Room created and added to floor plan: {0:s}'.format(name))
        return room

    def get_room_by_name(name):
        rooms = [room for room in FloorPlan.rooms if room.name == name]
        if len(rooms) == 0:
            print('ERROR: Unrecognized room name: {0:s}'.format(name))
            sys.exit(-1)
        elif len(rooms) > 1:
            print('ERROR: Multiple rooms with the same name: {0:s}'.format(name))
            sys.exit(-1)
        return rooms[0]

    def is_room_name_in_floorplan(name):
        return name in [room.name for room in FloorPlan.rooms]

    def is_room_name_original(name):
        return name not in [room.name for room in FloorPlan.rooms]


class Player:
    STILL_PLAYING = 0
    WON = 1

    def __init__(self, name, location):
        self.name = name
        self.location = location

    def go(self, direction):
        room_name = self.location.name
        if not FloorPlan.is_room_name_in_floorplan(room_name):
            print('ERROR: No such room ({0:s})!'.format(room_name))
            sys.exit(-1)
        key = (self.location.name, direction)
        if verbose:
            print('INFO: key={0:s}'.format(str(key)))
        if key not in FloorPlan.room_connections:
            print('ERROR: No path from {0:s} in direction {1:s}'
                .format(room_name, direction))
            sys.exit(-1)
        next_room = FloorPlan.room_connections[key]
        self.location = next_room
        if verbose:
            print('INFO: Player {0:s} is now in room: {1:s}'
                .format(self.name, self.location.name))
        if self.location.name == FloorPlan.WINNING_ROOM_NAME:
            print("Congrats!!!  You've reached the winning room!!!")
            print("  Your treasure: {0:s}.".format(FloorPlan.TREASURE))
            return Player.WON
        else:
            return Player.STILL_PLAYING

    def play(self):
        directions = ['N', 'SE', 'E', 'SW']
        for direction in directions:
            if self.go(direction) == Player.WON:
                break


def main():
    # Setup
    room1 = FloorPlan.create_room('Room #1')
    room2 = FloorPlan.create_room('Room #2')
    room3 = FloorPlan.create_room('Room #3')
    room4 = FloorPlan.create_room('Room #4')
    room5 = FloorPlan.create_room('Room #5')
    room6 = FloorPlan.create_room('Room #6')
    room7 = FloorPlan.create_room('Room #7')
    room8 = FloorPlan.create_room('Room #8')
    room9 = FloorPlan.create_room('Room #9')

    FloorPlan.connect_rooms(room1, 'E', 'W', room6)
    FloorPlan.connect_rooms(room1, 'W', 'E', room8)

    FloorPlan.connect_rooms(room2, 'NW','SE',room5)
    FloorPlan.connect_rooms(room2, 'N', 'S', room7)
    FloorPlan.connect_rooms(room2, 'W', 'E', room9)

    FloorPlan.connect_rooms(room3, 'S', 'N', room4)
    FloorPlan.connect_rooms(room3, 'N', 'S', room8)

    FloorPlan.connect_rooms(room4, 'NE','SW',room5)
    FloorPlan.connect_rooms(room4, 'E', 'W', room9)

    FloorPlan.connect_rooms(room5, 'NE','SW',room6)
    FloorPlan.connect_rooms(room5, 'NW','SE',room8)

    FloorPlan.connect_rooms(room6, 'S', 'N', room7)

    FloorPlan.WINNING_ROOM_NAME = 'Room #9'
 
    # Here we go!
    player = Player('Theseus', location=room1)
    player.play()


if __name__ == '__main__':
    main()
