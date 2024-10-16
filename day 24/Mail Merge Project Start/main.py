# TODO: Create a letter using starting_letter.txt

with open("./Input/Letters/starting_letter.txt", mode="r") as file:
    content = file.read()

# for each name in invited_names.txt
with open("./Input/Names/invited_names.txt", mode="r") as file:
    names_list = file.read()

names_list = names_list.strip()
name_list = names_list.split("\n")
# Replace the [name] placeholder with the actual name.
for name in name_list:
    new_letter = content.replace("[name]", f"{name}")
    # Save the letters in the folder "ReadyToSend".
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as file:
        file.write(new_letter)
