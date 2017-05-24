class Person:
    def __init__(self, name, interests):
        self.name = name
        self.interests = interests
        self.score = None
    def getName(self):
        return self.name
    def getInterests(self):
        return self.interests
    def checkCompatibility(self, otherPerson):
        otherInterests = otherPerson.getInterests()
        union = len(self.interests) + len(otherInterests)
        intersection = 0
        for interest in self.interests:
            if interest in otherInterests:
                intersection += 1
        union -= intersection
        return intersection / union

n = int(input())
people = []
for i in range(n):
    line = input().split()
    currentPerson = Person(line[0], line[1:])
    people.append(currentPerson)
david = people.pop(0)
people.sort(key=lambda x: x.checkCompatibility(david), reverse=True)
print(people.pop(0).getName())
