import mysql.connector
from dictionary_data_base import *
from difflib import get_close_matches

def traslate(word):
    # Load words from dictionary
    words = get_all_words_in_dictionary()
    word = word.lower()
    # Check if the word is in the dictionary
    if word in words:
        return get_possible_definitions(word)
    elif word.upper() in words:
        return  get_possible_definitions(word.upper())
    elif word.capitalize() in words:
        return get_possible_definitions(word.capitalize())
    # If the word isn't in the dictionary we will try find the most similar
    elif get_close_matches(word, words, n=1, cutoff=0.8):
        prob_word = get_close_matches(word, words,
                n=1, cutoff=0.8)[0]
        res = input("Did you mean %s instead? Enter Y if yes, or N if no: " %
                prob_word)
        if res == "Y":
            return get_possible_definitions(prob_word)
        elif res != "N":
            return "We didn't undestand your entry."
    return "The word doesn't exist. Please double check it."

word = input("Enter word: ")
result = traslate(word)
# Show each definition
if isinstance(result, list):
    number_definitions = len(result)
    for def_index in range(number_definitions):
        print("%dº Definition: %s" % (def_index + 1, result[def_index]))
else:
    print(result)
