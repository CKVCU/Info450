import random

def fun_game(die_sides):
  """This is a game to roll the user determined die five times"""
  die_rolls=[random.randint(1,die_sides) for die in range(5)]
  return die_rolls

def number_game():
  """This function gets a random number btwn 1 and 10 and the user tries to guess"""
  secret=random.randint(1,10)
  guess=int(input("Guess a number between 1 and 10:"))
  if guess==secret:
    return f"You got it! The number was {secret}."
  else:
    return f"You got it wrong! The number was {secret}."
