from player import EffectsManager as ef
from Utils import SpellChain


allowed_gestures = "DPSFWdpsfwc>-"


class Player(SpellChain):

    # abstract method from SpellChain
    def trigger_spell(self, spell):
        spell.effect(self)

    def __init__(self, name):
        self.health = 10
        self.name = name
        self.alive = True
        self.effects = ef.EffectsManager(self)

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

    def turn(self):
        # resolve status effects
        self.effects.resolve_effects()
        # process other spells
        self.check_dead()

    def make_left_gesture(self, gesture):
        if allowed_gestures.find(gesture) != -1:
            self.left_hand += gesture

    def make_right_gesture(self, gesture):
        if allowed_gestures.find(gesture) != -1:
            self.right_hand += gesture
