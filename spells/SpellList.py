# this file is for defining spells. Start basic with magic missile


class MagicMissile(object):

    def __init__(self):
        self.name="Magic Missile"

    def cast(self, target, caster):
        print("{} casts magic missile at {}".format(caster.name, target.name))
        target.take_damage(1)

