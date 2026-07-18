print("Welcome to your journal. Enter 1 to Add Entry, 2 to View Entries, 3 to Quit")

while True:
    selection = input("Please enter selection.  ").strip()
    if selection == "1":
        entry = input("Please type your entry here:  ")
        with open("entries.txt", "a") as file:
            file.write(entry)
    elif selection == "2":
        with open("entries.txt") as file:
            for line in file:
                print(line, end = "")

    elif selection == "3":
        print("Quitting Program")
        break
    else:
        print("Invalid Entry.")

