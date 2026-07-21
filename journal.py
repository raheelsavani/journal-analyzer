def word_count():
    words = 0
    with open("entries.txt") as file:
        for line in file:
            stripped = line.strip()
            split = stripped.split()
            words += len(split)
    return words


def longest_line():
    longest = ""
    with open("entries.txt") as file:
        for line in file:
            stripped = line.strip()
            lst = stripped.split()
            final = " ".join(lst)
            if len(final) > len(longest):
                longest = final 
    return longest


print("Welcome to your journal. Enter 1 to Add Entry, 2 to View Entries, 3 to Keyword Search, 4 to Analyze, and 5 to Quit")

while True:
    selection = input("Please enter selection.  ").strip()
    if selection == "1":
        entry = input("Please type your entry here:  ")
        with open("entries.txt", "a") as file:
            file.write(entry + "\n")
    elif selection == "2":
        with open("entries.txt") as file:
            for line in file:
                print(line)
    elif selection == "3":
        print("Keyword Search under construction. Check back soon!")
    elif selection == "4":
        print(f"Total Word Count = {word_count()}. Longest Entry = {longest_line()}.")
    elif selection == "5":
        print("Quitting Program")
        break
    else:
        print("Invalid Entry.")

