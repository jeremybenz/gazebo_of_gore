# coding: utf-8

import time

#Intial Values
inventory = []
x_pos = 3
y_pos = 1
current_room = "ent"
jab = "alive"

#Room Descriptions
ent_desc = "You stand at the entrance of the Jabberwok's abode. It's quite fancy for the home of a ravening beast. Two small side tables sprout lovely potted ferns, and the teal patterned wallpaper coordinates pleasingly with the white tile flooring."
foy_desc = "The Jabberwok's foyer is massive and ornate. A collection of beanie babies in a crystal cabinet attracts your attention."
clo_desc = "This large walk-in closet is piled high with dusty old newpapers and expired coupons. Looks like the Jabberwork is a bit of a hoarder."
sit_desc = "This room is full of overstuffed chairs, each with the bottom cut out to accomodate the Jabberwok's tail. The fireplace is banked and lit, bathing the room in a warm, friendly glow."
gal_desc = "Artful paintings adorn the walls of this well-kept gallery. One large oil painting draws your eye. It depicts a young woman in a blue dress brandishing a deadly-looking sword. She is deftly challenging a scaly, toothsome beast."
hal_desc = "This hallway is covered in scorch marks and corn dog sticks. This part of the abode is not nearly as neat as the rest of the house. You must be getting close to the Jabberwok's den. A massive oak and iron-shod door stands at the end of the hallway."
den_desc = "The center of the room is dominated by large cauldron, currently occupied by a weeping Mad Hatter. The Jabberwok is adding some finely diced onions to the pot, when the beast notices your trespass unto its domain. It pulls a chain suspended from the high ceiling, and a portculis slams down, blocking your exit!"

#Encounters
enc_sword = "You look closely at the painting, and see that it's not sitting flush with the wall. You gingerly pull the bottom of the artwork away from the wall, and discover a gleaming sword hanging from two nails hammered into the plaster. You take the vorpal sword and return the painting to its place."
enc_key = "You shuffle through the odd bits of paperwork, vastly increasing the amount of airborn dust in the closet. You are about to end your search, when you spy the glint of metal amongst the detritus piled in the corner. You open an old Penny Saver leaflet to find an ornate golden key, which you place into your front pocket."
enc_nothing = "Your search reveals nothing."
enc_locked = "This door is locked"
enc_door = "You pull the golden key from your front pocket, and slide it into the keyhole on the massive door. It opens inward, and you journey through."
enc_boss = "'Alice, my dear!' cries the Mad Hatter, 'Flee before you join me in this wretched monster's stew!' The Jabberwok explodes into motion, rearing up for a strike."

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
		
	#Listing the Room Exits and Search:
	def exit_list(self):
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
		print "You may also (s)earch this room."

ent = Room("The Entryway", ent_desc , "nothing", "TRUE", "FALSE", "FALSE", "FALSE", "FALSE")
foy = Room("The Foyer", foy_desc, "nothing", "TRUE", "TRUE", "TRUE", "TRUE", "FALSE")
clo = Room("The Closet", clo_desc, "key", "FALSE", "FALSE", "TRUE", "FALSE", "FALSE")
sit = Room("The Sitting Room", sit_desc, "nothing", "TRUE", "FALSE", "FALSE", "TRUE", "FALSE")
gal = Room("The Gallery", gal_desc, "sword", "FALSE", "FALSE", "TRUE", "FALSE", "FALSE")
hal = Room("The Hallway", hal_desc, "nothing", "FALSE", "TRUE", "FALSE", "FALSE", "TRUE")
den = Room("The Jabberwok's Den", den_desc, "nothing", "FALSE", "FALSE", "FALSE", "FALSE", "FALSE")

while (jab == "alive"):
	action = raw_input("What shall you do, Alice?")
	