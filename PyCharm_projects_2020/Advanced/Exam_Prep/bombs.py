from collections import deque

bomb_effects = deque(int(n) for n in input().split(','))
bomb_casings = [int(n) for n in input().split(',')]

bomb_types = {40: 'Datura Bombs', 60: 'Cherry Bombs', 120: 'Smoke Decoy Bombs'}
bomb_pouch = {'Datura Bombs': 0, 'Cherry Bombs': 0, 'Smoke Decoy Bombs': 0}
job_done = False

def check_pouch(pouch):
    if all(x >= 3 for x in pouch.values()):
        return True


def print_leftover(list_b, list_name):
    if len(list_b) == 0:
        print(f'{list_name}: empty')
    else:
        print(f"{list_name}: {', '.join(str(n) for n in list_b)}")


def print_dict(dicti):
    for k, v in sorted(dicti.items()):
        print(f"{k}: {v}")


while bomb_casings and bomb_effects:
    b_effect = bomb_effects[0]
    b_case = bomb_casings[-1]
    sum_b = b_effect + b_case
    if sum_b in bomb_types:
        type_b = bomb_types[sum_b]
        bomb_pouch[type_b] += 1
        bomb_effects.popleft()
        bomb_casings.pop()
        if check_pouch(bomb_pouch):
            job_done = True
            break
    else:
        bomb_casings[-1] -= 5

if not job_done:
    print("You don't have enough materials to fill the bomb pouch.")
else:
    print("Bene! You have successfully filled the bomb pouch!")

print_leftover(bomb_effects, 'Bomb Effects')
print_leftover(bomb_casings, 'Bomb Casings')
print_dict(bomb_pouch)
