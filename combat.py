# coding: utf-8

from random import randint
import time

#Initial Stats
hero_hp = 18
gumdrops = 3
monster_hp = 25

#Greeting
print "'Save me, my valiant champion!', cries Princess Sweetums. Gumdrop tears cascade from her perfect marzipan cheeks. She struggles fetchingly against candy cane chains binding her wrists to the chocolate throne."

time.sleep(10)

print " "

print "You are a warrior, fashioned out of popsicle sticks, fondant, and grim determination. From across the arena you are greeted by the howls of your opponent: a savage polar gummy bear, bristling with hostility. You brandish your toothpick and grimly wade into battle for your one true love."

time.sleep(15)

#Combat!
while (monster_hp > 0):
	if (hero_hp > 0):
		print " "
		action = raw_input("What will you do, champion? " + "Your popsicle frame has " + str(hero_hp) + " hit points remaining. You have " + str(gumdrops) + " gumdrops in your fruit leather bandolier. Your foe has " + str(monster_hp) + " hit points. You can (s)lash, (l)unge, or (e)at a gumdrop.")
		if action == "s":
			monster_damage = randint(2,4)
			monster_hp = monster_hp - monster_damage
			print " "
			print "You slash the gummy monstrosity for " + str(monster_damage) + " points of damage! "
			time.sleep(3)
			if (monster_hp > 0):
				hero_damage = randint(3,6)
				hero_hp = hero_hp - hero_damage
				print " "
				print "The gummy artic fiend swipes a squishy paw across your ribs for " + str(hero_damage) + " points of popsicle stick trauma!"
				time.sleep(3)
				continue
			else:
				break
		elif action == "l":
			monster_damage = randint(1,8)
			monster_hp = monster_hp - monster_damage
			print " "
			print "You lunge at the polar grizzly with all your balsa wood heart! You hit for " + str(monster_damage) + " points of damage!"
			time.sleep(3)
			if (monster_hp > 0):
				print " "
				hero_damage = randint(5,8)
				hero_hp = hero_hp - hero_damage
				print "After your lunge, the foul pineapple-smelling beast bear-hugs you for " + str(hero_damage) + " stick-cracking points of damage!"
				time.sleep(3)
				continue
			else:
				break
		elif action == "e":
			if gumdrops > 0:
				hero_heal = randint(6,10)
				hero_hp = hero_hp + hero_heal
				gumdrops = gumdrops - 1
				print " "
				print "The gumdrop slides down your gullet. Your fondant hardens and your popsicles shed splinters. You gain " + str(hero_heal) + " hit points."
				time.sleep(3)
				print " "
				print "The savage polar gummy bear sniffs about, confused."
				time.sleep(3)
				continue
			else:
				print " "
				print "You ram your hand into the bandolier, but only find buttercup wrappers."
				time.sleep(3)
				hero_damage = randint(1,3)
				hero_hp = hero_hp - hero_damage
				print " "
				print "The ferocious bear sighs and looks bored. He gnaws on your leg for " + str(hero_damage) + " points of damage."
				time.sleep(3)
				continue
		else:
			print " "
			print "What is this nonsense? Please type either s, l, or e!"
			time.sleep(3)
			continue
	else:
		break	
		
#Victory or Defeat!
time.sleep(3)
if hero_hp >= monster_hp:
	print " "
	print "The polar gummy bear huffs, grumbles, and then topples over. With one stroke of your mighty toothpick, you sever the candy cane chains fettering the beautiful Princess Sweetums. 'You are my one, true champion' she sighs. You sweep her up off her immaculate chiclet feet, carrying her from the arena to the cheers of the gathered candyfolk thronging the plaza below."
	time.sleep(20)
	print " "
	print "King Crackle places a crown upon your head, and Pope Popsicle VI unites you and Princess Sweetums in holy matrimony before the entire kingdom."
	time.sleep(8)
	print " "
	print "You perish of diabetes two months later."
	time.sleep(3)
	print " "
	print "Well done, Champion!"
	
else:
	print " "
	print "Your balsa wood body shatters against the hard peanut brittle floor of the arena. 'They're always too fragile,' Princess Sweetums pouts. 'Daddy! Send another one before I become cross!'"
	time.sleep(5)
	print " "
	print "Your best was not good enough, champion."