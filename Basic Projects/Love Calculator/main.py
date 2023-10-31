print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_name = name1 + name2

lower_case_name = combined_name.lower()

true_count = lower_case_name.count("t") + lower_case_name.count("r") + lower_case_name.count(
    "u") + lower_case_name.count("e")  # counting for 'TRUE' in combined name

love_count = lower_case_name.count("l") + lower_case_name.count("o") + lower_case_name.count(
    "v") + lower_case_name.count("e")  # counting for 'LOVE' in combined name

love_score = int(str(true_count) + str(love_count))  # change values to string

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif 40 <= love_score <= 50:
    print(f"Your score is {love_score} you are alright together.")
else:
    print(f"Your score is {love_score}%")
