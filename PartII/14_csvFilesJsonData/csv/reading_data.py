import csv 
exampleFile = open('example.csv')
exampleReader = csv.reader(exampleFile)
for row in exampleReader: 
    print(f'Row #{exampleReader.line_num} {row}')