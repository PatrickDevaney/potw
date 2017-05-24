def castBallot(vote, district, inList):
    if inList[district][1] == 0:
        inList[district][0] = vote
        inList[district][1] = 1
    elif inList[district][0] == vote:
        inList[district][1] += 1
    else:
        inList[district][1] -= 1


districts, votes = list(map(int, input().split()))
districtCounts = []

# Populate the district count
for i in range(districts):
    districtCounts.append(["",0])

# Count individual votes
for i in range(votes):
    vote, district = input().split()
    district = int(district)
    castBallot(vote, district, districtCounts)

# Count districts
electoralCollege = [["", 0]]
for win in districtCounts:
    castBallot(win[0], 0, electoralCollege)

print(electoralCollege[0][0])
