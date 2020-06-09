import sys
import pyinputplus as pyip


# to display a gap of 30 lines (by default) to give a individual 'screen' like effect
def spacer(n=30):
    for i in range(n + 1):
        print()


# returns a list of all words in the dictionary
def words_list():
    words = {}
    f = open("C:\\Users\\abukh\\MyPythonScripts\\dictionary.txt")
    for w in f:
        if w == '\n':
            continue
        w = w.split(' ')
        words[w[0].lower()] = " ".join(w[1:])
    f.close()

    return list(words.keys())


# displays all words and their meanings one by one
def display_words():
    if not words_list():  # ie no words in the dictionary
        print("No words to show :(")
        return

    f = open("C:\\Users\\abukh\\MyPythonScripts\\dictionary.txt")
    for w in f:
        if w == '\n':
            continue
        w = w.split(' ')
        print(f'{w[0].upper()}\n   -{" ".join(w[1:])}')
    f.close()


# adds a new word into the text file
def add(word, meaning):
    if word.lower() in words_list():
        print("Word already exists in your dictionary!")
        return

    f = open("C:\\Users\\abukh\\MyPythonScripts\\dictionary.txt",
             "a")  # 'a' appends to the end of the file
    f.write("\n%s %s" % (word.lower(), meaning))
    f.close()


# deletes a word and updates the text file
def delete(word):
    if word.lower() not in words_list():
        print("No such word found in your dictionary!")
        return

    words = {}
    f = open("C:\\Users\\abukh\\MyPythonScripts\\dictionary.txt")
    for w in f:
        if w == '\n':
            continue
        w = w.split(' ')
        words[w[0].lower()] = " ".join(w[1:])
    f.close()

    words.pop(word.lower())

    f = open("C:\\Users\\abukh\\MyPythonScripts\\dictionary.txt",
             "w")  # 'a' appends to the end of the file
    for wo in words.keys():
        f.write("%s %s" % (wo.lower(), words[wo]))
    f.close()

    print("Word deleted successfully.")


#  check if a word exists and display it
def search(word):
    if not words_list():  # ie no words in the dictionary
        print("Dictionary is empty :(")
        return

    # get all words and meanings
    words = {}
    f = open("C:\\Users\\abukh\\MyPythonScripts\\dictionary.txt")
    for w in f:
        if w == '\n':
            continue
        w = w.split(' ')
        words[w[0].lower()] = " ".join(w[1:])
    f.close()

    # display word if it exists, else offer to add it to the dictionary
    if word in words.keys():
        print(f'\n{word.capitalize()}\n   -{words[word]}')
    else:
        add_word = pyip.inputChoice(['y', 'n'], "No such word found in your dictionary, wanna add it (y/n)? ")
        if add_word == 'y':
            print(f"\nWord: {word.capitalize()}")
            meaning = pyip.inputStr(f"Enter {word}'s meaning: ")
            add(word.lower(), meaning)
            print("Word added!")


# displays a list of options to perform
def display_menu():
    print("##### MAIN MENU #####")
    choice = pyip.inputMenu(['1', '2', '3', '4', '5'],
                            "1. Show list of words\n"
                            "2. Search for a word\n"
                            "3. Add word\n"
                            "4. Delete word\n"
                            "5. Quit\n"
                            "\nEnter your choice: ")

    return int(choice)


def main():
    if len(sys.argv) > 1:  # to handle command line input
        word = sys.argv[1].lower()
        meaning = ' '.join(sys.argv[2:])

        print("Word:", word.capitalize())
        if word in words_list():
            print("Word already exits in your dictionary!")
        else:
            print("Meaning:", meaning)

            add(word, meaning)
            print("Word added to your dictionary!")

        quit = pyip.inputChoice(['m', 'q'], "\nType 'm' to go to the main menu or type 'q' to quit: ")
        if quit == 'q':
            print("Bye bye!")
            return

    spacer()
    choice = display_menu()

    while choice != 5:
        if choice == 1:  # display words
            spacer()

            print("##### YOUR WORDS LIST #####\n")

            display_words()

            choice = pyip.inputChoice(['m', 's'],
                                      "\nType 's' to search for a word or 'm' to go back to the main menu: ")
            if choice == 's':
                choice = 's'
                continue
        elif choice == 's' or choice == 2:  # search for a word
            spacer()

            print("##### SEARCH FOR A WORD #####\n")

            w = pyip.inputStr("Enter a word to search: ")

            search(w)

            choice = pyip.inputChoice(['s', 'm'],
                                      "\nType 's' to search again or 'm' to go back to the main menu: ")
            if choice == 's':
                choice = 's'
                continue
        elif choice == 3:  # add word
            spacer()

            print("##### ADD NEW WORD #####")

            word = pyip.inputStr("\nEnter the word: ")

            if word in words_list():
                print("Word already exits in your dictionary!")
            else:
                meaning = pyip.inputStr(f"Enter {word}'s meaning: ")
                add(word, meaning)

                print("Word added to your dictionary!")

            choice = pyip.inputChoice(['m', 'a'], "\nType 'a' to add another word or 'm' to go back to the main menu: ")
            if choice == 'a':
                choice = 3
                continue
        elif choice == 4:
            spacer()

            print("##### DELETE A WORD #####\n")

            word = pyip.inputStr("Enter the word you wish to delete: ")

            delete(word)

            choice = pyip.inputChoice(['m', 'd'],
                                      "\nType 'd' to delete another word or 'm' to go back to the main menu: ")
            if choice == 'd':
                choice = 4
                continue

        spacer()
        choice = display_menu()

    print("\nBye bye!")


main()
