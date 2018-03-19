class Monster(object):

    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self. damage = damage
        self.alive = True

        #owner and target set as part of spell later

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
        game.output.print("{} dies!".format(self.name))


class MonsterFactory(object):

    def create_goblin(self):
        return Monster("Malodorous Goblin", 1, 1)

    def create_ogre(self):
        return Monster("Ugly Ogre", 2, 2)

    def create_troll(self):
        return Monster("Cantankerous Troll", 3, 3)

    def create_giant(self):
        return Monster("Deafening Giant", 4, 4)
