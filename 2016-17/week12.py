setCount = int(input())

learningData = []
weights = [1,1]
tally = 0
for i in range(setCount):
    learningData.append(list(map(int, input().split())))
    # A correction for false to make my implementation work
    if(learningData[i][2] == -1):
        learningData[i][2] = 0


# Threshold
t = 0
# Learning Rate
lRate = 0.01
errCount = 1
while errCount > 0:
    errCount = 0
    for i in range(setCount):
        x = learningData[i][0] * weights[0]
        y = learningData[i][1] * weights[1]
        answer = learningData[i][2]
        if (x + y) >= t:
            output = 1
        else:
            output = 0
        if(output != answer):
            errCount += 1
            weights[0] += learningData[i][0] * (answer - output)
            weights[1] += learningData[i][1] * (answer - output)
            t -= lRate * (answer - output)
    # Debug outputs
    print(answer - output)
    print(t)
    print(str(weights[0]) + " " + str(weights[1]))

toTest = int(input())
for i in range(toTest):
    info = list(map(int, input().split()))
    if(((weights[0] * info[0]) + (weights[1] * info[1])) >= t):
        print("Cool")
    else:
        print("Nerd")
