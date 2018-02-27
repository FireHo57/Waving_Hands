from archive.Warlock import hand as h

class warlock:

    def __init__(self,name,health=15):
        self.name = name
        self.left_hand = h.hand("Left Hand")
        self.right_hand = h.hand("Right Hand")
        self.health = health

    def make_left_hand_gesture(self,gesture):
        self.left_hand.make_gesture(gesture)

    def make_right_hand_gesture(self,gesture):
        self.right_hand.make_gesture(gesture)