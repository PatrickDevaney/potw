# Converts two cell letters into a tuple of integers
def convertCell(inString):
    return (int(ord(inString[0]) - 65), int(ord(inString[1]) - 65))

# Turns a tuple of coordinates into two cell letters
def deConvert(inCoords):
    return str(chr(inCoords[0] + 65)) + str(chr(inCoords[1] + 65))

# A depth-first search, implemented from Wikipedia's description
def visit(place, inList, outList, markers):
    i = place[0]
    j = place[1]
    if place not in markers:
        markers[place] = 1
        # If it's not a single integer...
        if not (len(inList[i][j]) == 1) or not (type(inList[i][j][0]) == int):
            for item in inList[i][j]:
                if type(item) != int:
                    visit(convertCell(item), inList, outList, markers)
        sortedCells.insert(0, deConvert((i, j)))

# Calculate the value of a given cell given a tuple of coordinates and a list of cells
def calcCell(place, inList):
    i = place[0]
    j = place[1]
    cellSum = 0
    for item in inList[i][j]:
        if type(item) == int:
            cellSum += item
        # If it's not an integer, get the value of the cell it refers to
        else:
            x,y = convertCell(item)
            cellSum += inList[x][y]
    # Insert the final sum in place of the original calculation
    inList[i][j] = cellSum

n = int(input())
cells = []
sortedCells = []
visited = {}

# Process everything
for i in range(n):
    cells.append(input().split(","))
    for j in range(n):
        cells[i][j] = cells[i][j].split("+")
        for k in range(len(cells[i][j])):
            try:
                cells[i][j][k] = int(cells[i][j][k])
            except ValueError:
                continue

# Do the topological sort
for i in range(len(cells)):
    for j in range(len(cells[i])):
        visit((i,j), cells, sortedCells, visited)

# Calculate the cell values
for i in range(len(sortedCells)):
    calcCell(convertCell(sortedCells.pop()), cells)

# Output the results
for row in cells:
    outStr = ""
    for column in row:
        outStr += str(column) + ","
    # Remove the last comma
    print(outStr[:-1])
