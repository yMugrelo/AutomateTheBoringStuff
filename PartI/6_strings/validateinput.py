def validatename():
    while True:
        
        print("Please enter your full name: ")
        name = input().title()
        if name.istitle():
            break
        print("Please enter your name!")

    return name 

def validatepassword():
    while True:
        
        print("Please enter a valid new password (only letters or numbers!):")
        password = input()
        if password.isalnum():
            break
        print("Passwords can only have letters and numbers!")

    return password


users = {}

print("Create a new user! ")
name = validatename()
password = validatepassword()

users[name] = password

print(users)