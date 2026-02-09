def collatzSequence():
    print("Enter number: ")
    while True: 
        number = int(input())
        if number % 2 == 0:
            number = number // 2
            print(number)
        elif number % 2 == 1:
            number = 3 * number + 1
            print(number)
        if number == 1:
            break

    
collatzSequence()