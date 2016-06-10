# coding: utf-8

import time
import console
	
class Room():
	def __init__(self, name, description, x_pos, y_pos, n_exit, e_exit, s_exit, w_exit):
		self.name = name
		self.description = description
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.n_exit = n_exit
		self.e_exit = e_exit
		self.s_exit = s_exit
		self.w_exit = w_exit
		
class Hero(object):
	def __init__(self, name, moving, x_pos, y_pos):
		self.name = name
		self.moving = moving
		self.x_pos = x_pos
		self.y_pos = y_pos
	
hero = Hero("Hero", "moving", 0, 0)

ent = Room("Entrance", "This is the entrance to the tower.", 0, 0, False, False, True, False)

hal = Room("Hallway", "You are in a hallway.", 0, 1, True, False, True, False)

gar = Room("Garden", "A lush garden captivates your senses.", 0, 2, True, True, False, False)

fou = Room("Fountain", "A burbling fountain dominates the center of this room.", 1, 0, False, False, True, False)

tin = Room("T-Intersection", "Options for movement abound.", 1, 1, True, True, True, False)

lib = Room("Library", "Books float from shelf to shelf in scandalous configurations.", 1, 2, True, False, False, True)

sta = Room("Stairway", "A decrepit stone stairway ascends to the next level. It looks risky. You decide to pass.", 2, 0, False, False, True, False)

rec = Room("Reception Room", "This room is obviously designed to receive prestigious visitors. You feel very fancy.", 2, 1, True, False, True, True)

gal = Room("Gallery", "Numerous paintings adorn the walls. You take a moment to thoughtfully consider each specimen.", 2, 2, True, False, False, False)

n_exit = ("  #  \n  |  ")
no_n_exit = ("    \n     ")
e_exit = ("  @-#")
w_exit = ("#-@  ")
ew_exit = ("#-a-#")
no_e_w_exit = ("  @  ")
s_exit = ("  |  \n  #  ")
no_s_exit = ("    \n     ")
nope = ("You can't go that way "+ hero.name + "!\n")

hero.name = raw_input("You bravely enter the first floor of the tower. What is your name, hero?")
console.clear()
while (hero.moving == "moving"):
	if (hero.x_pos == 0 and hero.y_pos == 0):
		Room = ent
	elif (hero.x_pos == 1 and hero.y_pos == 0):
		Room = fou
	elif (hero.x_pos == 2 and hero.y_pos == 0):
		Room = sta
	elif (hero.x_pos == 0 and hero.y_pos == 1):
		Room = hal
	elif (hero.x_pos == 1 and hero.y_pos == 1):
		Room = tin
	elif (hero.x_pos == 2 and hero.y_pos == 1):
		Room = rec
	elif (hero.x_pos == 0 and hero.y_pos == 2):
		Room = gar
	elif (hero.x_pos == 1 and hero.y_pos == 2):
		Room = lib
	else:
		Room = gal
	print(Room.name) + ":\n"
	print(Room.description) + "\n"
	if (Room.n_exit == True):
		print(n_exit)
	else:
		print(no_n_exit)
	if (Room.e_exit and Room.w_exit == True):
		print(ew_exit)
	elif (Room.e_exit == True):
		print(e_exit)
	elif (Room.w_exit == True):
		print(w_exit)
	else:
		print(no_e_w_exit)
	if (Room.s_exit == True):
		print(s_exit) + "\n"
	else:
		print(no_s_exit) + "\n"
	action = raw_input("Which way will you go, " + hero.name + "?\n (n)orth, (s)outh, (east), (w)est, or e(x)it.")
	console.clear()
	if (action == "n" and Room.n_exit == True):
		hero.y_pos -= 1
	elif (action == "e" and Room.e_exit == True):
		hero.x_pos += 1
	elif (action == "s" and Room.s_exit == True):
		hero.y_pos += 1
	elif (action == "w" and Room.w_exit == True):
		hero.x_pos -= 1
	elif (action == "x"):
		break
	else:
		print(nope)

console.clear()
print("Thanks for walking around the first floor of the tower, " + hero.name + "!")	