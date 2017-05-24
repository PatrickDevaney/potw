def getinput():
    return input()

# Checks a signle IP
def checkIP(bannedList, ip):
    if ip[0] in bannedList[0]:
        i = 1
        previous = ip[0]
        for term in ip[1:]:
            # If we've reached the end of the range
            if "," in bannedList[i][previous]:
                return "banned"
            # Or if we have a whole IP
            elif (i == 3) and (term in bannedList[i][previous]):
                return "banned"
            # Otherwise, it must be valid
            elif term not in bannedList[i][previous]:
                break
            previous += "." + term
            i += 1
    return "valid"

# Checks the whole list
def banHammer(bannedList, ipList):
    for ip in ipList:
        print(checkIP(bannedList, ip))


bannedRangeNumber = int(getinput())
# A list of a list and 3 dictionaries
bannedRangeList = [[], {}, {}, {}]
for i in range(bannedRangeNumber):
    bannedRange = str(getinput()).split(".")
    # If the first term's not already a key, add it
    if bannedRange[0] not in bannedRangeList[0]:
        bannedRangeList[0].append(bannedRange[0])
    ipTerm = 1
    previousTerms = bannedRange[0]
    # Creates a series of dictionaries with the preceding part as the key
    for term in bannedRange[1:]:
        if previousTerms not in bannedRangeList[ipTerm]:
            bannedRangeList[ipTerm][previousTerms] = [term]
        # Append the term if it's not there and it's not already a whole banned range
        elif (term not in bannedRangeList[ipTerm][previousTerms]):
            bannedRangeList[ipTerm][previousTerms].append(term)
        previousTerms += "." + term
        ipTerm += 1
    # Add a "," to mark the end of a range if it's not a full IP
    if ipTerm < 4:
        bannedRangeList[ipTerm][previousTerms] = [","]

testIPNumber = int(getinput())
# A list of IPs to test, split by "."
testIPList = []
for i in range(testIPNumber):
    testIPList.append(str(getinput()).split("."))

banHammer(bannedRangeList, testIPList)
