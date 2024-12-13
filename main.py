# represents a letter
class Letter:
    def __init__(self, letter: str, count: int = 0):
        self.letter = letter
        self.count = count
        self.position_rankings = [0, 0, 0, 0, 0]

    def __str__(self):
        return f"{self.letter}: {self.count} {self.position_rankings}"

    def __eq__(self, other):
        return self.letter == other.letter

    def __le__(self, other):
        return self.count <= other.count

    def __lt__(self, other):
        return self.count < other.count

    def __ge__(self, other):
        return self.count >= other.count

    def __gt__(self, other):
        return self.count > other.count
    
# Global Variables
file_name: str = "wordlewords.txt"
words: [str] = []
letters: {str, Letter} = {}
filtered_words: [str] = [] # the words that only contain the top letters


def get_letter_count():
    for word in words:
        for letter in word:
            position = word.index(letter)
            if letter in letters:
                letters[letter].count += 1
            else:
                letters[letter] = Letter(letter, 1)
            # update the position ranking
            letters[letter].position_rankings[position] += 1
    print_letter_count()


def print_letter_count():
    for letter in letters:
        print(f"{letter}: {letters[letter]}")


def get_top_letters(top_num=15) -> [Letter]:
    # Sort the dictionary by value
    return sorted_letters()[:top_num]

def sorted_letters() -> [Letter]:
    """
    Return an array of Letters sorted from top count to lowest count
    :return:
    """
    return sorted(letters.values(), reverse=True)


def print_top_letters(top_num=15):
    top_letters = get_top_letters(top_num)
    the_letters: [] = []
    print("\n\n\nTop Letters:\n")
    for letter in top_letters:
        the_letters.append(letter.letter)
        print(letter)
    print(the_letters)


def get_words_with_filter(these_words: [str], these_letters: [str]) -> [str]:
    """
    Given an array of words and an array of letters, return an array of words that only contain the letters
    :param these_words:
    :param these_letters:
    :return:
    """
    these_filtered_words = []
    for word in these_words:
        add_word = True
        for letter in word:
            if letter not in these_letters:
                add_word = False
        if add_word:
            these_filtered_words.append(word)
    return these_filtered_words


def get_filtered_words():
    """
    Get the words that only contain the top 15 letters
    :return:
    """
    global filtered_words
    # get_top_letters(), returns an array of Letters. Get the letter from each Letter
    top_letters: [str] = [letter.letter for letter in get_top_letters()]
    filtered_words = get_words_with_filter(words, top_letters)
    print(f"Filtered Words: {len(filtered_words)}")
    return filtered_words


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
