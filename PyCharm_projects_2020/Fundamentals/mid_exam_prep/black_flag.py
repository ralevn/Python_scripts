days = int(input())
per_day = int(input())
expected = float(input())

plunder = 0.0


for d in range(1, days + 1):
    plunder += per_day
    if d % 3 == 0:
        plunder += 0.5 * per_day
    if d % 5 == 0:
        plunder *= 0.7

if plunder >= expected:
    print(f'Ahoy! {plunder:.2f} plunder gained.')
else:
    print(f'Collected only {(plunder / expected) * 100:.2f}% of the plunder.')
