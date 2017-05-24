# A function to get input so I can write using open() and you can test using input()
def getinput():
    return input()

# Groups together lines with name matches (in a way that needs to be repeated)
def group_iteration(inputList):
    # The line number that's currently the search terms
    searchLineNumber = 0
    # The queue of lines to be deleted
    deletionQueue = []
    # Take a line of our list...
    for searchLine in inputList:
        #... and search every subsequent line for name matches
        currentLineNumber = searchLineNumber + 1
        for line in inputList[(searchLineNumber + 1):]:
            # Check whether any of the names are in the current line
            nameMatch = False
            for name in searchLine:
                if name in inputList[currentLineNumber]:
                    nameMatch = True
                    break
            # If there is a match, append all the other names to the current line...
            if nameMatch == True:
                for name in searchLine:
                    if name not in inputList[currentLineNumber]:
                        inputList[currentLineNumber].append(name)
                #...and queue the old line for deletion (at the front of the list)
                if searchLineNumber not in deletionQueue:
                    deletionQueue.insert(0, searchLineNumber)
                #...and break, since the current line is queued to become the search one
                currentLineNumber += 1
                break
            else:
                currentLineNumber += 1
        searchLineNumber += 1
    # Delete redundant lines
    for line in deletionQueue:
        del inputList[line]
    return inputList

# Runs group_iteration() until the list it outputs is the same as the input list
def group(inputList):
    previousLength = 0
    while len(inputList) != previousLength:
        previousLength = len(inputList)
        inputList = group_iteration(inputList)
    return inputList

# Searches the list for a line with both search terms
# Takes input as a list of two terms and a list to search
def searchList(searchTerms, inputList):
    for line in inputList:
        if (searchTerms[0] in line) and (searchTerms[1] in line):
            return "yes"
    return "no"

# Number of friendships
friendships = int(getinput())
# List of pairs of friends (stored as lists)
friendshipList = []
# Process inputs into a list
for i in range(friendships):
    friendshipList.append(getinput().split())
# Sort said list into as few groups as possible
friendshipList = group(friendshipList)

# Number of search terms
searchTermNumber = int(getinput())
# List of search term pairs (stored as lists)
searchTermList = []
for i in range(searchTermNumber):
    searchTermList.append(getinput().split())

# Run the searches, and output the results
for searchTerms in searchTermList:
    print(searchList(searchTerms, friendshipList))
