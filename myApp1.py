import json
from difflib import SequenceMatcher, get_close_matches

data = json.load(open("data.json"))


# print(data["rain"])

def translate(entered_word):
    # print(SequenceMatcher(None, "rainn", "rain").ratio())
    entered_word = entered_word.lower()
    if entered_word in data:
        return data[entered_word]
    elif get_close_matches(entered_word, data.keys()):
        similar_word = get_close_matches(entered_word, data.keys())
        if len(similar_word) > 0:
            for i in similar_word:
                decision = input("Do you mean: %s " % i)
                if decision == 'y':
                    return data[i]
            return "Which word is that!"
    else:
        return "The word doesn't exist!"


word = input("enter word: ")
