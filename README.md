

<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->



<!-- PROJECT LOGO -->
<br />

  <h3 align="center"> Tic_Tac_Toe_with_1_step_look_ahead_agent</h3>

  <p align="center">
    A tic-tac-toe game with agent(opponent) using n-step lookahead algorithm
    <br />
  </p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

![project screenshot](https://github.com/sirreajohn/Tic_Tac_Toe_with_1_step_look_ahead_agent/tree/main/images/check_.png?raw=true)

this is a tictactoe game made from scratch under 1 hr as part of a challenge, while implementing an agent is out of scope of the said challenge. it gave me a opportunity to 
explore a new ~niche pleasure of watching ur creation doing things~ hobby

### Built With

Welp!, nothing just python 3.8 and numpy 
* [Python](https://www.python.org/)



<!-- GETTING STARTED -->
## Getting Started

To set this up locally, just download the rar and open IDE, set PWD to these files, **run the agent.py**

## features

* one step look ahead to play a turn 
```
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
```
![win_one](https://github.com/sirreajohn/Tic_Tac_Toe_with_1_step_look_ahead_agent/tree/main/images/win_one.png?raw=true)

* blocking player
```
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
```
![blocking](https://github.com/sirreajohn/Tic_Tac_Toe_with_1_step_look_ahead_agent/tree/main/images/blocks happen!.png)

<!-- CONTACT -->
## Contact

Mahesh Patapalli - sirreajohn@gmail.com


[linkedin](https://www.linkedin.com/in/mahesh-patapalli-bba1aa191/) - [github](https://github.com/sirreajohn)


Project Link: [https://github.com/sirreajohn/Tic_Tac_Toe_with_1_step_look_ahead_agent](https://github.com/sirreajohn/Tic_Tac_Toe_with_1_step_look_ahead_agent)

