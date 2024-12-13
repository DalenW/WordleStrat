# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

file_name: str = "wordlewords.txt"
words: [str] = []
letter_counts: {str, int} = {}
filtered_words: [str] = [] # the words that only contain the top letters

def get_letter_count():
    for word in words:
        for letter in word:
            if letter in letter_counts:
                letter_counts[letter] += 1
            else:
                letter_counts[letter] = 1
    print_letter_count()


def print_letter_count():
    for letter in letter_counts:
        print(f"{letter}: {letter_counts[letter]}")


def get_top_letters(top_num=15) -> [(str, int)]:
    # Sort the dictionary by value
    sorted_letter_counts = sorted(letter_counts.items(), key=lambda x: x[1], reverse=True)
    top_letters = []
    for i in range(top_num):
        top_letters.append(sorted_letter_counts[i])

    return top_letters


def print_top_letters(top_num=15):
    top_letters = get_top_letters(top_num)
    letters: [] = []
    print("\n\n\nTop Letters:\n")
    for letter in top_letters:
        letters.append(letter[0])
        print(f"{letter[0]}: {letter[1]}")
    print(letters)


def get_filtered_words():
    global filtered_words
    # get_top_letters(), returns a tuple. get the first element of the tuple which is the letter
    top_letters: [str] = [letter[0] for letter in get_top_letters()]
    for word in words:
        add_word: bool = True
        for letter in word:
            if letter not in top_letters:
                add_word = False
        if add_word:
            filtered_words.append(word)
    print(f"Filtered Words: {len(filtered_words)}")


def strip_words():
    global words
    for i in range(len(words)):
        words[i] = words[i].strip()


def read_file(file_name):
    global words

    with open(file_name, 'r') as file:
        words = file.readlines()

    print(f"Words: {len(words)}")
    strip_words()


def main():
    read_file(file_name)
    get_letter_count()
    print_top_letters()
    get_filtered_words()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
