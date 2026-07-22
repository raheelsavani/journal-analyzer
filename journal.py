def word_count(): #function to get total count of words, called in section 4
    words = 0
    with open("entries.txt") as file:
        for line in file:
            stripped = line.strip()
            split = stripped.split()
            words += len(split)
    return words


def longest_line(): #function to get longest entry, called in section 4
    longest = ""
    with open("entries.txt") as file:
        for line in file:
            stripped = line.strip()
            lst = stripped.split()
            final = " ".join(lst)
            if len(final) > len(longest):
                longest = final 
    return longest


print("Welcome to your journal. Enter 1 to Add Entry, 2 to View Entries, 3 to Keyword Search, 4 to Analyze, and 5 to Quit") #welcome message + instructions

try:
    file = open("entries.txt")
    file.close()
except FileNotFoundError:
    file = open("entries.txt", "a")
    file.close()

while True:
    selection = input("Please enter selection.  ").strip()
    if selection == "1": # section for adding entry
        entry = input("Please type your entry here:  ")
        with open("entries.txt", "a") as file:
            file.write(entry + "\n")
    elif selection == "2": # section for viewing entries
        with open("entries.txt") as file:
            found_entry = False
            for line in file:
                print(line)
                found_entry = True
        if found_entry == False:
            print("No entries found")
    elif selection == "3": # section for searching by keyword
        kw = input("Enter keyword:  ").lower()
        with open("entries.txt") as file:
            flag = False
            for line in file:
                if kw in line.lower():
                    flag = True
                    print(line)
        if flag == False:
                print("Keyword not found.")
    elif selection == "4": #section for running analysis 
        print(f"Total Word Count = {word_count()}. Longest Entry = {longest_line()}.")
    elif selection == "5": #section to end program
        print("Quitting Program")
        break
    else:
        print("Invalid Entry.")

