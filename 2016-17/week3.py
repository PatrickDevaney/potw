# Using Python 3
# To run, enter input file name

import math

filename = open(input("Input file name:\n"), "r")

documentCount = int(filename.readline())

# The list of document words
documents = []
for i in range(documentCount):
    documents.append(filename.readline().split())
# The word to search for
searchTerm = filename.readline()

# Word frequency list - aka tf(T, di)
documentSearch = []
for currentDoc in documents:
    count = 0
    for i in currentDoc:
        if i == searchTerm:
            count += 1
    documentSearch.append(count)

# Calculate idf(T, D)
containsCount  = 0
for i in documentSearch:
    if i != 0:
        containsCount += 1
idfTD = math.log10(documentCount / containsCount)

for i in range(documentCount):
    print(str(i + 1) + " " + str(round((documentSearch[i] * idfTD), 6)))
