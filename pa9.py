def main():
    
    inFile = open("pa9.words", 'r')

    word = inFile.readline().strip()
    wordList = []

    while word != "ZZZZZ":
        wordList.append(word)
        word = inFile.readline().strip()

    inFile.close()

    # length of the list
    listLength = len(wordList)
    sumWordsLength = 0
    print("Length =", listLength)
    
    # average word length (round to 1 decimal)
    for i in range(listLength):
        currentWord = wordList[i]
        lengthCurrentWord = len(currentWord)
        sumWordsLength += lengthCurrentWord

    averageWordLength = sumWordsLength / listLength
    print("Average Word Length =", format(averageWordLength, '.1f'))

    print()

    countWordsGreaterAverage = 0
    #count of words that are longer than the average word length
    for i in range (listLength):
        currentWord = wordList[i]
        lengthCurrentWord = len(currentWord)
        if lengthCurrentWord > averageWordLength:
            countWordsGreaterAverage += 1
    print("Number of words above average word length =", countWordsGreaterAverage)

    print()

    #count of vowels
    countA = countE =countI = countO = countU = 0
    for i in range (listLength):
        currentWord = wordList[i]
        lengthCurrentWord = len(currentWord)
        for i in range (lengthCurrentWord):
            if currentWord[i] == 'a':
                countA += 1
            elif currentWord[i] == 'e':
                countE += 1
            elif currentWord[i] == 'i':
                countI += 1
            elif currentWord[i] == 'o':
                countO += 1
            elif currentWord[i] == 'u':
                countU += 1
    print("A count =", countA)
    print("E count =", countE)
    print("I count =", countI)
    print("O count =", countO)
    print("U count =", countU)

    print()

    # print the list in reverse, but skip 10 items as you print 
    #(that is, step should be -10)
    print("List printed in reverse, skipping 10 entries at a time ...")
    for i in range (listLength -1, -10, -10 ):
        currentWord = wordList[i]
        print(currentWord, end = ', ')
    
main()