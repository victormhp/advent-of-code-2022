# A X -> Rock 
# B Y -> Paper 
# C Z -> Scissors


def get_input():
    with open("./input.txt") as f:
        input_lines = f.read().splitlines()
    return input_lines


def part1(input_lines):
    results = {
    "A X": 3 + 1,
    "A Y": 6 + 2,
    "A Z": 3,
    "B X": 1,
    "B Y": 3 + 2,
    "B Z": 6 + 3,
    "C X": 6 + 1,
    "C Y": 2,
    "C Z": 3 + 3
}

    points = 0
    for game in input_lines:
        points += results[game]
        
    return points


def part2(input_lines):
    results = {
    "A X": 3,
    "A Y": 3 + 1,
    "A Z": 6 + 2,
    "B X": 1,
    "B Y": 3 + 2,
    "B Z": 6 + 3,
    "C X": 2,
    "C Y": 3 + 3,
    "C Z": 6 + 1
}

    points = 0
    for game in input_lines:
        points += results[game]
        
    return points
    
    
input_lines = get_input()
print(f"Part 1: {part1(input_lines)}")
print(f"Part 2: {part2(input_lines)}")
