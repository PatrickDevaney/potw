# I'm a first-year, so complexity rules don't apply to me
# To run: Enter the input file (e.g. input.txt)

import math

filename = input("Input file name:\n")

# Simple distance using pythagorean theorem
# Takes input as two lists
def distancefrom(a, b):
    x1 = a[0]
    y1 = a[1]
    x2 = b[0]
    y2 = b[1]
    distx = abs(x1 - x2)
    disty = abs(y1 - y2)
    dist = math.sqrt((distx * distx) + (disty * disty))
    return dist

# Returns space-seperated numbers as a list
def spaceSepProcess(numbers):
    space = numbers.find(" ")
    x = int(numbers[:space])
    space += 1
    y = int(numbers[space:])
    return [x,y]

# Turns the list created above back into space-seperated numbers
def deProcess(l):
    return str(l[0]) + " " + str(l[1])

values = open(filename, "r")
# Initial location
initial = spaceSepProcess(values.readline())
# Number desired
desired = int(values.readline())
# Number total
total = int(values.readline())



# Creates and sorts a list of locations, then outputs it
locations = {}
for i in range(total):
    currentloc = spaceSepProcess(values.readline())
    distance = distancefrom(initial, currentloc)
    locations[distance] = currentloc
x = sorted(locations)
for i in range(desired):
    print(deProcess(locations[x[i]]))
