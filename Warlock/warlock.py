from Warlock import hand as h
from Spells import Spells

class warlock:

    def __init__(self,name):
        self.name = name
        self.left_hand = h.hand("Left Hand")
        self.right_hand = h.hand("Right Hand")