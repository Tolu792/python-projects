print("Welcome to Python Pizza Deliveries!")
print(" ")
print("OUR PRICES:\nSMALL SIZE: ₦3,000\nMEDIUM SIZE: ₦5,500\nLARGE SIZE: ₦7,500")
print(" ")
size = input("What size pizza do you want? S, M, or L ").lower()
print(" ")
print("TO ADD PEPPERONI COSTS EXTRA:\nFOR SMALL SIZE: ₦200\nFOR MEDIUM & LARGE SIZE: ₦300")
print(" ")
add_pepperoni = input("Do you want pepperoni? Y or N ").lower()
print(" ")
print("WOULD YOU ALSO LIKE TO ADD EXTRA CHEESE?:\nTHIS COSTS ₦100 FOR ALL SIZES")
print(" ")
extra_cheese = input("Do you want extra cheese? Y or N ").lower()

bill = 0
if size == "s":
    bill = 3000
    if add_pepperoni == "y":
        bill += 200
    if extra_cheese == "y":
        bill += 100
    print(f"Your final bill is: ₦{bill}")

elif size == "m":
    bill = 5500
    if add_pepperoni == "y":
        bill += 300
    if extra_cheese == "y":
        bill += 100
    print(f"Your final bill is: ₦{bill}")

elif size == "l":
    bill = 7500
    if add_pepperoni == "y":
        bill += 300
    if extra_cheese == "y":
        bill += 100
    print(f"Your final bill is: ₦{bill}")
