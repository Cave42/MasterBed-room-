import pandas as pd
import numpy as np

nCovBed = "C:/Users/cave42/PycharmProjects/bedToMaster/Files/nCoV-2019.bed"
nCovInsertBed = "C:/Users/cave42/PycharmProjects/bedToMaster/Files/nCoV-2019.insert.bed"
nCovTsv = "C:/Users/cave42/PycharmProjects/bedToMaster/Files/nCoV-2019.tsv"

df = pd.DataFrame(columns=	['sequence_name','target_start', 'target_end',	'amplicon_name', 'fprimer_start', 'fprimer_end', 'fprimer_name',	'rprimer_start',	'rprimer_end',	'rprimer_name',	'forward_sequence',	'reverse_sequence'])

byTwo = 0
lineCount = 0
newLineCount = 0

with open(nCovBed)as file1:
    for line in file1:

        strippedLine = line.split()

        if(lineCount%2) == 0:
            df.loc[newLineCount, 'sequence_name'] = strippedLine[0]
            emptyName = strippedLine[3].replace('_LEFT','')
            df.loc[newLineCount, 'amplicon_name'] = emptyName
            newLineCount = newLineCount + 1

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

with open(nCovInsertBed)as file2:
    for line in file2:

        strippedLine = line.split()


        df.loc[lineCount, 'target_start'] = strippedLine[1]
        df.loc[lineCount, 'target_end'] = strippedLine[2]

        lineCount = lineCount + 1

byTwo = 0
lineCount = 0
newLineCount = 0

with open(nCovInsertBed) as file2:
    for line in file2:
        strippedLine = line.split()

        df.loc[lineCount, 'target_start'] = strippedLine[1]
        df.loc[lineCount, 'target_end'] = strippedLine[2]

        lineCount = lineCount + 1

byTwo = 0
lineCount = 0
newLineCount = 0

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

#print(df.to_string())

numpy_array = df.to_numpy()
np.savetxt("Masterfile.txt", numpy_array, fmt='%s')