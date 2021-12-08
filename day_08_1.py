import itertools

def get_decoded_patterns(line):
    for a, b, c, d, e, f, g in itertools.permutations(['a', 'b', 'c', 'd', 'e', 'f', 'g']):
        irregular_patterns = {
            frozenset({a, b, c, e, f, g}): 0,
            frozenset({c, f}): 1,
            frozenset({a, c, d, e, g}): 2,
            frozenset({a, c, d, f, g}): 3,
            frozenset({b, c, d, f}): 4,
            frozenset({a, b, d, f, g}): 5,
            frozenset({a, b, d, e, f, g}): 6,
            frozenset({a, c, f}): 7,
            frozenset({a, b, c, d, e, f, g}): 8,
            frozenset({a, b, c, d, f, g}): 9
        }
        for pattern in line['signal_patterns']:
            if pattern not in irregular_patterns:
                break
        else:
            return irregular_patterns


with open("day_08_input_1") as f:
    raw_data = f.readlines()
    data = []
    for line in raw_data:
        signal_patterns, output_value = line.split('|')
        signal_patterns = list(map(frozenset, signal_patterns.split()))
        output_value = list(map(frozenset, output_value.split()))
        data.append({'signal_patterns': signal_patterns, 'output_value': output_value})

regular_patterns = {
    frozenset({'a', 'b', 'c', 'e', 'f', 'g'}): 0,
    frozenset({'c', 'f'}): 1,
    frozenset({'a', 'c', 'd', 'e', 'g'}): 2,
    frozenset({'a', 'c', 'd', 'f', 'g'}): 3,
    frozenset({'b', 'c', 'd', 'f'}): 4,
    frozenset({'a', 'b', 'd', 'f', 'g'}): 5,
    frozenset({'a', 'b', 'd', 'e', 'f', 'g'}): 6,
    frozenset({'a', 'c', 'f'}): 7,
    frozenset({'a', 'b', 'c', 'd', 'e', 'f', 'g'}): 8,
    frozenset({'a', 'b', 'c', 'd', 'f', 'g'}): 9
}

output_values = []
count = 0
sum = 0
for line in data:
    irregular_patterns = get_decoded_patterns(line)
    count += len([irregular_patterns[pattern] for pattern in line ['output_value'] if irregular_patterns[pattern] in (1, 4, 7, 8)])
    sum += int(''.join([str(irregular_patterns[pattern]) for pattern in line['output_value']]))

print(count, sum)
