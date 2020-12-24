Solving Aquarium Puzzle Using CSP
=================================
Represented Aquarium Puzzle as a [Constraint Satisfaction Problem](https://en.wikipedia.org/wiki/Constraint_satisfaction) and solved it using the [constraint](https://pypi.org/project/python-constraint/) library.

## Table of Content

* [What is Aquarium Puzzle?](#what-is-aquarium-puzzle?)
* [CSP representation of the aquarium puzzle](#csp-representation-of-the-aquarium-puzzle)
* [Input of the program](#input-of-the-program)
* [Output of the program](#output-of-the-program)
* [How to run?](#how-to-run?)
* [License](#license)

## What is Aquarium Puzzle?

Uses a rectangular grid of cells divided into blocks (called aquariums), with numeric clues on each row and column. with water according to the following rules:

**The aim is to fill the specified amount of cells with water according to the following rules:**
1) The water level of a block should be the same across its full width.
2) A block can be filled up to a certain level, obeying the gravity law. If a cell in a block is filled with water, the cells below it should also be filled in that block.
3) The clues denote the number of filled cells in each row and column.

For instance, an instance of this puzzle, and its solution are presented in **Figure (a)** and **Figure (b)** respectively.

<p align="center">
  <img width="500" alt="Screen Shot 2020-12-24 at 12 05 02" src="https://user-images.githubusercontent.com/37274614/103077161-4c4c6d00-45e0-11eb-991a-74c2a109c609.png">
</p>


## CSP representation of the aquarium puzzle
* [Variables](#variables)
* [Domain](#domain)
* [Constraints](#constrains)
  * [Constraint 1](#constraint-1)
  * [Constraint 2](#constraint-2)
  * [Constraint 3](#constraint-3)

### Variables:
 
{0,1,2,3…n} where n is ((# of cells in the puzzle) – 1).

### Domain:
 {0,1} 1 to represent filled cell, 0 to represent empty cell.

### Constraints:
Represented the problem with 3 constraints.

- Vij is a representation of a variable in the aquarium matrix. (i’th row and j’th column)
#### Constraint 1
**Rule:** Sum of 1’s in a row must be equal to the clue of the row and the sum of 1’s in a column must be equal to the clue of the column.
ESCi (RCi, {Vi0, Vi1 …, Vic}) 	 i ∈ {0,1,…, r},
ESCj (CCj, {V0j, V1j …, Vrj }) 	 j ∈ {0,1,…, c}

- c is (#variable in a column – 1) and r is (#variable in a row - 1)

- ESCi (a,b) is an exact sum constraint for i’th row. Where sum of every variable in set b = a

- ESCj is an exact sum constraint for j’th column. Where sum of every variable in set b = a

- RCi is row clue of i’th row.
-	CCj is column clue of j’th column. 
#### Constraint 2
**Rule:** For a given row, the value of every variable must be equal to the value of a variable at its right, if there is no border(x) between those two variables.	
     EQi (Vix,Vi(x+1))	x ∈ {columns of variable in i’th row, that has no border at its right}.                                                            	
-	r is (#variable in a row - 1)
-	EQi is an equal constraint for i’th row.
#### Constraint 3

**Rule:** For a given column, if a value of the variable is 1 and there is no border(x) below then, the value of the variable above also must be 1.	
Reminder: Since aquarium_matrix[0][0] is top left instead of bottom left, below of a cell in the puzzle means, larger row.
EQj (Vyj, V(y+1)j)		

-	c is (#variable in a column – 1)
-	EQj is an equal constraint for j’th column.

## Input of the program
The input puzzle is represented by a matrix where:

- **x** denotes borders
- **0** denotes empty blocks that can be filled with water
- **.** denotes no border
- **Horizontal and vertical numbers** denotes how many blocks will be filled for the given row/column.

The matrix (see [aquarium1.txt](./aquarium1.txt)) below represents the game board depicted in **Figure (a)**:

        3   5   1   4   3   2

      x x x x x x x x x x x x x

    1 x 0 x 0 x 0 . 0 . 0 . 0 x

      x . x . x x x x x x x . x

    1 x 0 x 0 x 0 . 0 . 0 x 0 x

      x . x x x . x x x x x . x

    2 x 0 . 0 . 0 x 0 . 0 x 0 x

      x . . . . . x . x x x . x

    4 x 0 . 0 . 0 x 0 x 0 . 0 x

      x x x . x x x . x . . . x

    5 x 0 x 0 x 0 x 0 x 0 . 0 x

      x . x . x . x . x . . . x

    5 x 0 x 0 x 0 x 0 x 0 . 0 x

      x x x x x x x x x x x x x
  

## Output of the program
The output of the program is a .txt file that denotes values of the grids in the following format (see [aquarium1_solution.txt](./aquarium1_solution.txt)) which denotes **Figure (b)**)

    Solution (0 = empty, 1 = filled with water)

    010000

    010000

    000110

    111100

    110111

    110111

## How to run?
1) Install [constraint](https://pypi.org/project/python-constraint/) (to solve the puzzle after representing it as a CSP) 
```python
pip install python-constraint
```
2) Run main.py 
3) Enter the path of the file which contains the puzzle. (ex: aquarium1.txt)

## License
  
[MIT](../LICENSE)
