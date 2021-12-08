with open('day_01_input_1') as d:
    depths = [int(depth.strip()) for depth in d.readlines()]

depth_increases = 0
prev_depth = None
for depth in depths:
    if not prev_depth:
        print(depth, '(N/A)', depth_increases)
    if prev_depth and prev_depth < depth:
        depth_increases += 1
        print(depth, '(increased)', depth_increases)
    elif prev_depth:
        print(depth, '[decreased]', depth_increases)
    prev_depth = depth

print(depth_increases)