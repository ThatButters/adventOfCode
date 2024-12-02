left = []
right = []
totalCount = 0
totalGap = 0
numGap = 0

with  open("input.txt", "r") as f:
    lines = f.read().splitlines()
    for i in lines:
        a, b = i.split("   ")
        left.append(int(a))
        right.append(int(b))

left.sort()
right.sort()

# Logic of loop
# get first number from each sorted list
# find out how far apart they are from each other (absolute value?)
# add up the distances for all numbers in the lists

for num in range(len(left)):
    numGap = abs(left[num] - right[num])
    totalGap += numGap

print ("Solution to part 1: " + str(totalGap))

#count how many times each number from the left list appears in the right list.
# similarity score
# start with left list, first value, iterate, count amount of times, multiplied by the original number
# for the similarity score, then add all similary scores together.

for x in left:
    totalCount += (right.count(x) * x)

print ("total count of similarity: " + str(totalCount))