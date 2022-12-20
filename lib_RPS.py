import random

rps = ["Rock", "Paper", "Scissors"]
drc = ["Up", "Down", "Left", "Right"]
winning_matchups = {"Rock":"Scissors", "Paper":"Rock", "Scissors":"Paper"}

def bot_rps():
    random.seed()
    n = random.randrange(0, 3)
    return rps[n]

def bot_drc():
    random.seed()
    n = random.randrange(0, 4)
    return drc[n]

def rps_battle(player_hand, bot_hand):
    if player_hand == bot_hand:
        return 0
    elif winning_matchups[player_hand] == bot_hand:
        return 1
    else:
        return -1
