from spells import SpellList as sp

class SpellController(object):

    def __init__(self):
        # at some point pass in the index but for now just make one
        self.index = dict()
        self.index["SD"] = sp.MagicMissile()

    def check_spells(self,sequence):
        return self.index.get(sequence,None)



