import csv 

example_file = open('example.csv')
exampleReader = csv.reader(example_file)
exampleData = list(exampleReader)
print(exampleData)