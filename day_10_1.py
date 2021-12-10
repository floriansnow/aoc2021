def check(line):
    filo = []
    for char in line:
        if char in opening:
            filo.append(char)
        elif char in closing and filo and char == closing[opening.index(filo[-1])]:
            filo.pop()
        else:
            return char
    if filo:
        return filo


opening = ['[', '(', '<', '{']
closing = [']', ')', '>', '}']
with open("day_10_input_1") as f:
    data = [line.strip() for line in f.readlines()]

illegal_points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}
completion_points = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

illegal_score = 0
completion_scores = []
for line in data:
    completion_score = 0
    illegal = check(line)
    if isinstance(illegal, str):
        illegal_score += illegal_points[illegal]
    else:
        for char in reversed(illegal):
            closing_char = closing[opening.index(char)]
            completion_score = completion_score * 5 + completion_points[closing_char]
        completion_scores.append(completion_score)

print(illegal_score, sorted(completion_scores)[len(completion_scores) // 2])
