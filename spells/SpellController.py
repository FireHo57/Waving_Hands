from spells import SpellList as sp

class SpellController(object):

    def __init__(self):
        # at some point pass in the index but for now just make one
        self.index = dict()
        self.index["SD"] = sp.MagicMissile()
        self.index["cDPW"] = sp.DispelMagic()
        self.index["cSWWS"] = sp.SummonIceElemental()
        self.index["cWSSW"] = sp.SummonIceElemental()
        self.index["cw"] = sp.MagicMirror()
        self.index["DFFDD"] = sp.LightningBolt()
        self.index["DFPW"] = sp.CureHeavyWounds()
        self.index["P"] = sp.Shield()

        self.index["SD"] = sp.MagicMissile()

    def check_spells(self, sequence):
        for spell in self.index:
            if sequence[-len(spell):] == spell:
                return self.index[spell]



