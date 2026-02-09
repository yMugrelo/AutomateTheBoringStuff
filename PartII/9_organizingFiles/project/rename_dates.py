import os 
import re 

datePattern = re.compile(r"""
^(.*?)
((0|1)?\d)-           # mês
((0|1|2|3)?\d)-       # dia
((19|20)\d\d)         # ano
(.*?)$
""", re.VERBOSE)


folder = "."

for filename in os.listdir(folder):

    match = datePattern.search(filename)

    if match is None: 
        continue 

    
    before = match.group(1)
    month = match.group(2)
    day = match.group(4)
    year = match.group(6)
    after = match.group(8)

    europeanName = f"{before}{day} - {month} - {year}{after}"

    print(f"Renaming: {filename} → {europeanName}")

    oldPath = os.path.join(folder, filename)
    newPath = os.path.join(folder, europeanName)

    os.rename(oldPath, newPath)

print("Done!")