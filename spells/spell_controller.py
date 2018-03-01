from spells import SpellList as sp

class Spell:

    def __init__(self,name,effect):
        self.name=name
        self.effect=effect


def damage_effect(target,damage=5):
    some_effect()


class SpellController:

    def __init__(self):
        # at some point pass in the index but for now just make one
        self.index["magic Missile"] = Spell("Magic Missile", )

    #def resolve_effect(self,effect):
