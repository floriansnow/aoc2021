with open('day_06_input_1') as f:
    data = [int(num) for num in f.readlines()[0].split(',')]


def get_fishes_after(days, fishes):
    for day in range(days):
        fishes_new = empty_fishes.copy()
        for fish, num in fishes.items():
            if fish == 0:
                fishes_new[8] += num
                fishes_new[6] += num
            else:
                fishes_new[fish - 1] += num
        fishes = fishes_new
    return fishes


empty_fishes = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
fishes = empty_fishes.copy()
for fish in data:
    fishes[fish] += 1

fishes_80 = get_fishes_after(80, fishes)
fishes_256 = get_fishes_after(176, fishes_80)
print(sum(fishes_80.values()), sum(fishes_256.values()))