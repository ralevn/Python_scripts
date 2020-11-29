from class_and_instance.guild_system.project.player import Player

class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players = []

    def assign_player(self, player):
        if player.guild == self.name:
            return f"Player {player.name} is already in the guild."
        elif player.guild != "Unaffiliated":
            return f"Player {player.name} is in another guild."
        elif player.guild == "Unaffiliated":
            self.players.append(player)
            player.guild = self.name
            return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name):
        for p in self.players:
            if p.name == player_name:
                self.players.remove(p)
                p.guild = "Unaffiliated"
                return f"Player {player_name} has been removed from the guild."
        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        data_1 = f"Guild: {self.name}\n"
        data_2 = ""
        for p in self.players:
            data_2 += f"{p.player_info()}\n"
        return data_1 + data_2

first_player = Player("George", 50, 100)
second_player = Player("Ivan", 80, 200)
shooters = Guild("UGT")
strategy = Guild("Goodies")
print(first_player.add_skill("Shield Break", 20))
print(first_player.add_skill("CS-25", 20))
print(second_player.add_skill("Civ IV", 45))
print(second_player.add_skill("Anno 1404", 45))
print(second_player.add_skill("Anno 1404", 45))
print(shooters.assign_player(first_player))
print(strategy.assign_player(second_player))
print(strategy.assign_player(first_player))
print(strategy.kick_player("Peter"))

print(strategy.guild_info())
print(shooters.guild_info())

print(first_player.player_info())
print(second_player.player_info())