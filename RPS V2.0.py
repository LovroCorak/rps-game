# -*- coding: utf-8 -*-
"""
Created on Thu Jan 15 13:48:48 2026

@author: lovro
"""
import tkinter as tk
import random

class RPSGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Rock paper scissors")
        self.root.geometry("400x400")
        
        self.score_player = 0
        self.score_pc = 0
        
        self.choices = ["rock", "paper", "scissors"]
        
        # Naslov
        tk.Label(self.root, text="Choose!", font=("Arial", 16)).pack(pady=20)
        
        # Gumbi
        frame = tk.Frame(self.root)
        frame.pack(pady=20)
        tk.Button(frame, text="🪨 Rock", command=lambda: self.play("rock"), width=12, height=2).pack(side=tk.LEFT, padx=10)
        tk.Button(frame, text="📄 Paper", command=lambda: self.play("paper"), width=12, height=2).pack(side=tk.LEFT, padx=10)
        tk.Button(frame, text="✂️ Scissors", command=lambda: self.play("scissors"), width=12, height=2).pack(side=tk.LEFT, padx=10)
        
        # Rezultat
        self.result_label = tk.Label(self.root, text="", font=("Arial", 14), fg="blue")
        self.result_label.pack(pady=20)
        
        # Rezultat
        self.score_label = tk.Label(self.root, text="Ti: 0 | PC: 0", font=("Arial", 12))
        self.score_label.pack(pady=10)
        
        # Reset
        tk.Button(self.root, text="New game", command=self.reset, bg="lightgreen").pack(pady=20)
    
    def play(self, player):
        pc = random.choice(self.choices)
        
        if player == pc:
            rezultat = "TIE!"
        elif (player == "rock" and pc == "scissors") or \
             (player == "scissors" and pc == "paper") or \
             (player == "paper" and pc == "rock"):
            rezultat = f"You win! {player} beats {pc}"
            self.score_player += 1
        else:
            rezultat = f"PC won! {pc} beats {player}"
            self.score_pc += 1
        
        self.result_label.config(text=rezultat)
        self.score_label.config(text=f"You: {self.score_player} | PC: {self.score_pc}")
    
    def reset(self):
        self.score_player = 0
        self.score_pc = 0
        self.result_label.config(text="")
        self.score_label.config(text="You: 0 | PC: 0")
    
    def run(self):
        self.root.mainloop()

game = RPSGame()
game.run()

