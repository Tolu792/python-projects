PLACEHOLDER = "[name]"

# Read the starting letter
with open("Input/Letters/starting_letter.txt") as letter_file:
    letter_content = letter_file.read()

# Read the names in the invited names
with open("Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

    # iterate through the names
    for name in names:
        stripped_name = name.strip()  # strip the name of whitespace.
        modified_letter = letter_content.replace(PLACEHOLDER, stripped_name)  # replace placeholder with names in the
                                                                              # invited names

        # Write to the Ready to send folder
        with open(f"Output/ReadyToSend/letter_to_{stripped_name}.txt", mode="w") as complete_letter:
            complete_letter.write(modified_letter)
