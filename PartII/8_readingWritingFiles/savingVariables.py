import pprint 

cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]

pprint.pformat(cats)
fileObj = open('myCats.txt', 'w')
fileObj.write('cats = ' + pprint.pformat(cats) + '\n')

fileObj.close()