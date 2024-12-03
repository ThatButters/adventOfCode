safeReports = 0

# Read from file to get input data
with open("inputDay2.txt", "r") as f:
    lines = f.read().splitlines()

# Function to check if a report is safe with one potential issue
def is_safe_with_dampener(numbers):
    increasing = decreasing = True
    dampener_used = False

    for i in range(len(numbers) - 1):
        diff = numbers[i + 1] - numbers[i]

        if abs(diff) < 1 or abs(diff) > 3:
            if not dampener_used:
                dampener_used = True
            else:
                return False

        if diff > 0:
            decreasing = False
        elif diff < 0:
            increasing = False

        if increasing and decreasing:
            if not dampener_used:
                dampener_used = True
            else:
                return False

    return increasing or decreasing


# Convert the line into a list of ints and check for safety
for line in lines:
    numbers = list(map(int, line.split()))
    print(f"Checking report: {numbers}")  # Debug statement
    if is_safe_with_dampener(numbers):
        print("Safe with or without dampener")  # Debug statement
        safeReports += 1
    else:
        print("Unsafe")  # Debug statement

print(f"Total safe reports: {safeReports}")