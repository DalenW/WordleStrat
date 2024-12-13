# Wordle Strategy

Given a list of 5 letter words, this finds the top 3 words from the top 15 letters by occurrence, using words with the top (first) best letter position.

A better way to put it is the script (by default) finds the top 15 letters by occurrence. 
Then, it tries to find the top 3 words. 
First, it takes the best letter and it's top position, and finds a word that has that letter in that position, made up of letters in the top 15 list.
Next it removes that word from the word list, and it's letters from the top letter list.
Then it repeats the process for the next best letter and position, and so on.

Long story short, here's the result:

1. Pendu
2. Calmy
3. Riots