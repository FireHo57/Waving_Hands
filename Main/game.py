from player import player as p
from spells import SpellController as Sc
from enum import *


class GlobalEffects(Flag):
    ICE_ELEMENTAL = auto()
    FIRE_ELEMENTAL = auto()
    FIRE_STORM = auto()
    ICE_STORM = auto()
    DISPEL_MAGIC = auto()
    NO_FLAGS = auto()


class Game:

    def __init__(self, spell_controller):
        self.player_list = dict()
        self.spell_controller = spell_controller
        self.effects = GlobalEffects.NO_FLAGS

    def add_player(self, player):
        self.player_list[player.name] = player
        print("Player {} joined the arena".format(player.name))

    def do_damage_to_player(self, player_name, damage):
        target = self.player_list.get(player_name, 0)
        if target == 0:
            print("Damage Flies off into the distance!")
        else:
            target.take_damage(damage)

    def get_player(self, name):
        return self.player_list.get(name, None)

    # gets the player to update
    def get_player_gestures(self, name):
        left_hand = input("{}'s left hand: ".format(name))
        right_hand = input("{}'s right hand: ".format(name))
        player = self.player_list[name]
        player.make_left_gesture(left_hand)
        player.make_right_gesture(right_hand)
        print("{}\n{}".format(player.left_hand, player.right_hand))

    def resolve_spells(self, player):
        spell_left = self.spell_controller.check_spells(player.left_hand)
        spell_right = self.spell_controller.check_spells(player.right_hand)

        # get a target
        target_string = ""
        for i in self.player_list:
            target_string += i + ","
        print("Available Targets: {}".format(target_string))

        if spell_left is not None:
            target = input("Select Target for {}: ".format(spell_left.name))
            spell_left.cast(self.player_list[target], player)
        if spell_right is not None:
            target = input("Select Target for {}: ".format(spell_right.name))
            spell_right.cast(self.player_list[target], player)

    def resolve_global_effects(self):
        if self.effects == GlobalEffects.FIRE_STORM:
            print("Oh no everything is on fire")

    def next_turn(self):

        # get players to make turns
        for name in self.player_list:
            self.get_player_gestures(name)
            self.resolve_spells(name)

        self.resolve_global_effects()

if __name__ == "__main__":
    spell_controller = Sc.SpellController()
    spell = spell_controller.check_spells("SD")

    new_game = Game(spell_controller)
    new_game.add_player(p.Player("player1"))
    new_game.add_player(p.Player("player2"))

    new_game.next_turn()
