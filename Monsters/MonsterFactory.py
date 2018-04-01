from enum import Enum, auto


class Elemental(Enum):
    FIRE = auto()
    ICE = auto()


class Monster(object):

    def __init__(self, name, health, damage, elemental=None):
        self.name = name
        self.health = health
        self. damage = damage
        self.alive = True
        self.target = None
        self.owner = None
        if elemental:
            self.elemental = elemental

    def set_target(self, target, setter):
        # check that the warlock owning the creature is the one giving it the orders
        if setter is self.owner:
            self.target = target

    def do_damage(self, damage):
        self.target.take_damage(damage)

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.alive = False

    def set_owner(self, owner):
        self.owner = owner

    def kill(self):
        self.alive = False

    def die(self):
        print("{} dies!".format(self.name))


class MonsterFactory(object):

    @staticmethod
    def create_goblin():
        return Monster("Malodorous Goblin", 1, 1)

    @staticmethod
    def create_ogre():
        return Monster("Ugly Ogre", 2, 2)

    @staticmethod
    def create_troll():
        return Monster("Cantankerous Troll", 3, 3)

    @staticmethod
    def create_giant():
        return Monster("Deafening Giant", 4, 4)

    @staticmethod
    def create_ice_elemental():
        return Monster("Ice Elemental", 5, 3, Elemental.ICE)

    @staticmethod
    def create_fire_elemental():
        return Monster("Fire Elemental", 5, 3, Elemental.FIRE)
