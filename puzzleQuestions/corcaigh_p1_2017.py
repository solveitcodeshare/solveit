#Corcaigh-xit, Q1 2017

import fileinput
import sys
filename = "testp1_2017_2"

#input file shuld be given via stdinput e.g. python corcaigh_p1_2017.py < input/testp1_2017_1.in

#read in the header line
header = input().split()

rows,cols = int(header[0]),int(header[1])

#read in the data
#need to track indexes
i = 0
mineLocations = []
minesCountOutput= []
for line in fileinput.input():
    rowOutput =  [0] * cols
    for k, m in enumerate(line.split()):

        if m == "x": #found mine
            rowOutput[k] = 'x'
            mineLocations.append([i,k])
    i+=1
    minesCountOutput.append(rowOutput)

#create output list all set to zero
#minesCountOutput = [ [0] * cols for _ in range(rows)]

#go through mines and increment neighbouts
for mine in mineLocations:
    for i in range((mine[0]-1),(mine[0]+2)):

        for j in range((mine[1]-1),(mine[1]+2)):

            if (i >= 0 and j >= 0) and (i < rows and j < cols):
                if (minesCountOutput[i][j] != 'x'):
                    #this location gets incremented
                    #print(mine[0],mine[1],"UPDATE ",i,j,minesCountOutput[i][j])
                    minesCountOutput[i][j] +=1
#create outpurstring
outputstring = ""
for line in minesCountOutput:
    for i, a in enumerate(line):
        outputstring += str(a)
        if i<(len(line)-1):
            outputstring += " "
    outputstring+="\n"

#test the input
filenameExpected = 'expectedoutputs\\'+filename+'.expected'
filenameOutput = 'output\\'+filename+'.out'

with open(filenameExpected, 'r') as content_file:
    expectedoutput = content_file.read()

if outputstring != expectedoutput:
    print("OUTPUT DOES NOT MATCH EXPECTED")
else:
    sys.stdout.write(outputstring)
    #sys.stdout.flush()

#output to file
with open(filenameOutput,"w") as fileout:
    fileout.write(outputstring)
