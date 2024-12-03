import re
totalSum = 0

# Regular expression pattern with an outer capturing group
# How does anyone do this from memory and not a regex assist tool?
pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

# Reading from the file and finding matches
with open("inputDay3.txt", "r") as f:
    matches = re.findall(pattern, f.read())

# Look through our matches list, multiply the numbers, then add them to totalSum
for match in matches:
    x, y = map(int, match) #convert captured strings to ints
    multipliedValue = x * y
    totalSum += multipliedValue

print(f"the Total total sum of all multiplications is: {totalSum}")
