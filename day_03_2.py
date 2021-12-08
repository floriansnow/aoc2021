import numpy

with open('day_03_input_1') as f:
    rows = [list(map(int, list(line.strip()))) for line in f]

def rotate_data(data):
    data = numpy.array(data, int)
    return numpy.rot90(data)[::-1].tolist()

def get_most_common_value(num):
    return int(sum(num) >= len(num) - sum(num))

def get_least_common_value(num):
    return int(not (sum(num) >= len(num) - sum(num)))

def bin_list_to_int(l):
    return int(''.join(map(str, l)), 2)

oxygen_rows = rows.copy()
co2_rows = rows.copy()
for column_index in range(len(rows[0])):
    if len(oxygen_rows) > 1:
        oxygen_columns = rotate_data(oxygen_rows)
        oxygen_mcv = get_most_common_value(oxygen_columns[column_index])
        oxygen_rows = [row for row in oxygen_rows if row[column_index] == oxygen_mcv]
    if len(co2_rows) > 1:
        co2_columns = rotate_data(co2_rows)
        co2_lcv = get_least_common_value(co2_columns[column_index])
        co2_rows = [row for row in co2_rows if row[column_index] == co2_lcv]

print(bin_list_to_int(oxygen_rows[0]) * bin_list_to_int(co2_rows[0]))