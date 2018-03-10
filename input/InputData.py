
class HandData(object):


    def __init__(self, gesture, spell, target):
        self.gesture = gesture
        self. spell = spell
        self.target = target

    def get_gesture(self):
        return self.gesture

    def get_spell(self):
        return self.spell

    def get_target(self):
        return self.target


class InputData(object):

    def __init__( self, left_hand, right_hand ):
        self.left_hand = left_hand
        self.right_hand = right_hand

    def left_hand(self):
        return self.left_hand

    def right_hand(self):
        return  self.right_hand

