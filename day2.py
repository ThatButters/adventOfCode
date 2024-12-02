safeReports = 0


# Requirements for Safe report:
# ALL INCREASING or DECREASING (no up and down)
# Adjacent differ by at least 1, 3 at most.

## FIX to ONLY MARK SAFE ONCE PER LINE (report) not for every pair.

# read from file to get input data.
with  open("inputDay2.txt", "r") as f:
    lines = f.read().splitlines()

#convert the line into a list of ints
for line in lines:
    numbers = list(map(int, line.split()))
    safe = True
    increasing = False
    decreasing = False

    for x, y in zip(numbers, numbers[1:]):

        diff = abs(y - x)
        if diff < 1 or diff > 3 or diff == 0:
            safe = False
        if y > x:
            increasing = True
        elif y < x:
            decreasing = True
        # exit early due to being unsafe if mixed
        if increasing and decreasing:
            safe = False
        else:
            print("unsafe")
    # If the sequence was safe and meets all criteria, increment safeReports
    if safe:
        safeReports += 1

print (safeReports)