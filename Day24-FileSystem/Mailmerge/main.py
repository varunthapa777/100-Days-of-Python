with open("input/Names/invited_names.txt") as file:
    name_list = file.read().splitlines()

print(name_list)

with open("input/Letters/starting_letter.txt") as file:
    letter = file.read()

for name in name_list:
    new_letter = letter.replace("[name]", name)
    with open(f"Output/ReadyToSend/letter_for_{name}.txt", "w") as f:
        f.write(new_letter)


