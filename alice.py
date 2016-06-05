# coding: utf-8

import time
import os

#Intial Values
inventory = []
x_pos = 3
y_pos = 1
current_room = "ent"
jab = "alive"

#Movement Functions
def north():
	y_pos += 1
def east():
	x_pos += 1
def south():
	y_pos -= 1
def west():
	x_pos -= 1
def through():
	x_pos -= 1
def nope():
	print "You can't go that way, Alice!\n"
	
#Room Descriptions
ent_desc = "You stand at the entrance of the Jabberwok's abode. It's quite fancy for the home of a ravening beast. Two small side tables sprout lovely potted ferns, and the teal patterned wallpaper coordinates pleasingly with the white tile flooring.\n\n"
foy_desc = "The Jabberwok's foyer is massive and ornate. A collection of beanie babies in a crystal cabinet attracts your attention.\n\n"
clo_desc = "This large walk-in closet is piled high with dusty old newpapers and expired coupons. Looks like the Jabberwork is a bit of a hoarder.\n\n"
sit_desc = "This room is full of overstuffed chairs, each with the bottom cut out to accomodate the Jabberwok's tail. The fireplace is banked and lit, bathing the room in a warm, friendly glow.\n\n"
gal_desc = "Artful paintings adorn the walls of this well-kept gallery. One large oil painting draws your eye. It depicts a young woman in a blue dress brandishing a deadly-looking sword. She is deftly challenging a scaly, toothsome beast.\n\n"
hal_desc = "This hallway is covered in scorch marks and corn dog sticks. This part of the abode is not nearly as neat as the rest of the house. You must be getting close to the Jabberwok's den. A massive oak and iron-shod door stands at the end of the hallway.\n\n"
den_desc = "The center of the room is dominated by large cauldron, currently occupied by a weeping Mad Hatter. The Jabberwok is adding some finely diced onions to the pot, when the beast notices your trespass unto its domain. It pulls a chain suspended from the high ceiling, and a portculis slams down, blocking your exit!\n\n"

#Encounters
enc_start = "You stare at the empty seat at the head of the table. 'Not like him at all, missing his very own unbirthday,' the March Hare snorts.\n\n'He's late for a very important date!' the White Rabbit yells into his pocket watch.\n\nYou, of all people, know of the Mad Hatter's eccentricities; but this is pushing it, even for him. The tea grows cold as dark clouds occlude the sun, darkening the clearing. The Doormouse is getting very anxious. You make sure the pot of jam is well-stocked in case she needs calming down.\n\nA white feline grin materializes over the tea service, followed by the rest of the Cheshire Cat.\n\n'Our flamboyant friend has been snatched up by the Jabberwok. The foul beast has taken him back to its abode; to make a meal of him, I'm almost sorry to say,' the Cat purrs.\n\nYour friend is in grave danger!\n\nWithout a second thought, you bolt from the table and into the Tolgey Woods. You jump into the third mushroom ring, and find yourself at the front door of the Jabberwok's homestead. You fling open the front door and advance northward into the lair of the most fearsome beast in all of Wonderland.\n\n"
enc_cannot = "You cannot leave the Jabberwok's domain while your friend is in grave peril!\n\n"
enc_sword = "You look closely at the painting, and see that it's not sitting flush with the wall. You gingerly pull the bottom of the artwork away from the wall, and discover a gleaming sword hanging from two nails hammered into the plaster. You take the vorpal sword and return the painting to its place.\n\n"
enc_key = "You shuffle through the odd bits of paperwork, vastly increasing the amount of airborn dust in the closet. You are about to end your search, when you spy the glint of metal amongst the detritus piled in the corner. You open an old Penny Saver leaflet to find an ornate golden key, which you place into your front pocket.\n\n"
enc_nothing = "Your search reveals nothing.\n\n"
enc_locked = "This door is locked.\n\n"
enc_door = "You pull the golden key from your front pocket, and slide it into the keyhole on the massive door. It opens inward, and you journey through.\n\n"
enc_boss = "'Alice, my dear!' cries the Mad Hatter, 'Flee before you join me in this wretched monster's stew!' The Jabberwok explodes into motion, rearing up for a strike.\n\n"
enc_defeat = "With nothing to fight the Jabberwok, you remember the old adage 'Music can soothe the savage beast.' You being to sing an old song about a baby on a treetop in a lovely contralto. The Jabberwok stops instantly and starts swaying languidly to your song. As soon as the 'bough breaks,' however; the beast shakes and strikes! You feel terrible teeth piercing your throat!\n\n You awaken to Dinah, your kitten bumping into your right hand seeking its caresses. 'Alice! It's time to finish your history lesson!' your sister calls from the Solarium. You sigh, scoop up Dinah, and head back indoors."
enc_victory = "You bravely brandish the vorpal sword in the face of your adversary. The Jabberwok darts in for a killing blow, and the blade goes 'SNICKER SNACK!' The Jabberwok's grusome head tumbles from its gory shoulders.\n\n 'Hooray!' cries the Mad Hatter. You help your friend from the cauldron (luckily the water was just beginning to heat up), and walk with him outside back into the Tolgey Woods. Soon, you all are gathered at the table in the clearing.\n\n 'About time,' sighs the White Rabbit as the Doormouse pours the tea.\n\n"

#Room Class
class Room(object):
	def __init__ (self, name, desc, item, n_exit, e_exit, s_exit, w_exit, t_exit):
		self.name = name
		self.desc = desc
		self.item = item
		self.n_exit = n_exit
		self.e_exit = e_exit
		self.s_exit = s_exit
		self.w_exit = w_exit
		self.t_exit = t_exit
		
	#Entering the Room
	def room_enter(self):
		print (self.name) + ":\n" + (self.desc)
		
	#Searching the Room
	def room_search(self):
		if (self.item != "nothing"):
			if (current_room == "gal"):
				inventory.append("a vorpal sword")
				gal.item = "nothing"
				print(enc_sword)
			else:
				inventory.append("a golden key")
				clo.item = "nothing"
				print(enc_key)
		else:
			print(enc_nothing)
		
	#Listing Inventory, Room Exits and Search
	def exit_list(self):
		print "You have" + str(inventory)
		if (self.n_exit == "TRUE"):
			print "There is an exit to the (n)orth."
		if (self.e_exit == "TRUE"):
			print "There is an exit to the (e)ast."
		if (self.s_exit == "TRUE"):	
			print "There is an exit to the (s)outh."
		if (self.w_exit == "TRUE"):
			print "There is an exit to the (w)est."
		if (self.t_exit == "TRUE"):
			print "There is an exit (t)hrough the large door."
		print "You may also searc(h) this room."

ent = Room("The Entryway", ent_desc , "nothing", "TRUE", "FALSE", "FALSE", "FALSE", "FALSE")
foy = Room("The Foyer", foy_desc, "nothing", "TRUE", "TRUE", "TRUE", "TRUE", "FALSE")
clo = Room("The Closet", clo_desc, "key", "FALSE", "FALSE", "TRUE", "FALSE", "FALSE")
sit = Room("The Sitting Room", sit_desc, "nothing", "TRUE", "FALSE", "FALSE", "TRUE", "FALSE")
gal = Room("The Gallery", gal_desc, "sword", "FALSE", "FALSE", "TRUE", "FALSE", "FALSE")
hal = Room("The Hallway", hal_desc, "nothing", "FALSE", "TRUE", "FALSE", "FALSE", "TRUE")
den = Room("The Jabberwok's Den", den_desc, "nothing", "FALSE", "FALSE", "FALSE", "FALSE", "FALSE")

#The Start of the Adventure
print str(enc_start)

#The Quest to Save the Mad Hatter
while (jab == "alive"):
	#Determine Player Location
	if (x_pos == 3 and y_pos == 1):
		current_room = "ent"
	elif (x_pos == 3 and y_pos == 2):
		current_room = "foy"
	elif (x_pos == 3 and y_pos == 3):
		current_room = "clo"
	elif (x_pos == 4 and y_pos == 2):
		current_room = "sit"
	elif (x_pos == 4 and y_pos == 3):
		current_room = "gal"
	elif (x_pos == 2 and y_pos == 2):
		current_room = "hal"
	elif (x_pos == 1 and y_pos == 2):
		current_room = "den"
	else:
		print "You have somehow lost your way in the Tolgey Woods, despite being inside the Jabberwok's abode a moment ago.\n\n"
		break
	
	#Conditionals for Each Room
	#Ent
	if (current_room == "ent"):
		ent.room_enter()
		ent.exit_list()
		action = raw_input("What shall you do, Alice?")
		if (action == "h"):
			ent.room_search()
		elif (action == "n"):
			north()
		elif (action == "s"):
			print str(enc_cannot)
		else:
			nope()
	#Foy
	elif (current_room == "foy"):
		foy.room_enter()
		foy.exit_list()
		action = raw_input("What shall you do, Alice?")
		if (action == "h"):
			foy.room_search()
		elif (action == "n"):
			north()
		elif (action == "e"):
			east()
		elif (action == "s"):
			south()
		elif (action == "w"):
			west()
		else:
			nope()
	#Clo
	elif (current_room == "clo"):
		clo.room_enter()
		clo.exit_list()
		action = raw_input("What shall you do, Alice?\n\n")
		if (action == "h"):
			clo.room_search()
		elif (action == "s"):
			south()
		else:
			nope()
	#Sit
	elif (current_room == "sit"):
		sit.room_enter()
		sit.exit_list()
		action = raw_input("What shall you do, Alice?\n\n")
		if (action == "h"):
			sit.room_search()
		elif (action == "n"):
			north()
		elif (action == "e"):
			east()
		else:
			nope()
	#Gal
	elif (current_room == "gal"):
		gal.room_enter()
		gal.exit_list()
		action = raw_input("What shall you do, Alice?\n\n")
		if (action == "h"):
			gal.room_search()
		elif (action == "s"):
			south()
		else:
			nope()
	#Hal
	elif (current_room == "hal"):
		hal.room_enter()
		hal.exit_list()
		action = raw_input("What shall you do, Alice?\n\n")
		if (action == "h"):
			hal.room_search()
		elif (action == "e"):
			east()
		elif (action == "t" and "a golden key" in inventory == True):
			print str(enc_door)
			east()
		elif (action == "t" and "a golden key" in inventory == False):
			print str(enc_locked)
	#Den
	elif (current_room == "den"):
		den.room_enter()
		den.exit_list()
		print str(enc_boss)
		if ("a vorpal sword" in inventory == True):
			jab == "dead"
		else:
			print "Uh oh...\n\n"
		
#The Ending
if (jab == "dead"):
	print str(enc_victory)
else:
	print str(defeat)