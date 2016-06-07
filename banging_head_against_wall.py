# Boom! Here is where I discovered that either Python or Pythonista DOES NOT LIKE a class attribute named 'def'. I have spent about 2 hours spinning my wheels with this issue. At least I found the answer. In hindsight, I see that (def)ining a function and having an attribute with the name 'def' is the issue here; but I don't see why it matters. Both are two different things... Well, at least I learned something NOT to do while coding in Python...
class Test2(self, def):
	def __init__ (self, def):
		self.def = def

# I thought there was a limit of 10 attributes per class (including 'self'), in either Python, or specifically Pythonista. I did a lot more googling, but could not find any reference to the maximum number of attributes in a class. I then decided to write a whole new class with different values. The interpreter had no problem with this.
class Test(object):
	def __init__ (self, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13):
		self.x1 = x1
		self.x2 = x2
		self.x3 = x3
		self.x4 = x4
		self.x5 = x5
		self.x6 = x6
		self.x7 = x7
		self.x8 = x8
		self.x9 = x9
		self.x10 = x10
		self.x11 = x11
		self.x12 = x12
		self.x13 = x13

# After a long time researching classes, and traceback errors, I decided to replicate the code below and run the interpeter after each attribute entry. It stopped here at 'atk' (it threw the traceback error when I tried to add the 'def' attribute)
class Hero(object):
	def __init__(self, name, lev, x_pos, y_pos, hp, max_hp, mp, max_mp, atk):
		self.name = name
		self.lev = lev
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.hp = hp
		self.max_hp = max_hp
		self.mp = mp
		self.max_mp = max_mp
		self.atk = atk

#I couldn't figure out why this was throwing a traceback error.. I was using the attribute name 'def' for player defense to allow for easier keystrokes when coding, along with the convention of the other attributes. Later I just changed it to 'defense' (you'll see why)		
class Player(object):
	def __init__ (self, name, lev, x_pos, y_pos, hp, max_hp, mp, max_mp, atk, defense, fla, amu, inv):
		self.name = name
		self.lev = lev
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.hp = hp
		self.max_hp = max_hp
		self.mp = mp
		self.max_mp = max_mp
		self.atk = atk
		self.defense = defense
		self.fla = fla
		self.amu = amu
		self.inv = inv
