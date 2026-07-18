print("Wlecome to your journal. Enter 1 to Add Entry, 2 to View Entries, 3 to Quit")

while True:
    selection = input("Please enter selection.  ").strip()
    if selection == "1":
        print("Adding Entry")
    elif selection == "2":
        print("Viewing Entries")
    elif selection == "3":
        print("Quitting Program")
        break
    else:
        print("Invalid Entry.")

