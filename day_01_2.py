with open('day_01_input_1') as d:
    depths = [int(depth.strip()) for depth in d.readlines()]

def get_depth_windows(depths):
    depth_windows = []
    for index, depth in enumerate(depths):
        if (index + 3) > len(depths):
            return depth_windows
        depth_windows.append(depth + depths[index +1] + depths[index + 2])


depth_increases = 0
prev_depth = None
depth_windows = get_depth_windows(depths)
for depth in depth_windows:
    if not prev_depth:
        print(depth, '(N/A)', depth_increases)
    if prev_depth and prev_depth < depth:
        depth_increases += 1
        print(depth, '(increased)', depth_increases)
    elif prev_depth:
        print(depth, '[decreased]', depth_increases)
    prev_depth = depth

print(depth_increases)