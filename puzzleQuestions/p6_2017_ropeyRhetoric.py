#repairing ropery rhetoric

#sample call  python p6_2017_ropeyRhetoric.py < input/p6_2017_1.in

#read in the input
header1 = input()
numOfTexts = int(header1)

i = 0
originalText = []
updatedText = []
charsText1 = []
charsText2 = []
#print(numOfTexts)


while i < numOfTexts:
    textHeader=input()
    #print(textHeader)
    charsNums =  [int(x) for x in textHeader.split()]
    charsText1.append(charsNums[0])
    charsText2.append(charsNums[1])
    #read in original
    originalText.append(input())
    updatedText.append(input())
    i+=1

#go through input and output, creating a dict for each
results = []

for i, inp in enumerate(originalText):
    inputDict = {}
    outputDict = {}
    score = 0
    print(originalText)
    print(updatedText)

    for c in inp:
        inputDict[c] = inputDict.get(c, 0) + 1
    #same for corrosponding putput
    for c2 in updatedText[i]:
        outputDict[c2] = outputDict.get(c2,0) + 1

    #generate score

    #if the text 2 is bigger add the difference- characters must be added
    if charsText2[i] - charsText1[i] > 0:
        score +=  charsText2[i] - charsText1[i]
        print(score)
    for key in inputDict.keys():
        count = inputDict.get(key) - outputDict.get(key,0)
        print(key," ",inputDict.get(key)," ",outputDict.get(key,0)," ",count)
        if count >0:
            score += count
    # for key in outputDict.keys():
    #     if inputDict.get(key,0) == 0:
    #         score+=outputDict.get(key,0)
    results.append(score)


for r in results:
    print(r)
