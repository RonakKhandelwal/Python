#!/usr/bin/env python

import random
import time

rock = 1
paper = 2
scissors = 3

names = { rock: "Rock", paper: "Paper", scissors: "Scissors" }
rules = { rock: scissors, paper: rock, scissors: paper }

player_score = 0
computer_score = 0
def start():
    print "Lets play a game of Rock, Paper & Scissors"
    while game():
        pass
    scores()

def game():
    player = move()
    computer = random.randint(0,3)
    result(player, computer)
    return play_again()
def move():
    while True:
        player = raw_input("Rock = 1, Paper = 2 & Scissors = 3")
        try:
            player = int(player)
            if player in (1, 2, 3):
                return player
        except ValueError:
            pass
        print "Oops worng value entered"
def result(player, computer):
    print "1..."
    time.sleep(1)
    print "2..."
    time.sleep(1)
    print "3..."
    time.sleep(1)

    print "Computer threw {0}!".format(names[computer])
    global player_score, computer_score
    if player == computer:
        print "Tie game"
    else:
        if rules[player] == computer:
            player_score += 1
            print "Victory"
        else:
            computer_score += 1
            print "Next time is ours"
def play_again():
    print "Do you want to play again?"
    ans = raw_input()
    if ans == "y":
        return answer
    else:
        print "Thank you"

def scores():
    global player_score, computer_score
    print "player : ", player_score
    print "Computer : ", computer_score

if __name__ == '__main__':
    start()
