import csv 

outputFile = open('output.csv', 'w', newline= '')
outputWriter = csv.writer(outputFile)
outputWriter.writerow(['Hello World!', 'Eggs', 'bacon', 'ham'])

