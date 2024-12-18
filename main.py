# represents a letter
class Letter:
    def __init__(self, letter: str, count: int = 0):
        self.letter: str = letter
        self.count: int = count
        self.position_rankings: [int] = [0, 0, 0, 0, 0] # simply the sum of the position of the letter in our word list

    def top_position_index(self):
        return self.position_rankings.index(max(self.position_rankings))

    def top_rank(self) -> int:
        return max(self.position_rankings)

    def rank_position(self, index: int) -> int:
        """
        Every time a letter appears in a position in a word, the rank is incremented by one on that position.
        This means that the more times a letter appears in a position, the higher the rank.
        It also means that the rank is not a percentage, or relative to other letters / positions.
        This lets us not only see how often a letter appears in a position, but how also how common of a letter it is across all words
        :param index:
        :return:
        """
        return self.position_rankings[index]

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

### Global Variables
letters: {str, Letter} = {}
###


class Word:
    def __init__(self, word: str):
        self.letters: [Letter] = []
        self.letter_count = len(word)
        self.word = word.upper()

    def rank(self) -> float:
        """
        Ranks the word based on the rank of each letter in the word.
        As said in the letter rank documentation, the more common a word is the higher it's rank.
        This means that words with very common letters will have a much higher rank that words with less common letters.
        :return:
        """
        letter_ranks = []
        # get each letter rank
        for i in range(self.letter_count):
            letter = self.letters[i]
            rank = letter.rank_position(i) # / letter.top_rank()
            letter_ranks.append(rank)
        return sum(letter_ranks) / self.letter_count # no need to divide by the letter count, as all words are the same length

    @property
    def word(self) -> str:
        return self._word

    @word.setter
    def word(self, word: str):
        self._word = word
        self.letter_count = len(word)
        self.letters = []

        for letter in word:
            self.letters.append(letters[letter])

    def __str__(self):
        return f"{self._word} {self.rank()}"

    def __eq__(self, other):
        return self._word == other._word


    def __lt__(self, other):
        return self.rank() < other.rank()

    def __le__(self, other):
        return self.rank() <= other.rank()

    def __gt__(self, other):
        return self.rank() > other.rank()

    def __ge__(self, other):
        return self.rank() >= other.rank()

    def __hash__(self):
        return hash(self._word)



### More Global Variables
word_ranks: {Word, int} = {}
file_name: str = "wordlewords.txt"
###


def get_letter_foundation() -> {str, Letter}:
    """
    Builds a list of letters and their objects
    :return:
    """
    these_letters: {str, Letter} = {}

    for i in range(26):
        letter = chr(i + 65)
        these_letters[letter] = Letter(letter)

    return these_letters


def build_word_ranks():
    """
    Builds the word_ranks
    :param words:
    :return:
    """
    global word_ranks
    words_str: [str] = read_file(file_name)
    words: [Word] = []
    this_word_ranks: {Word, int} = {}

    # build letter rankings, compile word list
    for word_str in words_str:
        word = Word(word_str)
        words.append(word)
        for i in range(word.letter_count):
            letter = word.letters[i]
            letter.count += 1
            letter.position_rankings[i] += 1

    # print_letters()

    # compile word ranks
    for word in words:
        this_word_ranks[word] = word.rank()

    # sort word ranks from largest to smallest
    sorted_word_ranks = sorted(this_word_ranks.items(), key=lambda x: x[1], reverse=True)

    # print top 10
    for i in range(10):
        print(sorted_word_ranks[i])

    # print bottom 10
    for i in range(10):
        print(sorted_word_ranks[-i])

    word_ranks = dict(sorted_word_ranks)


def print_top_3_guesses():
    """
    Returns the top 3 guesses with unique letters
    :return:
    """
    top_3_guesses = []
    for word in word_ranks:
        # first check if the word has unique letters
        if len(set(word.word)) != len(word.word):
            continue
        # then make sure that the word is not made up of letters in the top 3 guesses list
        if len(top_3_guesses) == 3:
            break

        skip_word = False
        for guess in top_3_guesses:
            for letter in guess.word:
                if letter in word.word:
                    skip_word = True

        if skip_word:
            continue

        top_3_guesses.append(word)

    for guess in top_3_guesses:
        print(guess)


def print_letters():
    for l in letters:
        print(letters[l])


def read_file(this_file_name: str) -> [str]:
    words_str: [str] = []

    with open(this_file_name, 'r') as file:
        for line in file:
            words_str.append(line.strip())

    print(f"Words: {len(words_str)}")
    return words_str


def main():
    global letters
    letters = get_letter_foundation()
    build_word_ranks()
    print_top_3_guesses()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
