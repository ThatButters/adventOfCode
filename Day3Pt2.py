import re
with open("inputDay3.txt", "r") as f:
    lines = f.read().splitlines()

def solve_puzzle(memory):
    # Regex to find valid mul and conditional instructions
    pattern = r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)"
    instructions = re.findall(pattern, memory)

    # Start with mul instructions enabled
    mul_enabled = True
    total_sum = 0

    for instr in instructions:
        if instr[0] == "do":
            mul_enabled = True
        elif instr[0] == "don't":
            mul_enabled = False
        elif mul_enabled:
            x, y = int(instr[0]), int(instr[1])
            total_sum += x * y

    return total_sum


# Example memory input
result = solve_puzzle(lines)
print(result)  # This should output 48 (based on your example)
