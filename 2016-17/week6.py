from collections import Counter

def getinput():
    return input()

# Creates a count of how many times each process ID appears
def findDuplicates(inputList):
    processTally = Counter()
    for i in inputList:
        processTally[i] += 1
    return processTally

# Returns the most frequent ID
def identifySmith(inputList):
    # The most common process
    smith = findDuplicates(inputList).most_common(1)
    # Just return the process ID
    return smith[0][0]

# Never actually used...
processCount = getinput()
# The list of process ID's
processes = getinput().split()
# The main function
print(identifySmith(processes))
