arrayA=[1,2]
arrayB=[3,4]
def printUnorderedPairs(arrayA, arrayB):
    for i in range(len(arrayA)):
        for j in range(len(arrayB)):
            for k in range(0,5):
                print(str(arrayA[i]) + "," + str(arrayB[j]))
printUnorderedPairs(arrayA, arrayB)