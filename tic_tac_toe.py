# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 11:12:04 2021

@author: mahesh
"""
import numpy as np

class tic_tac_toe:
    
    def __init__(self):
        self.canvas = np.empty(shape = (3,3), dtype = object )
        self.turnvar = " "
        self.initial = np.random.randint(0,2)
        self.game = True
        self.playerlist = ["X","O"]
        
    def check_horizontal(self,canvas):
        for row in range(3):
            val_list = []
            for col in range(3):
                zero = canvas[row][col]
                val_list.append(zero)
            if val_list[0] != None and val_list[1] != None and val_list[2] != None:
                if val_list[0] == val_list[1] and val_list[1] == val_list[2] and val_list[0] == val_list[2]:
                    return -1
        return 0
    
    def check_vertical(self,canvas):
        for col in range(3):
            val_list = []
            for row in range(3):
                zero = canvas[row][col]
                val_list.append(zero)
            if val_list[0] != None and val_list[1] != None and val_list[2] != None:
                if val_list[0] == val_list[1] and val_list[1] == val_list[2] and val_list[0] == val_list[2]:
                    return 1
        return 0
    
    def check_diag(self,canvas):
        val_list_1 = []
        for col,row in zip(range(3),range(3)):
            zero = canvas[row][col]
            val_list_1.append(zero)
        if val_list_1[0] != None and val_list_1[1] != None and val_list_1[2] != None:
            if val_list_1[0] == val_list_1[1] and val_list_1[1] == val_list_1[2] and val_list_1[0] == val_list_1[2]:
                return 1
            
        val_list_2 = []   
        for row,col in zip(range(0,3),range(2,-1,-1)):
            zero = self.canvas[row][col]
            val_list_2.append(zero)
        if val_list_2[0] != None and val_list_2[1] != None and val_list_2[2] != None:
            if val_list_2[0] == val_list_2[1] and val_list_2[1] == val_list_2[2] and val_list_2[0] == val_list_2[2]:
                return 1
        return 0
    def in_deter(self,pos):
        #kill me for this monstrosity of a code
        #past me, what were you thinking...USE A DICTIONARY!!!!
        if pos in [0,1,2]:
            if pos == 0:
                return [0,0]
            if pos == 1:
                return [0,1]
            if pos == 2:
                return [0,2]
        elif pos in [3,4,5]:
            if pos == 3:
                return [1,0]
            if pos == 4:
                return [1,1]
            if pos == 5:
                return [1,2]
        elif pos in [6,7,8]:
           if pos == 6:
               return [2,0]
           if pos == 7:
               return [2,1]
           if pos == 8:
               return [2,2]
        else:
            return -1
    def initial_turn(self):
        self.turnvar = self.playerlist[self.initial]        
    def change_turn(self):
        if self.turnvar == "X":
            self.turnvar = "O"
        else:
            self.turnvar = "X"
    def display_board(self):
        print("----------------------------------------------------\n")
        print(f" canvas \n{self.canvas}     \n\npos_matrix\n{np.array([*range(9)]).reshape(3,3)}")
    def in_canvas(self,pos):
        if self.canvas[pos[0]][pos[1]] == None:
            self.canvas[pos[0]][pos[1]] = self.turnvar
            return 0
        else:
            return -1
        
    def game_conditions(self,canvas):
        x = self.check_horizontal(canvas)
        y = self.check_diag(canvas)
        z = self.check_vertical(canvas)
        if 1 in [x,y,z]:
            return 1
        else:
            return 0
    
    def tie(self):
        if None not in self.canvas:
            return 1
        return 0
    
    def play_game(self):
        self.initial_turn()
        while(self.game):
            self.display_board()
            print(f"player {self.turnvar}'s turn")
            choice = int(input("choose between 0-8: "))
            print("----------------------------------------------------\n")
            pos = self.in_deter(choice)
            if pos == -1:
                print("CHOSE b/w 0-8")
                continue
            valid = self.in_canvas(pos)
            if valid == 0:
                if self.game_conditions(self.canvas) == 1:
                    print(f"{self.turnvar} WINS!")
                    self.display_board()
                    self.game = False
                if self.tie() == 1:
                    print("game tied")
                    self.display_board()
                    self.game = False
                self.change_turn()
            else:
                print("already exists: choose another position to play")
                continue
        print("done")
            
                
            
if __name__ == "__main__":
    game1 = tic_tac_toe()
    game1.play_game()
        
        
