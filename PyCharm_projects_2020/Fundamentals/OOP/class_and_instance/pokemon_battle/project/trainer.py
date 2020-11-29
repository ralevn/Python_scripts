from class_and_instance.pokemon_battle.project.pokemon import Pokemon

class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemon = []

    def add_pokemon(self, pokemon_inst):
        if pokemon_inst not in self.pokemon:
            self.pokemon.append(pokemon_inst)
            return f"Caught {pokemon_inst.pokemon_details()}"
        else:
            return f"This pokemon is already caught"

    def release_pokemon(self, pokemon_name):
        for p in self.pokemon:
            if p.name == pokemon_name:
                self.pokemon.remove(p)
                return f"You have released {pokemon_name}"
        else:
            return f"Pokemon is not caught"

    def trainer_data(self):
        data_1 = f"Pokemon Trainer {self.name}\n"
        data_2 = f"Pokemon count {len(self.pokemon)}\n"
        data_3 = ""
        for p in self.pokemon:
            data_3 += f"- {p.pokemon_details()}\n"
        return data_1 + data_2 + data_3


# first_pokemon = Pokemon("Pikachu", 90)
# print(first_pokemon.pokemon_details())
# trainer = Trainer("Ash")
# print(trainer.add_pokemon(first_pokemon))
# second_pokemon = Pokemon("Charizard", 110)
# third_pokemon = Pokemon("Idiot", 1000)
# print(trainer.add_pokemon(second_pokemon))
# print(trainer.release_pokemon("Pikachu"))
# print(trainer.add_pokemon(third_pokemon))
# print(trainer.trainer_data())