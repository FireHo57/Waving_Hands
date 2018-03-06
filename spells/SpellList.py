# this file is for defining spells. Start basic with magic missile

# Spells are all individual classes
# They have 2 functions, cast and global_effects
# Cast deals with caster-target interaction then returns global effects to the game to be resolved


# Helper function for printing spell stuff
def cast_text(caster, target, spell_name):
    print("{} casts {} at {}".format(caster.name, spell_name, target.name))


# Dispel magic removes all enchantments currently in play and acts as a shield for the target
# Monsters still get to attack on the turn but then die
# Any spells cast on the turn fail
class DispelMagic(object):

    def __init__(self):
        self.name = "Dispel Magic"

    def cast(self, target, caster):
        cast_text(target, caster, self.name)
        target.set_shield(True)
        return self.global_effect

    def global_effect(self, game):
        game.dispel_magic()


# Elementals of opposite types cancel each other out. They are also destroyed by elemental storms

# Summons an Ice elemental, this is treated as a global effect as elementals attack everyone
class SummonIceElemental(object):

    def __init__(self):
        self.name = "Summon Ice Elemental"

    def cast(self, target, caster):
        cast_text(target, caster, self.name)
        # no targeted effect
        return self.global_effect

    def global_effect(self, game):
        game.summon_ice_elemental()


# As summon Ice elemental except summons fire elemental
class SummonFireElemental(object):

    def __init__(self):
        self.name = "Summon Ice Elemental"

    def cast(self, target, caster):
        cast_text(target, caster, self.name)
        # no targeted effect
        return self.global_effect

    def global_effect(self, game):
        game.summon_fire_elemental()


class MagicMirror(object):

    def __init__(self):
        self.name = "Magic Mirror"

    def cast(self, target, caster):
        cast_text(target, caster, self.name)
        target.set_magic_mirror(True)
        # no global effect
        return None


class LightningBolt(object):

    def __init__(self):
        self.name = "Lightning Bolt"

    def cast(self, target, caster):
        cast_text(target, caster, self.name)
        target.take_damage(5)
        return None


class CureHeavyWounds(object):

    def __init__(self):
        self.name = "Cure Heavy Wounds"

    def cast(self, target, caster):
        cast_text(target, caster, self.name)
        target.heal(2)
        target.cure_disease()

        
class CureLightWound(object):
    
    def __init__(self):
        self.name = "Cure Light Wounds"
        
    def cast(self, target, caster):
        cast_text(target, caster, self.name)
        target.heal(1)
        
  
class Blindness(object):

class Amnesia(object):
    
class Confusion(object):

class Disease(object):
    
class DelayEffect(object):
    
class Poison(object):
    
class Paralyisis(object):
   
class SummonTroll(object):
    
class Fireball(object):

class Surrender(object):
 
class RemoveEnchantment(object):

class Invisibility(object):

class CharmMonster(object):
    
class CharmPerson(object):
    
class SummonOgre(object):
    
class FingerOfDeath(object):
    
class Haste(object):

class SummonGoblin(object):
    
class AntiSpell(object):
    
class Permanency(object):
    
class TimeStop(object):
    
class ResistCold(object):
    
class Fear(object):
    
class FireStorm(object):

class ClapOfLightning(object):
    
class CauseLightWounds(object):
    
class SummonGiant(object):
    
class CauseHeavyWounds(object):
    
class CounterSpell(object):
    
class IceStorm(object):
    
class ResistHeat(object):
    
class Protection(object):
    
class MagicMissile(object):

    def __init__(self):
        self.name = "Magic Missile"

    def cast(self, target, caster):
        cast_text(caster, target, self.name)
        target.take_damage(1)
        return None

    # no global effect

    
    
class Shield(object):

    def __init__(self):
        self.name = "Shield"

    def cast(self, target, caster):
        cast_text(caster, target, self.name)
        target.set_shield(True)
        return None
