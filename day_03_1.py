import numpy

with open('day_03_input_1') as f:
    data = [list(line.strip()) for line in f]

data = numpy.array(data, int)
data = numpy.rot90(data)[::-1].tolist()
#data = [''.join(map(str, line)) for line in data]

majority = (len(data[0]) // 2) + 1

gamma_rate = int(''.join(map(str, [sum(entry) // majority for entry in data])), 2)
epsilon_rate = int(bin((gamma_rate ^ (2 ** (len(data)+1) - 1)))[3:], 2)
print(gamma_rate * epsilon_rate)
