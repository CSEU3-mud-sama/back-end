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
r_dungeon = Room(title = "The Dungeon", description = """You're in the dungeon, shh! move quietly so as not to alert the angry prisoners. You can move *** to return to previous room or *** to move to the turret """ )
r_turret = Room(title = "Turret", description = """Fancy a party? Sure, stay! but someone might grab the treasure before you. Go *** to head to the *** instead""" )
r_kitchen = Room(title = "Kitchen", description = """You're currently in the kitchen, you can move *** to return to previous room or """ )
r_queenschamber = Room(title = "Queen's chamber", description = """If playing dress up is your thing, this might be the room for you. Unfortunately not the kind of treasure you want this time!""" )
r_dinninghall = Room(title = "Dinning hall", description = """Don't get distracted by the delicious feast, you can head *** to the dinning hall to see where it may lead or *** to return to the previous room""" )
r_rosegarden = Room(title = "Rose Garden", description = """Pick a nice rose for your loved one on your way but you may need the room for enough treasure, head *** to see where it leads you! """ )
r_lilygarden = Room(title = "Lily Garden", description = """You're currently in a different part of the garden, forge forward to see if the treasure is hidden somewhere in the garden or return to previous room""" )
r_tulipgarden = Room(title = "Tulip Garden", description = """Oops! More flowers. Unfortunatly only flowers here, you may only return to previous room!""" )
r_throneroom = Room(title = "Throne room", description = """You've reached the throne room, you could take a nap or return to previous room to continue your treasure hunt!""")
r_solar = Room = Room(title = "Solar", description = """This is where the royals have family time, unfortunately no treasures here. But you may choose to go north to enter ****, east to enter ****, west to enter *** or south to go back to ****""")

r_chambers = Room(title = "Chambers", description = """Surely the treasure must be in one of the chambers but which one? Head north to go into the throne room west to go into the Queen's chamber, east to go into the wing that holds the royal heirs or south to return to the solar room """)
r_royalheirs = Room(title = "Royal Heirs", description = """Makes sense to keep all treasures in the same spot? let's see if any of the rooms in this wing hold the treasure you seek. Head north to go into the princess' chamber or south to head into the prince's chamber. You can also head west to return to the hallway of the chambers.""")
r_princessroom = Room(title = "Princess' room", description = "Boo! No luck here. You may head south to leave room ")
r_princeroom = Room(title = "Prince's room", description = "No luck here either.You may head south to leave room ")
r_landing = Room(title = "Landing", description =  """You have now entered the north wing of the castle, You may go north to the solar room, east to the kitchen or west to the banquet hall""")
r_banquethall = Room(title = "Banquet hall", description = """You are now in the banquet hall, join the party if you want but the treasure might go to someone who works more. Go east to return to the landing or north to go to the hallway""")
r_banquethallway = Room(title = "Banquest Hallway", description = """The hallway would be a silly place to hide some treasure wouldn't it? Go south to return to the banquet hall or east to go to the *** """)
r_partyroom = Room(title = "Party room", description = """More party! I know you just want some treasure, dont give up! you can go west to return to the hallway or east to return to head into the dinning room for some comfort food""")
r_garden = Room(title = 'Garden', description = """You are in a garden now, this would make a perfect location for a reception, unfortunately no treasure here. You may return to the party room on the South or go west to explore another hallway""")
r_gardenhallwayone = Room(title = "Garden Hallway One", description = """We know now that hallways have no treasures. No, not even behind an imaginary save behind the painting. Head east to return to the garden or south to explore more hallways, it might lead somewhere """)

r_gardenhallwaytwo = Room(title = "Garden Hallway Two", description = """It is a really long hallway, go south to keep going or north to return to previous hallway""")
r_gardenhallwaythree = Room(title = "Garden Hallway Three", description = """We are almost at the end of this hallway now! You've come so far, don'g give up but if you wish, you may go back to the previous hallway by going north or to the next room by heading east""")
r_courtyard = Room(title = """Welcome to the castle! Your quest begins you may head north, west or east to explore the castle or head south to exit the castle""")



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

r_chambers.save()
r_royalheirs.save()
r_princessroom.save()
r_princeroom.save()

r_landing.save()
r_banquethall.save()
r_banquethallway.save()
r_partyroom.save()
r_garden.save()
r_gardenhallwayone.save()
r_gardenhallwaytwo.save()
r_gardenhallwaythree.save()
r_courtyard.save()



# Link rooms together
r_outside.connectRooms(r_foyer, "n")
r_foyer.connectRooms(r_outside, "s")

r_foyer.connectRooms(r_overlook, "n")
r_overlook.connectRooms(r_foyer, "s")

r_foyer.connectRooms(r_narrow, "e")
r_narrow.connectRooms(r_foyer, "w")

r_narrow.connectRooms(r_treasure, "n")
r_treasure.connectRooms(r_narrow, "s")

#new rooms
r_solar.connectRooms(r_chambers, "n")
r_chambers.connectRooms(r_solar, "s")

r_chambers.connectRooms(r_queenschamber, "w")
r_queenschamber.connectRooms(r_chambers, "e")

r_chambers.connectRooms(r_throneroom, "n")
r_throneroom.connectRooms(r_chambers, "s")

r_chambers.connectRooms(r_royalheirs, "e")
r_royalheirs.connectRooms(r_chambers, "w")

r_royalheirs.connectRooms(r_princessroom, "n")
r_princessroom.connectRooms(r_royalheirs, "s")

r_royalheirs.connectRooms(r_princeroom, "s")
r_princeroom.connectRooms(r_royalheirs, "n")

r_landing.connectRooms(r_solar, "n")
r_solar.connectRooms(r_landing, "s")

r_banquethall.connectRooms(r_landing, "e")
r_landing.connectRooms(r_banquethall, "w")

r_banquethall.connectRooms(r_banquethallway, "n")
r_banquethallway.connectRooms(r_banquethall, "s")

r_partyroom.connectRooms(r_banquethallway, "w")
r_banquethallway(r_partyroom, "e")

r_partyroom.connectRooms(r_garden, "n")
r_garden.connectRooms(r_partyroom, "s")

r_gardenhallwayone.connectRooms(r_garden, "e")
r_garden.connectRooms(r_gardenhallwayone, "w")

r_gardenhallwayone.connectRooms(r_gardenhallwaytwo, "s")
r_gardenhallwaytwo.connectRooms(r_gardenhallwayone, "n")

r_gardenhallwaythree.connectRooms(r_gardenhallwaytwo, "n")
r_gardenhallwaytwo.connectRooms(r_gardenhallwaythree, "s")

r_gardenhallwaythree.connectRooms(r_courtyard, "e")
r_courtyard.connectRooms(r_gardenhallwaythree, "w")

r_courtyard.connectRooms(r_landing, "n")
r_landing.connectRooms(r_courtyard, "s")


players=Player.objects.all()
for p in players:
  p.currentRoom=r_outside.id
  p.save()

