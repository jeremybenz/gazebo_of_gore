# coding: utf-8

import time
import random
import console

#top = ("+++++++\n")
#row1 = ("+  #  +\n")
#row2 = ("+  |  +\n")
#row3 = ("+#-@-#+\n")
#row4 = ("+  |  +\n")
#row5 = ("+  #  +\n")
#bot = ("+++++++\n")
#print(top + row1 + row2 + row3 + row4 + row5 + bot)

# Name, Level, X position, Y Position, Hit Points, Max Hit Points, Magic Points, Max Magic Points, Evasions, Defense, Attack, Flask Fill Level, Amulet Charge, Spells, Equipped Weapon, Equipped Armor, Equipped Shield, Cloak, Inventory
class Player(object):
	def __init__(self, name, lv, x, y, hp, mhp, mp, mmp, ev, de, at, fl, am, sp, we, ar, sh, cl, inv):
		self.name = name
		self.lv = lv
		self.x = x
		self.y = y
		self.hp = hp
		self.mhp = mhp
		self.mp = mp
		self.mmp = mmp
		self.ev = ev
		self.de = de
		self.at = at
		self.fl = fl
		self.am = am
		self.we = we
		self.ar = ar
		self.sh = sh
		self.cl = cl
		self.inv = inv

# Name, Monster Descrition, Hit Points, Max Hit Points, Magic Points, Max Magic Points, Spells
class Monster(object):
	def __init__(self, name, desc, hp, mhp, mp, mmp, ev, de, at, sp):
		self.name = name
		self.desc = desc
		self.hp = hp
		self.mhp = mhp
		self.mp = mp
		self.mmp = mmp
		self.ev = ev
		self.de = de
		self.at = at
		self.sp = sp
		self.it = it

# Name, Item Description, Item Type
class Item(object):
	def __init__(self, name, desc, type)
		self.name = name
		self.desc = desc
		self.type = type

#	Equipped?, Attack Bonus, Defense Bonus
class Weapon(Item):
	def __init__(self, eq, atb, deb):
		self.eq = eq
		self.atb = atb
		self.deb = deb
		
class Armor(Item):
	def __init__(self, eq, deb, hpb, ):
		self.eq = eq
		self.deb = deb
		self.hpb = hpb
		
class Shield(Item):
	def __init__(self, eq)
		
class 

# Name, Level, X position, Y position, Monster Presence, Chest, Barrel, Crystal, Shrine
class Room(object):
	def __init__(self, name, lv, x, y, mo, ch, ga, cr, sh)