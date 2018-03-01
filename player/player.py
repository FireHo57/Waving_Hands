class Player:

    def __init__(self, name):
        self.health = 10
        self.name = name
        self.alive = True
        self.shielded = False

    def take_damage(self, damage):

        if self.shielded:
            print("Damage bounces of {}'s shield!".format(self.name))
        else:
            self.health -= damage
            print (("{} is hit for {} damage!".format(self.name, damage)))
            self.check_dead()

    def check_dead(self):
        if self.health <= 0:
            print("{} dies!".format(self.name))
            self.alive = False

    def set_shield(self, shield_on):
        self.shielded = shield_on
