# Determine if gene2 is a mutation of gene1
def isMutation(gene1, gene2):
    diffCount = 0
    for i in range(len(gene1)):
        if gene1[i] != gene2[i]:
            diffCount += 1
    if diffCount == 1:
        return True
    else:
        return False

# Find mutations of a gene, given a list to test
def findMutations(initGene, geneList):
    mutations = []
    for i in range(len(geneList)):
        if isMutation(initGene, geneList[i]):
            mutations.append(i)
    return sorted(mutations, reverse=True)

def main():
    # Starting gene
    initString = input()
    n = int(input())
    # List of genes
    genes = []
    for i in range(n):
        genes.append(input())
    # Whether it's possible to reach the geek gene given the initial gene
    path = False
    # Number of hops from start to end
    hops = 0
    # Initialize the current "row" as the initial one, next row is it's mutations,
    # next row is their mutations, and so on
    currentRow = [initString]
    while(len(currentRow) > 0):
        nextRow = []
        for item in currentRow:
            mutations = findMutations(item, genes)
            for i in mutations:
                nextRow.append(genes.pop(i))
        hops += 1
        # If it's in the next row, there's nothing more to do
        if "GEEK" in nextRow:
            path = True
            break
        # Otherwise, keep looking
        else:
            currentRow = nextRow
    if path == True:
        print(hops)
    else:
        print("-1")

if __name__ == "__main__":
    main()
