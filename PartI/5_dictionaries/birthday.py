birthdays = {'Gabriel' : 'Apr 1', 'Bernardo' : 'Jul 17', 'Renato' : 'Jan 16'}

while True: 
    print("Enter a name: (Blank to quit)")
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(f"{birthdays[name]} is the birthday of {name.title()}")

    else:
        print(f"I do not have birthdau information for {name}")
        print("What is their birthday? ")
        bday = input()
        birthdays[name] = bday
        print("Birthday database updated!")

print("ALL the birthday list: \n")
for i, j in birthdays.items():
    print(f"\t-{j.title()} is the birthday of {i.title()}!")