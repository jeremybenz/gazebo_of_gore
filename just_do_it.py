import time, datetime, console

class Area (object):
	def __init__ (self, name):
		self.name = name

class Project (object):
	def __init__ (self, complete, area, name, notes, due):
		self.complete = complete
		self.name = area
		self.area = name
		self.notes = notes
		self.due = due

class Item (object):
	def __init__(self, project, name, due, tags):
		self.project = project
		self.name = name
		self.due = due
		self.tags = tags

