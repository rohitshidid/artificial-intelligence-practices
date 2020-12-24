Solving Bloxorz using A* and UCS
=================================
Implementation of [A*](https://en.wikipedia.org/wiki/A*_search_algorithm) and [UCS](https://www.educba.com/uniform-cost-search/) algorithms to solve the early stages of the Bloxorz Puzzle and make performance comparison.

## Table of Content
* [What is Bloxorz](#table-of-content)
* [Input of the problem](#input-of-the-problem)
* [Output of the problem](#output-of-the-problem)
* [How to run](#how-to-run)
* [License](#license)

## What is Bloxorz?

Bloxorz is a game where the goal is to drop a 1×2×1 block through a hole in the middle of a board without falling off its edges. Block can only move by making vertical or horizontal rolls.

The game is available at [coolmath games](http://www.coolmath-games.com/0-bloxorz/index.html.).

## Input of the problem
The input game board of size m×n is represented by a matrix
of size m × n where:

- O denotes safe tiles: the block can stand on these anytime;
- X denotes empty tiles: the block may never touch an empty tile, even if half of the block is on a safe tile;
- S denotes the tile(s) occupied by the block: if the block is in the vertical orientation then there is one tile labeled S, otherwise (if the block is in the horizontal orientation) there are two adjacent tiles labeled S;
- G denotes the goal tile: the block needs to be on it (vertically) to fall into the goal.

The matrix (see board2.txt) below represents the game board depicted in Figure 1:

    OOOXXXXXXX

    OOOOOOXXXX

    OOOSOOOOOX

    XOOSOOOOOO

    XXXXXOOGOO

    XXXXXXOOOX

<p align="center">
  <img width="633" alt="Screen Shot 2020-12-23 at 23 16 51" src="https://user-images.githubusercontent.com/37274614/103076211-4190d880-45de-11eb-8d1a-83dcae5667cc.png">
</p>

## Output of the problem
The shortest sequence of legal states that navigate the block from its given initial location into the goal.

## How to run
1) Install [guppy](https://pypi.org/project/guppy/) (to view the memory usage) 
```python
pip install guppy
```
2) Run main.py 
3) Enter the path of the file which contains the gameboard. (ex: board2.txt)

## License
  
[MIT](../LICENSE)
