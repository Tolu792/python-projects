print("Welcome to the roller coaster ride!")
bill = 0

while True:
    try:
        height = int(input("How tall are you in cm? "))
        break
    except ValueError:
        print("Invalid input")

if height >= 120:
    print("You can ride the roller coaster!.")

    while True:
        try:
            age = int(input("How old are you? "))
            break
        except ValueError:
            print("Invalid Input")

    if age < 12:
        bill = 5
        print("Child tickets are $5")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7")
    elif 45 <= age <= 55:
        bill = 0
        print("Midlife crisis? Enter for $0!")
    else:
        bill = 12
        print("Adult tickets are $12")

    while True:
        wants_photo = input("Do you want a photo taken? Cost is $3 Y or N: ").lower()
        if wants_photo == "y":
            bill += 3
            break
        else:
            print("Choose either Y or N")

    print(f"Your total bill is ${bill}")


else:
    print("Grow taller.")