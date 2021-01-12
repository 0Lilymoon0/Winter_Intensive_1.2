# Imports
# -------------------------------------------------
import random
from voicelines import voicelines

# Variables
# -------------------------------------------------
dealer_number = random.randint(1, 21)
player_number = 0
player_draw1 = random.randint(1, 11)
player_draw2 = random.randint(1, 11)
hit_or_stay = "hit"
player_current_draw = random.randint(1, 11)

# Introduction and initial draws
# -------------------------------------------------
voicelines.greeting()
print("\n")
if player_draw1 == 1 or player_draw1 == 11:
  player_draw1 = int(input(voicelines.one_or_eleven()))
  print("\n")
  player_number += player_draw1
else:
  player_number += player_draw1

if player_draw2 == 1 or player_draw2 == 11:
  player_draw2 = int(input(voicelines.one_or_eleven()))
  print("\n")
  player_number += player_draw2
else:
  player_number += player_draw2

print(f'Player, your current number overall is {player_number}')
print("\n")

# Gameplay sequence + results
# -------------------------------------------------
if player_number > 21:
  voicelines.went_bust()
  print("\n")
  voicelines.you_lost()
else:
  while player_number < 21:
    print(f'A reminder player, your score is now {player_number}')
    print("\n")
    hit_or_stay = input(voicelines.hit_or_stay())
    print("\n")
    if hit_or_stay == "pass":
      break
    if player_current_draw == 1 or player_current_draw == 11:
      player_current_draw = int(input(voicelines.one_or_eleven()))
      print("\n")
      player_number += player_current_draw
    else:
      player_number += player_current_draw
  if player_number > 21:
    voicelines.went_bust()
    print("\n")
    voicelines.you_lost()
  elif player_number > dealer_number:
    voicelines.you_won()
  elif player_number < dealer_number:
    voicelines.you_lost()
  elif player_number == dealer_number:
    voicelines.you_tied()
