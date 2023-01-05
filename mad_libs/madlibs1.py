#!/usr/bin/python3

import random

def welcome():
    print("\tWelcome to Mad Libs!\n")
    print("\tKnow your parts of speech? \tWe'll find out!")
    print("\tCreative? \t\t\tWe'll find out!\n")
    print("\tEnjoy! :)\n")

def madlib_type():
  create = input("What do you want to create? (poem |story |joke) ")
  if create.lower() == "poem":
    poem_data = random.choice(poems)
    template = poem_data["template"]
    words = poem_data["words"]
    return template, words
  elif create.lower() == "story":
    story_data = random.choice(stories)
    template = story_data["template"]
    words = story_data["words"]
    return template, words
  elif create.lower() == "joke":
    joke_data = random.choice(jokes)
    template = joke_data["template"]
    words = joke_data["words"]
    return template, words
  else:
    print("Invalid input. Please try again.")

def poem_database():
  poems = [
      {
          "template": "Roses are {color},\nViolets are {color2}.\nSugar is sweet,\nAnd so are you.",
          "words": ["color", "color2"]
      },
      {
          "template": "Twinkle, twinkle, little {noun},\nHow I wonder what you are.\nUp above the world so high,\nLike a {noun2} in the sky.",
          "words": ["noun", "noun2"]
      },
      {
          "template": "I love you more than {noun3}\nMore than {noun4} and {noun5}\nMore than {noun6} on the shore\nI love you more and more.",
          "words": ["noun3", "noun4", "noun5", "noun6"]
      },
      {
          "template": "The {adjective1} {noun1} was {adverb} {verb1}ing in the {noun2}.\nA(n) {adjective2} {noun3} was {adverb} {verb2}ing next to it.\nSuddenly, a(n) {adjective3} {noun4} appeared and started to {verb3}!\nWhat a(n) {adjective4} sight to {verb4}!",
          "words" : ["adjective1", "noun1", "adverb", "verb1", "noun2", "adjective2", "noun3", "adverb", "verb2", "adjective3", "noun4", "verb3", "adjective4", "verb4"]
          }

  ]
  return poems

# Print the welcome message
welcome()

# Get the list of poems from the poem database
poems = poem_database()

# Ask the user what they want to create and get the template and necessary words
template, words = madlib_type()

# Ask the user to input the necessary words
values = {}
for word in words:
  values[word] = input("Enter a {}: ".format(word))

# Insert the user's input into the template
madlib = template.format(**values)

# Print the completed madlib
print(madlib)
