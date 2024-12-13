# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

file_name = "wordlewords.txt"
words: [] = []
letter_counts: {str, int} = {}

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


def strip_words():
    global words
    for i in range(len(words)):
        words[i] = words[i].strip()


def read_file(file_name):
    global words

    with open(file_name, 'r') as file:
        words = file.readlines()

    strip_words()


def main():
    read_file(file_name)
    get_letter_count()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
