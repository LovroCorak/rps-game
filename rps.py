# -*- coding: utf-8 -*-
"""
Created on Sat Jan 10 21:02:10 2026

@author: lovro
"""

import random
import sys

options = ("rock","paper","scissors")
player= None


while True:
    computer =random.choice(options)
    player=input("Choose between a rock, paper, or scissors (to exit, write 'exit'): ").lower()
    if player in options:
        if player==computer:
            print("Same choice, another round!")
            continue
        break
    if player.lower() == "exit":
        sys.exit()
    print("wrong input.")
    

if (computer=="rock" and player=="paper") or \
    (computer=="paper" and player=="scissors") or \
    (computer=="scissors" and player=="rock"):
    print(f"Player wins, {player} beats {computer}!")

if (player=="rock" and computer=="paper") or \
   (player=="paper" and computer=="scissors") or \
   (player=="scissors" and computer=="rock"):
    print(f"Computer wins, {computer} beats {player}!")
    

