from django.contrib.auth.models import User
from adventure.models import Player, Room


Room.objects.all().delete()

r_outside = Room(title="Outside Cave Entrance",
               description="North of you, the cave mount beckons")

r_foyer = Room(title="Foyer", description="""Dim light filters in from the south. Dusty
passages run north and east.""")

r_overlook = Room(title="Grand Overlook", description="""A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""")

r_narrow = Room(title="Narrow Passage", description="""The narrow passage bends here from west
to north. The smell of gold permeates the air.""")

r_treasure = Room(title="Treasure Chamber", description="""You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""")

# new rooms 

r_solar = Room(title = "solar")



r_dungeon = Room(title = "The Dungeon", description = """You're in the dungeon, shh! move quietly so as not to alert the angry prisoners. You can move *** to return to previous room or *** to move to the turret """ )
r_turret = Room(title = "Turret", description = """""" )
r_kitchen = Room(title = "Kitchen", description = """You're currently in the kitchen, you can move *** to return to previous room or """ )
r_queenschamber = Room(title = "Queen's chamber", description = """If playing dress up is your thing, this might be the room for you. Unfortunately not the kind of treasure you want this time!""" )
r_dinninghall = Room(title = "Dinning hall", description = """Don't get distracted by the delicious feast, you can head *** to the dinning hall to see where it may lead or *** to return to the previous room""" )
r_rosegarden = Room(title = "Rose Garden", description = """Pick a nice rose for your loved one on your way but you may need the room for enough treasure, head *** to see where it leads you! """ )
r_lilygarden = Room(title = "Lily Garden", description = """You're currently in a different part of the garden, forge forward to see if the treasure is hidden somewhere in the garden or return to previous room""" )
r_tulipgarden = Room(title = "Tulip Garden", description = """Oops! More flowers. Unfortunatly only flowers here, you may only return to previous room!""" )
r_throneroom = Room(title = "Throne room", description = """You've reached the throne room, you could take a nap or return to previous room to continue your treasure hunt!""")
r_solar = Room = Room(title = "Solar", description = """This is where the royals have family time, unfortunately no treasures here. But you may choose to go north to enter ****, east to enter ****, west to enter *** or south to go back to ****""")


#solar family room
#throne room - kings room
#keep - banquet hall

r_outside.save()
r_foyer.save()
r_overlook.save()
r_narrow.save()
r_treasure.save()


#new rooms

r_dungeon.save()
r_kitchen.save()
r_turret.save()
r_queenschamber.save()
r_dinninghall.save()
r_rosegarden.save()
r_lilygarden.save()
r_tulipgarden.save()
r_throneroom.save()
r_solar.save()

# Link rooms together
r_outside.connectRooms(r_foyer, "n")
r_foyer.connectRooms(r_outside, "s")

r_foyer.connectRooms(r_overlook, "n")
r_overlook.connectRooms(r_foyer, "s")

r_foyer.connectRooms(r_narrow, "e")
r_narrow.connectRooms(r_foyer, "w")

r_narrow.connectRooms(r_treasure, "n")
r_treasure.connectRooms(r_narrow, "s")

players=Player.objects.all()
for p in players:
  p.currentRoom=r_outside.id
  p.save()

