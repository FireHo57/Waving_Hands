from player import player as p


class Game:

    def __init__(self):
        self.player_list=dict()

    def add_player(self,player):
        self.player_list[player.name]=player
        print("Player {} joined the arena".format(player.name))

    def do_damage_to_player(self,player_name,damage):
        target = self.player_list.get(player_name,0)
        if target == 0:
            print("Damage Flies off into the distance!")
        else:
            target.take_damage(damage)

    def get_player(self,name):
        return self.player_list.get(name,None)


if __name__ == "__main__":
    new_game = Game()
    new_game.add_player(p.Player("player1"))
    new_game.do_damage_to_player("null player", 5)
    new_game.do_damage_to_player("player1", 5)
    player = new_game.get_player("player1")
    if player is not None:
        player.set_shield(True)
    new_game.do_damage_to_player("player1", 5)
