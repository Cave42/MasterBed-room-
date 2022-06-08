import pandas as pd
import numpy as np

#Bed files used to compile into masterfile.txt
#Variables can be changed to work in comand line, .bed file type listed for each variable
nCovBed = "C:/Users/cave42/PycharmProjects/bedToMaster/Files/nCoV-2019.bed"
nCovInsertBed = "C:/Users/cave42/PycharmProjects/bedToMaster/Files/nCoV-2019.insert.bed"
nCovTsv = "C:/Users/cave42/PycharmProjects/bedToMaster/Files/nCoV-2019.tsv"

#Files are recompiled into a dataframe, this dataframe stores name of the columns
df = pd.DataFrame(columns=	['sequence_name','target_start', 'target_end',	'amplicon_name', 'fprimer_start', 'fprimer_end', 'fprimer_name',	'rprimer_start',	'rprimer_end',	'rprimer_name',	'forward_sequence',	'reverse_sequence'])

#Used to count my place in the loops, I don't know why my for loop wasn't converting the int properly, so I just added an int to manage how many times the loop had repeated
byTwo = 0
lineCount = 0
newLineCount = 0

#first loop for first file
with open(nCovBed)as file1:
    for line in file1:

        #Seperates the file into line by line
        strippedLine = line.split()

        #checks for every other line to add title
        if(lineCount%2) == 0:
            df.loc[newLineCount, 'sequence_name'] = strippedLine[0]
            emptyName = strippedLine[3].replace('_LEFT','')
            df.loc[newLineCount, 'amplicon_name'] = emptyName
            newLineCount = newLineCount + 1

        #Checks if line is left or right; where it needs to be placed
        if strippedLine[3][-5:] == "_LEFT":
            df.loc[newLineCount-1, 'fprimer_start'] = strippedLine[1]
            df.loc[newLineCount-1, 'fprimer_end'] = strippedLine[2]
            df.loc[newLineCount-1, 'fprimer_name'] = emptyName + "F"

        if strippedLine[3][-5:] == "RIGHT":
            df.loc[newLineCount-1, 'rprimer_start'] = strippedLine[1]
            df.loc[newLineCount-1, 'rprimer_end'] = strippedLine[2]
            df.loc[newLineCount-1, 'rprimer_name'] = emptyName + "R"

        lineCount = lineCount + 1

byTwo = 0
lineCount = 0
newLineCount = 0

#Second .bed file, much shorter
with open(nCovInsertBed)as file2:
    for line in file2:

        strippedLine = line.split()


        df.loc[lineCount, 'target_start'] = strippedLine[1]
        df.loc[lineCount, 'target_end'] = strippedLine[2]

        lineCount = lineCount + 1

byTwo = 0
lineCount = 0
newLineCount = 0

#Last .bed file

with open(nCovTsv) as file3:
    for line in file3:

        strippedLine = line.split()

        if (lineCount % 2) == 0:
            newLineCount = newLineCount + 1

        if strippedLine[0][-5:] == "_LEFT":
            df.loc[newLineCount-1, 'forward_sequence'] = strippedLine[2]

        if strippedLine[0][-5:] == "RIGHT":
            df.loc[newLineCount-2, 'reverse_sequence'] = strippedLine[2]

        lineCount = lineCount + 1

#Downloads the dataframe as a .txtfile
numpy_array = df.to_numpy()
np.savetxt("Masterfile.txt", numpy_array, fmt='%s')