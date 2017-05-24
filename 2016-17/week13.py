# Number of lines
n = int(input())
lucky = False

# Build the tree
tree = []
for i in range(n):
    tree.append(list(map(int, input().split())))

# The sum of the first branch
leafSum = 0
for j in range(n):
    leafSum += tree[j][0]

# Depth-first search
for i in range(2 ** (n-1)):
    # If it's lucky, no need to continue
    if(leafSum == 13):
        lucky = True
        break
    # Pop a leaf from the nth row every time, the n-1th row every other time, etc.
    for j in range(n):
        if (i+1) % (2 ** j) == 0:
            # Remove the old leaf from the sum
            leafSum -= tree[(n-1)-j][0]
            tree[(n-1)-j].pop(0)
            # Add the next one (if there is a next one)
            if len(tree[(n-1)-j]) > 0:
                leafSum += tree[(n-1)-j][0]

if lucky == False:
    print("not lucky")
else:
    print("lucky")
