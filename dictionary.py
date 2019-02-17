#Dictionary app looks up existing words in a data file in json

import json
from difflib import get_close_matches #helps to get similar words
#load data from JSON
data = json.load(open("data.json"))

def translate(w):
  #make word lower case to escape case sensitivity
  w = w.lower()
  #if the word is in database, then return word
  if w in data:
    return data[w]
    #if there are similar words, then suggest them else no word like that exists
  elif len(get_close_matches(w,data.keys())) > 0:
    yn = input("Did you mean %s instead? Enter Y if yes, or N if no." %get_close_matches(w,data.keys())[0])
    if yn == "Y":
      return data[get_close_matches(w,data.keys())[0]]
    elif yn == "N":
      return "The word doesn't exist. PLease double check it."
    else:
      return "We didn't understand your entry."
  else:
    return "The word doesnt exist. Please double check it."

word = input("Enter word: ")

print(translate(word))