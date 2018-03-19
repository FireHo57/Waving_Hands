# Class to track status effects on players
# statuses are (in no particular order):
#  Confusion/Maladroit
#  Amnesia
#  Paralysis
#  Magic Mirror
#  Blindness
#  Invisibility
#  Charmed
#

from enum import Flag, auto


class Statuses(Flag):
    CONFUSION = auto()
    AMNESIA = auto()
    PARALYSIS = auto()
    MAGIC_MIRROR = auto()
    BLINDNESS = auto()
    INVISIBILITY = auto()
    CHARMED = auto()
    DISEASED = auto()
    POISONED = auto()
    NO_EFFECTS = auto()
    ANTI_SPELL = auto()
    SURRENDERED = auto()

allowed_gestures = "DPSFWdpsfwc>-"


class Player:

    def __init__(self, name):
        self.health = 10
        self.name = name
        self.alive = True
        self.shielded = False
        self.status = Statuses(Statuses.NO_EFFECTS)
        self.turns_diseased = 0
        self.turns_poisoned = 0
        self.turns_invisible = 0
        self.turns_blind = 0

        self.left_hand = ""
        self.right_hand = ""

    def take_damage(self, damage):

        if self.shielded:
            print("Damage bounces of {}'s shield!".format(self.name))
        else:
            self.health -= damage
            print("{} is hit for {} damage!".format(self.name, damage))
            self.check_dead()

    def check_dead(self):
        if self.health <= 0:
            print("{} dies!".format(self.name))
            self.alive = False

    def set_shield(self, shield_on):
        self.shielded = shield_on

    def heal(self, heal_sum):
        self.health += heal_sum

    def set_invisible(self, turns):
        self.turns_invisible = turns

    def cure_disease(self):
        self.status -= Statuses.DISEASED

    def surrender(self):
        self.status += Statuses.SURRENDERED

    def anti_spell(self):
        self.status+=Statuses.ANTI_SPELL

    def turn(self):
        # reset status effects
        self.status = Statuses.NO_EFFECTS

        # resolve ongoing status effects
        self.turns_invisible-=1
        self.turns_blind-=1
        self.turns_poisoned+=1
        self.turns_diseased+=1

        if self.turns_invisible > 0:
            self.status += Statuses.INVISIBILITY
        if self.turns_blind > 0:
            self.status += Statuses.BLINDNESS


    def make_left_gesture(self, gesture):
        if allowed_gestures.find(gesture) != -1:
            self.left_hand += gesture

    def make_right_gesture(self, gesture):
        if allowed_gestures.find(gesture) != -1:
            self.right_hand += gesture
