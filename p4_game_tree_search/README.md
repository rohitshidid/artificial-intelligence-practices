Game Tree Search
=================================
Implementation of the [Alpha–beta pruning](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning#:~:text=Alpha%E2%80%93beta%20pruning%20is%20a,%2C%20Go%2C%20etc.) algorithm to create a two-player zero-sum game that the player play against the AI.

## Table of content
* [The game rules](#the-game-rules)
* [Representation of the game](#representation-of-the-game)
* [How to run](#how-to-run)
* [TODO](#todo)
* [License](#license)

## The game rules

Consider a two-player zero-sum game played on a 4 × 4 board that contains two L-shaped pieces, each L-piece belonging to one player only, and two square pieces that can be used by any of the players, as in the figure below:
<p align="center">
  <img width="155" alt="Screen Shot 2021-01-13 at 16 08 45" src="https://user-images.githubusercontent.com/37274614/104456397-a629cc80-55b9-11eb-9fcb-f0900e493428.png">
</p>
When a player’s turn comes, she must lift her L-shaped piece from the board and put it back into a different position so that the piece is entirely on the board, but it does not overlap with any other game piece. After the L-shaped piece has been placed on the board again, exactly one of the two square pieces must be moved to an empty square on the board. This completes the player’s move. For instance, suppose that the red L-shaped piece is owned by Player 1. If it is Player 1’s turn to move, one of the possible valid moves from the configuration above is shown in the figure below:
<p align="center">
  <img width="160" alt="Screen Shot 2021-01-13 at 16 12 29" src="https://user-images.githubusercontent.com/37274614/104456731-294b2280-55ba-11eb-9e22-8fb43bcbaf5e.png">
</p>

## Representation of the game
The input game board of size 4×4 is represented by a matrix
of size 4×4 where:

- **Dot (.)** represents the empty grids

- **1** represents the red L (L of the player 1)

- **2** represents the green L (L of player 2)

- **A** represents the blue block

- **B** represents the red block


Here is an example: (see [board2.txt](./board2.txt))

<p align="center">
  <img width="155" alt="Screen Shot 2021-01-13 at 16 08 45" src="https://user-images.githubusercontent.com/37274614/104456397-a629cc80-55b9-11eb-9fcb-f0900e493428.png">
</p>

    . 1 2 .
    
    . 1 2 .
    
    1 1 2 2
    
    . A B .

## How to run
1) Create a txt file that contains the game board representation as a matrix.
2) Run [main.py](./main.py)
3) Follow the instructions during the game.

## TODO
1) At the minimax function, instead of creating all children (all possible moves from the current state) of the current node at once, create them iteratively. Since most probably not all of them will get examined due to the alpha–beta pruning.

## License
  
[MIT](../LICENSE)
