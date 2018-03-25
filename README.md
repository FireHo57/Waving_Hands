# Waving_Hands
Simple implementation of the waving hands game. 

I'm eventually going to try writing a bot to play it which may or may not involve some sort of mahcine learning application.

Stuff to do:

add status effects to warlocks

add global effects to game

add monster adding to game

add turns to game (they're sort of implemented at the moment)

add a nice frontend for user input

As I'm going along it has started to feel like I need to rework the way spells happen. At the moment they are already assuming some knowledge of who/what they're targetting, i'd like to make it such that spells simply add one time (or more permanent) runnable effects to the player object. E.g. magic missile would be a one time effect of take 1 damage; the spell might look something like:

class MagicMissile:
...
...

def cast(self, target, caster):
  caster.add_effect(self)
  
def effect(self, target):
  target.take_damage(1)
  del self.value
  


There's plenty more but that will do for now.
