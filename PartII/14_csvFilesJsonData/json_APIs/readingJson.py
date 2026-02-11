import json 

pythonValue = {'isCat': True, 'miceCaught': 0, 'name': 'Zophie',
'felineIQ': None}

jsonDataAsPythonValue = json.dumps(pythonValue)
print(jsonDataAsPythonValue)