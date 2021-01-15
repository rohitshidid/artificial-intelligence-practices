Solving Fox, Goose, and Bag of Beans Puzzle Using Planning
=================================
Represented the [Fox, Goose, and Bag of Beans Puzzle](https://en.wikipedia.org/wiki/Wolf,_goat_and_cabbage_problem) in [PDDL](https://en.wikipedia.org/wiki/Planning_Domain_Definition_Language) format and solved it using the [Fast Downward](http://www.fast-downward.org/HomePage) library.

## Table of Content

* [What is Fox, Goose, and Bag of Beans Puzzle?](#what-is-fox,-goose,-and-bag-of-beans-puzzle?)
* [Representation of the problem](#representation-of-the-problem)
* [The input of the program](#the-input-of-the-program)
* [The output of the program](#the-output-of-the-program)
* [How to run](#how-to-run)
* [License](#license)

## What is Fox, Goose, and Bag of Beans Puzzle?

Once upon a time a farmer went to the market and purchased a fox, a goose, and a bag of beans.

On his way home, the farmer came to the bank of a river and hired a boat.
But in crossing the river by boat, the farmer could carry only himself and a single one of his purchases—the fox, the goose, or the bag of beans. If left alone, the fox would eat the goose, and the goose would eat the beans.
The farmer’s challenge was to carry himself and his purchases to the far bank of the river, leaving each purchase intact.

How did he do it?

## Representation of the Problem
* [Problem](#problem)
    * [Objects](#objects)
    * [Initial State](#initial)
    * [Goal State](#goal)
* [Domain](#domain)
    * [Predicates](#predicates)
    * [Action](#action)
### Problem
#### Objects
 * farmer
 * fox
 * goose
 * beans

#### Initial
 Farmer, fox, goose, and beans are all on the left side of the river

#### Goal
 Farmer, fox, goose, and beans are all on the right side of the river

### Domain
#### Predicates: onLeft(x)
True if x is at the left side of the river else false
#### Action: cross(x)
The only action is crossing the river
##### Parameter:
x (x denotes which object is crossing the river)
##### Preconditions: 
1)	If the farmer is passing by itself, (goose and fox) and (goose and beans) should not stay on the same side.
2)	If the farmer is passing the beans, the fox and goose should not stay on the same side.
3)	If the farmer is passing the fox, beans and goose should not stay on the same side.
4)	If the farmer is passing the goose, it does not need to check any constrain.
##### Effects:
* Object x crosses to the opposite side of the river.
* If x is not the farmer, the farmer also crosses to the opposite side of the river with x.

## The input of the program
The input consists of two .pddl files. One for the [domain](#domain) (see [dom.pddl](./dom.pddl)), one for the [problem](#problem) (see [prob.pdll](./prob.pddl))
  
## The output of the program
The output file (see [sas_plan](./sas_plan)) that contains the steps of the solution (from initial state to goal state).

**Note:** Farmer is also crossing the river in each step.

Example: (cross beans) means: beans and farmer is crossing, (cross farmer) means: the farmer is crossing by himself.

## How to run
1) [Install Fast Downward](http://www.fast-downward.org/ObtainingAndRunningFastDownward) (to solve the puzzle after implementing domain and problem) 
2) Create [dom.pddl](./dom.pddl) and [prob.pddl](./prob.pddl) inside the downward folder.
3) Open the downward folder (which contains fast-downward.py) in the terminal.
4) Use the following command to run the program.

        $ ./fast-downward.py dom.pddl prob.pddl --search "lazy_greedy([ff()], preferred=[ff()])"
5) The program will create a [sas_plan](./sas_plan) which contains the solution.

## License
  
[MIT](../LICENSE)
