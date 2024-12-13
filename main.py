# represents a letter
class Letter:
    def __init__(self, letter: str, count: int = 0):
        self.letter = letter
        self.count = count
        self.position_rankings = [0, 0, 0, 0, 0]

    def top_position_index(self):
        return self.position_rankings.index(max(self.position_rankings))

    def __str__(self):
        return f"{self.letter}: {self.count} {self.position_rankings}"

    def __eq__(self, other):
        if isinstance(other, Letter):
            return self.letter == other.letter
        if isinstance(other, str):
            return self.letter == other

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


def get_filtered_words(top_letter_num=15) -> [str]:
    """
    Get the words that only contain the top 15 letters
    :return:
    """
    global filtered_words
    # get_top_letters(), returns an array of Letters. Get the letter from each Letter
    top_letters: [str] = [letter.letter for letter in get_top_letters(top_letter_num)]
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



def find_top_3_words(num_of_words=3, skip_letters=3):
    top_letter_count = num_of_words * 5
    top_words: [str] = []
    top_letters: [Letter] = get_top_letters(top_letter_count)
    filtered_words: [str] = get_filtered_words(top_letter_count)

    def find_top_word(words, letters):
        """
        Given a list of (assumed) filtered words and a list of the top 15 letters.
        Find the top word that contains the top letter in its top position, and includes letters in the top 15 , minus the letters in the next 3 positions
        :param words:
        :param letters:
        :return:
        """

        top_letter: Letter = letters.pop(0)
        filtered_letters: [str] = [letter.letter for letter in letters]
        filtered_letters = filtered_letters[skip_letters:]
        filtered_letters.append(top_letter.letter)

        narrowed_words: [str] = get_words_with_filter(words, filtered_letters)

        for word in narrowed_words:
            if word[top_letter.top_position_index()] == top_letter.letter:
                # also check that the word is made up of unique letters
                unique_letters = set(word)
                if len(unique_letters) == len(word):
                    return word

        return None

    for i in range(num_of_words):
        top_word = find_top_word(filtered_words, top_letters)
        if top_word is None:
            print(f"Could not find a top word. We have {top_words}")
            # sometimes skip letters may go negative. but keeping it at 0 makes a infinite loop so let it go negative
            return find_top_3_words(num_of_words, skip_letters - 1)

        top_words.append(top_word)
        filtered_words.remove(top_word)
        # remove the letters in the top word from the top_letters
        for letter in top_word:
            if letter in top_letters:
                top_letters.remove(letter)

    print(f"Top {num_of_words} Words: {top_words}")
    return top_words


def main():
    read_file(file_name)
    get_letter_count()
    print_top_letters()
    get_filtered_words()
    find_top_3_words()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
