arrayA=[1,2,3,4,5]
arrayB=[1,9,0,6,12]
def printUnorderedPairs(arrayA, arrayB):
    for i in range(len(arrayA)):
        for j in range(len(arrayB)):
            if arrayA[i] < arrayB[j]:
                print(str(arrayA[i]) + "," + str(arrayB[j]))
printUnorderedPairs(arrayA, arrayB)