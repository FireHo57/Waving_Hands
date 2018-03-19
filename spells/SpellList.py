# this file is for defining spells. Start basic with magic missile

# Spells are all individual classes
# They have 2 functions, cast and global_effects
# Cast deals with caster-target interaction then returns global effects to the game to be resolved

from Monsters import MonsterFactory as mf

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

        
# creates a magic mirror on the target which reflects spells cast against the target back on the caster
class MagicMirror(object):

    def __init__(self):
        self.name = "Magic Mirror"

    def cast(self, target, caster):
        cast_text(target, caster, self.name)
        target.set_magic_mirror(True)
        # no global effect
        return None

    
# fires a bolt of lightning at the target for 5 damage
class LightningBolt(object):

    def __init__(self):
        self.name = "Lightning Bolt"

    def cast(self, target, caster):
        cast_text(target, caster, self.name)
        target.take_damage(5)
        return None

    
# restores 3 points of health to the target, also cures disease
class CureHeavyWounds(object):

    def __init__(self):
        self.name = "Cure Heavy Wounds"

    def cast(self, target, caster):
        cast_text(target, caster, self.name)
        target.heal(2)
        target.cure_disease()
        return None

    
# as cure heavy wounds but restores 1 point of health      
class CureLightWound(object):
    
    def __init__(self):
        self.name = "Cure Light Wounds"
        
    def cast(self, target, caster):
        cast_text(target, caster, self.name)
        target.heal(1)
        return None
    
    
# renders the target blind (unable to see opponenets chains, or hit opponents with spells) for 3 turns  
class Blindness(object):

    def __init__(self):
        self.name = "Blindness"
        
    def cast(self, target, caster):
        cast_text(target, caster, self.name)
        target.set_blind(3)
        return None

    
# warlocks with amnesia are forced to repeat the last set of gestures they made. Lasts 1 round
class Amnesia(object):
    
    def __init__(self):
        self.name = "Amnesia"
        
    def cast(self, target, caster):
        cast_text(target, caster, self.name)
        target.set_amnesia(1)
        return None
    

# Confusion causes a warlock to make a randomly selected gesture with one hand
class Confusion(object):
    
    def __init__(self):
        self.name = "Confusion"

    def cast(self, target, caster):
        cast_text(target, caster, self.name)
        target.set_confusion(1)
        return None
    
    
# Maladroit
class Maladroit(object):
    
    
    def __init__(self):
        self.name = "Maladroit"
        
    def cast(self, target, caster):
        cast_text(target, caster, self.name)
        target.set_maladroit(1)
        return None
    
    
# inflicts disease upon the target. Unless dispelled byb Cure heavy wounds or dispel magic the warlock will die in
# six turns
class Disease(object):

    def __init__(self):
        self.name = "Disease"

    def cast(self, target, caster):
        cast_text(target, caster, self.name)
        target.set_diseased(True)
        return None


# Delay effect once cast can 'bank' a spell cast in the same turn or int the three subsequent turns following it's casting
# this banked spell can be cast at any time by the warlock
class DelayEffect(object):

    def __init__(self):
        self.name = "Delay Effect"

    def cast(self, target, caster):
        cast_text(target, caster, self.name)
        target.set_delay(3)
        return None


# As disease except the obly thing that cures poison is a dispel magic
class Poison(object):

    def __init__(self):
        self.name = "Posion"

    def cast(self, target, caster):
        cast_text(target, caster, self.name)
        target.set_poisoned(True)
        return None


# Paralysis forces the target warlock to repeat the previous gesture on one hand (as selected by caster)
class Paralyisis(object):

   def __init__(self):
        self.name = "Paralysis"

   def cast(self, target, caster):
       cast_text(target, caster, self.name)
       target.paralyse(caster.choose_hand())
       return None


# Summons a troll to serve the warlock the spell is targeted at
class SummonTroll(object):

    def __init__(self):
        self.name = "Summon Troll"

    def cast(self, target, caster):
        cast_text(target, caster, self.name)
        new_monster = mf.MonsterFactory.create_troll()
        new_monster.set_owner(target)
        return new_monster


# Throws a fireball at target. Has no effect if target is heat resistant
class Fireball(object):

    def __init__(self):
        self.name = "Fireball"

    def cast(self, target, caster):
        cast_text(target, caster, self.name)
        target.take_damage(5)
        return None


# Surrender the warlock concedes the match to the remaining warlocks
class Surrender(object):

    def __init__(self):
        self.name = "Surrender"

    def cast(self,caster,target):
        # surrender has no cast text
        caster.surrender()
        return self.global_effect

    def global_effect(self,game,caster):
        return game.surrender(caster)


# removes all enchantments currently in effect and acts as s shield for the target
class RemoveEnchantment(object):

    def __init__(self):
        self.name = "Remove Enchantment"

    def cast(self, caster, target):
        cast_text(caster, target, self.name)
        caster.set_shield()
        return self.global_effect

    def global_effect(self,game):
        game.remove_enchantment()


# Turns the target invisible for 3 rounds. During this time the caster is not a valid target for spells and
# their gestures are invisible to other warlocks
class Invisibility(object):

    def __init__(self):
        self.name = "Invisibility"

    def cast(self, caster, target):
        cast_text(caster, target, self.name )
        caster.set_invisible(3)
        return self.global_effect

    def global_effect(self, game, caster):
        game.set_invisible(game, caster, 3)


# Charms the target monster into obeying caster
class CharmMonster(object):

    def __init__(self):
        self.name = "Charm Monster"

    def cast(self, caster, target):
        cast_text(caster, target, self.name)
        try:
            target.set_owner(caster)
        except:
            # this is probably because the target is a warlock
            print("No effect")
            # will need to convert this to use output properly
            return None


# Target is charmed into making the wrong gesture (as selected by caster)
class CharmPerson(object):

    def __init__(self):
        self.name = "Charm Person"

    def cast(self, caster, target):
        cast_text(caster, target, self.name)
        try:
            target.set_charmed(caster, 3)
        except:
            print("No effect")
        return None


# Summons an ogre to serve the caster
class SummonOgre(object):

    def __init__(self):
        self.name = "Summon Ogre"

    def cast(self, caster, target):
        cast_text(target, caster, self.name)
        new_monster = mf.MonsterFactory.create_ogre()
        new_monster.set_owner(target)
        return new_monster

# any warlock or monster hit by this instantly dies
class FingerOfDeath(object):

    def __init__(self):
        self.name = "Finger of Death"

    def cast(self, caster, target):
        cast_text(target, caster, self.name)
        target.set_health(0)
        return None


#
class Haste(object):

# Summons a goblin to server the caster
class SummonGoblin(object):

    def __init__(self):
        self.name = "Summon Goblin"

    def cast(self, caster, target):
        cast_text(caster, target, self.name)
        new_monster = mf.MonsterFactory.create_goblin()
        new_monster.set_owner(target)
        return new_monster


# cancels any spells cast by the target on that turn and turns the targets gestures to '-'
class AntiSpell(object):

    def __init__(self):
        self.name = "Anti-spell"

    def cast(self, caster, target):
        cast_text(caster, target, self.name)
        target.antispell()
        return None
    
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
