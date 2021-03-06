# Sample Python code that can be used to generate rooms in
# a zig-zag pattern.
#
# You can modify generate_rooms() to create your own
# procedural generation algorithm and use print_rooms()
# to see the world.

import random
from adventure.models import Room


roomTitles = ["Foyer","Grand Overlook","Narrow Passage", "Treasure Chamber", "Kitchen", "Kitchen Storage","Back Garden", "Dinning hall", "Lily Garden","waterwfall", "Tulip Garden", "Rose Garden", "Queen's chamber", "Throne room", "Solar"
                "The Dungeon", "Turret", "Chambers", "Royal Heirs", "Princess' room", "Prince's room", "Landing", "Banquet hall", "Banquest Hallway", "Party room",'Main Garden', "Garden Hallway One", "Garden Hallway Two",  "Garden Hallway Three"
            ]

descriptions = ["You're currently in the kitchen, you can move west to return to previous room or east to visit the storage. Would the storage be a cleaver place to hide treasure? You can have a look",
                "Maybe inbetween food isnt such a smart place to save treasure after all. Return to kitchen on the west or heard into the back garden on the north",
                "No treasure here today but dont give up! There are other parts of the castle to explore. Head south to return into the storage",
                "Don't get distracted by the delicious feast,there is no treasure here. You can return to the previous room on the south",
                "You're currently in a different part of the garden, forge forward to the rose garden on the north to see if the treasure is hidden somewhere, you may also exit to the main garden on the west or return to back garden on the south",
                "This is a pretty waterfall but no treasure here, You may go back to the garden on the south",
                "Oops! More flowers. Unfortunatly only flowers here, you may go north to the waterfall or east to the rose garden",
                "Pick a nice rose for your loved one on your way but you may need the room for enough treasure, head north to see where it leads you",
                "If playing dress up is your thing, this might be the room for you. Unfortunately not the kind of treasure you want this time! Head east to exit the roo",
                "You've reached the throne room, you could take a nap or return to previous room on the south to continue your treasure hun",
                "This is where the royals have family time, unfortunately no treasures here. But you may choose to go north to enter the chambers to see what is there",
                "You're in the dungeon, shh! move quietly so as not to alert the angry prisoners. You can move *** to return to previous room or *** to move to the turret ",
                "Fancy a party? Sure, stay! but someone might grab the treasure before you. Go *** to head to the *** instead" ,
                "Surely the treasure must be in one of the chambers but which one? Head north to go into the throne room west to go into the Queen's chamber, east to go into the wing that holds the royal heirs or south to return to the solar room ",
                "Makes sense to keep all treasures in the same spot? let's see if any of the rooms in this wing hold the treasure you seek. Head north to go into the princess' chamber or south to head into the prince's chamber. You can also head west to return to the hallway of the chambers.",
                "Boo! No luck here. You may head south to leave room ",
                "No luck here either.You may head south to leave room ",
                "You have now entered the north wing of the castle, You may go north to the solar room, east to the kitchen or west to the banquet hall",
                "You are now in the banquet hall, join the party if you want but the treasure might go to someone who works more. Go east to return to the landing or north to go to the hallway",
                "The hallway would be a silly place to hide some treasure wouldn't it? Go south to return to the banquet hall or east to go to the *** ",
                "More party! I know you just want some treasure, dont give up! you can go west to return to the hallway or east to return to head into the banquet room for some comfort food",
                "You are in the main garden now, this would make a perfect location for a reception, unfortunately no treasure here. You may return to the party room on the South or go west to explore another hallway.",
                "We know now that hallways have no treasures. No, not even behind an imaginary save behind the painting. Head east to return to the garden or south to explore more hallways, it might lead somewhere ",
                "It is a really long hallway, go south to keep going or north to return to previous hallway",
                "We are almost at the end of this hallway now! You've come so far, don'g give up but if you wish, you may go back to the previous hallway by going north or to the next room by heading east",
                "Welcome to the castle! Your quest begins you may head north, west or east to explore the castle or head south to exit the castle",

                 ]

class World:
    def __init__(self):
        self.grid = None
        self.width = 0
        self.height = 0
        self.list1 = []
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None



    def generate_rooms(self, size_x, size_y, num_rooms):
        '''
        Fill up the grid, bottom to top, in a zig-zag pattern
        '''

        # Initialize the grid
        self.grid = [None] * size_y
        self.width = size_x
        self.height = size_y
        for i in range( len(self.grid) ):
            self.grid[i] = [None] * size_x

        # Start from lower-left corner (0,0)
        x = -1 # (this will become 0 on the first step)
        y = 0
        room_count = 0

        # Start generating rooms to the east
        direction = 1  # 1: east, -1: west


        # While there are rooms to be created...
        previous_room = None
        while room_count < num_rooms:
            print(room_count)

            # Calculate the direction of the room to be created
            if direction > 0 and x < size_x - 1:
                room_direction = "e"
                x += 1
            elif direction < 0 and x > 0:
                room_direction = "w"
                x -= 1
            else:
                # If we hit a wall, turn north and reverse direction
                room_direction = "n"
                y += 1
                direction *= -1

            if room_count == 0:
                #move east
                self.n_to = None
                self.s_to = None
                self.e_to = room_count + 1
                self.w_to = None
            elif (room_count + 1) % 15 == 0 and direction < 0 and room_count >= 14:
                #move north
                self.n_to = room_count+1
                self.s_to = None
                self.e_to = room_count - 1
                self.w_to = None
            elif (room_count + 1) % 15 == 0 and direction > 0 and room_count >= 14:
                self.n_to = room_count+1
                self.s_to = None
                self.w_to = room_count - 1
                self.e_to = None
            elif room_count % 15 == 0 and direction < 0 and room_count >= 14:
                self.s_to = room_count - 1
                self.n_to = None
                self.w_to = room_count + 1
                self.e_to = None
            elif room_count % 15 == 0 and direction > 0 and room_count >= 14:
                self.s_to = room_count - 1
                self.n_to = None
                self.e_to = room_count + 1
                self.w_to = None
            elif direction > 0:
                self.w_to = room_count - 1
                self.e_to = room_count + 1
                self.n_to = None
                self.s_to = None
            else:
                self.w_to = room_count + 1
                self.e_to = room_count - 1
                self.n_to = None
                self.s_to = None

            # Create a room in the given direction using randomization
            room = Room(id=room_count, title=random.choice(roomTitles),
                        description=random.choice(descriptions), n_to=self.n_to,  s_to=self.s_to,  e_to=self.e_to, w_to=self.w_to, x=x, y= y)
           # print(room.n_to)
            room.save()
            self.list1.append(room)
            # Note that in Django, you'll need to save the room after you create it

            # Save the room in the World grid
            self.grid[y][x] = room

            # Connect the new room to the previous room
            # if previous_room is not None:
            #     previous_room.connect_rooms(room, room_direction)

            # Update iteration variables
            previous_room = room
            room_count += 1

w = World()
num_rooms = 100
width = 10
height = 10
w.generate_rooms(width, height, num_rooms)
# w.print_rooms()


# print(f"\n\nWorld\n  height: {height}\n  width: {width},\n  num_rooms: {num_rooms}\n")
