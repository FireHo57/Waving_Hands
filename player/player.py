


class player:

    def __init__(self,name):
        self.health = 10
        self.name=name
        self.alive=True

    def take_damage(self,damage):
        self.health -= damage
        print ("{} is hit for {} damage!".format(self.name,damage))
        self.check_dead()

    def check_dead(self):
        if self.health <= 0:
            print("{} dies!".format(self.name))
            self.alive=False