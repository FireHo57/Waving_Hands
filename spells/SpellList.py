# this file is for defining spells. Start basic with magic missile


def magic_missile(target, caster):
    print("{} caster.name casts magic missile at {}".format(caster.name, target.name))
    target.take_damage(1)
