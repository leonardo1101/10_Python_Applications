import json
from difflib import get_close_matches

with open("data.json") as dictionary:
    dictionary_data = json.load(dictionary)

def traslate(word):
    word = word.lower()
    # Check if the word is in the dictionary
    if word in dictionary_data:
        return dictionary_data[word]
    elif word.upper() in dictionary_data:
        return dictionary_data[word.upper()]
    elif word.capitalize() in dictionary_data:
        return dictionary_data[word.capitalize()]
    # If the word isn't in the dictionary we will try find the most similar
    elif get_close_matches(word, dictionary_data.keys(), n=1, cutoff=0.8):
        prob_word = get_close_matches(word, dictionary_data.keys(),
                n=1, cutoff=0.8)[0]
        res = input("Did you mean %s instead? Enter Y if yes, or N if no: " %
                prob_word)
        if res == "Y":
            return dictionary_data[prob_word]
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
