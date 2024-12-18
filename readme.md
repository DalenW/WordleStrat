# Wordle Strategy

Given a list of 5 letter words, this finds the top 3 words from the top 15 letters by occurrence, using words with the top (first) best letter position.

A better way to put it is it finds the count of each letter in each position in the word list. 
Then we use that information to make a word "rank". 
Then, given a sorted list, we find the top 3 ranked words made up of unique letters.