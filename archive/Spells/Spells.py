
allowed_gestures = "->SDFWPsdfwpc"

class Spell:

    def __init__(self,target,caster,effect):
        self.target=target
        self.caster=caster
        self.effect=effect

    def cast(self):
        self.effect(self.target,self.caster)

# an effect is just something that happens to a target
# three types of effect. Damage, Summon and Enchantment
# damage happens then goes away
# Summon exists until the creature summoned dies
# Enchantments last a set number of turns, or until dispelled
class effect:

    def doDamage(self,damage,target):
        target.takeDamage(damage)

    def summonMonster(self,monster_type,owner):
        new_monster=game.spawn(monster_type)
        new_monster.set_owner(owner)

    def applyEffect(self,effect,target,duration):
        target.addEffect(effect,duration)




class Spell_List:


    def __init__(self):
        self.Spells = dict()
        self.Spells["Dispel Magic"] = Spell("Dispel Magic", "cDPW", )
        self.Spells["Summon Ice Elemental"] = Spell("Summon Ice Elemental", "cSWWS")
        self.Spells["Summon Ice Elemental"] = Spell("Summon Ice Elemental", "cSWWS")




#cw
#Magic
#Mirror
#DFFDD
#Lightning
#Bolt
#DFPW
#Cure
#Heavy
#Wounds
#DFW
#Cure
#Light
#Wounds
#DFWFd
#Blindness
#DPP
#Amnesia
#DSF
#Confusion / Maladroitness
#DSFFFc
#Disease
#DWFFd
#Blindness
#DWSSSP
#Delay
#Effect
#DWWFWD
#Poison
#FFF
#Paralysis
#FPSFW
#Summon
#Troll
#FSSDD
#Fireball
#P
#Shield
#p    ! Surrender
#PDWP
#Remove
#Enchantment
#PPws
#Invisibility
#PSDD
#Charm
#Monster

#PSDF
#Charm
#Person
#PSFW
#Summon
#Ogre
#PWPFSSSD
#Finger
#of
#Death
#PWPWWc
#Haste
#SD
#Magic
#Missile
#SFW
#Summon
#Goblin
#SPFP
#Anti - spell
#SPFPSDW
#Permanency
#SPPc
#Time
#Stop
#SPPFD
#Time
#Stop
#SSFP
#Resist
#Cold
#SWD
#Fear(No
#CFDS)
#SWWc
#Fire
#Storm
#WDDc + Clap
#of
#Lightning
#WFP
#Cause
#Light
#Wounds
#WFPSFW
#Summon
#Giant
#WPFD
#Cause
#Heavy
#Wounds
#WPP
#Counter
#Spell
#WSSc
#Ice
#Storm
#WWFP
#Resist
#Heat
#WWP
#Protection
#WWS
#Counter
#Spell