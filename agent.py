# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 14:15:11 2021

@author: mahesh
"""
from tic_tac_toe import tic_tac_toe
import numpy as np
class agent(tic_tac_toe):                
    def __init__(self, agent_mark = "X"):
        self.agent_mark = agent_mark
        self.game = tic_tac_toe()
        self.board = self.game.canvas
        self.iter = 0
        if self.agent_mark == "X":
            self.op_mark = "O"
        else:
            self.op_mark = "X"
            
    def update_canvas(self):
        self.board = self.game.canvas.copy()
        
    def valid_moves_f(self):
        self.update_canvas()
        valid_moves = []
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == None:
                    valid_moves.append([row,col])
        return valid_moves
    
        
    def play(self):
        visited = []
        self.update_canvas()
        valid_moves = self.valid_moves_f()
        for move in valid_moves:
            if move not in visited:
                board = self.board.copy()
                board[move[0]][move[1]] = self.agent_mark
                visited.append(move)
                out = self.game.game_conditions(board)
                if out == 1:
                    return move
        if not valid_moves:
            return -1
        elif len(valid_moves) == 1:
            return valid_moves[0]
        else:
            return valid_moves[np.random.choice([*range(len(valid_moves)-1)])]
        
    def op_play(self):
         visited = []
         self.update_canvas()
         valid_moves = self.valid_moves_f()
         for move in valid_moves:
             if move not in visited:
                 board = self.board.copy()
                 board[move[0]][move[1]] = self.op_mark
                 visited.append(move)
                 out = self.game.game_conditions(board)
                 if out == 1:
                     return move
         if not valid_moves:
             return -1
         elif len(valid_moves) == 1:
             return -1
         else:
             return -1
        
        
    def check_for_win(self):
            if self.game.game_conditions(self.game.canvas) == 1:
                print(f"{self.game.turnvar} WINS!")
                self.game.game = False
                self.game.display_board()
            if self.game.tie() == 1:
                print("game tied")
                self.game.display_board()
                self.game.game = False
    
    def bot_play(self):
        self.game.turnvar = self.agent_mark
        while(self.game.game):
            self.game.display_board()
            print(f"player {self.game.turnvar}'s turn")
            if self.game.turnvar == self.agent_mark:
                played = self.play()
                blocking = self.op_play()
                if blocking == -1:
                    valid = self.game.in_canvas(played)
                else:
                    valid = self.game.in_canvas(blocking)
                if played == -1:
                    print("game tied")
                    self.game.display_board()
                    self.game.game = False
                    continue
                self.check_for_win()
            else:
                choice = int(input("choose between 0-8: "))
                print("----------------------------------------------------\n")
                pos = self.game.in_deter(choice)
                if pos == -1:
                    print("CHOSE b/w 0-8")
                    continue
                valid = self.game.in_canvas(pos)  
                if valid == 0:
                    self.check_for_win()
                else:
                    print("already exists: choose another position to play")
                    continue
            self.game.change_turn()
        
            
if __name__ == "__main__":
    bot_play1 = agent(agent_mark = "O")
    bot_play1.bot_play()       
