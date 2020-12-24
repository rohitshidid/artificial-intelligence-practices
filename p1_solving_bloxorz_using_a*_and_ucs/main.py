# Alp Cihan 24214

from NodeClass import Node, NodePQueue
from GameBoardClass import GameBoard
import time
from guppy import hpy

gameBoard = GameBoard() # game board object


# region Functions for UCS and A* algorithms

# Cost function creates cost for given coordinates (returns only child.cost() + 1 in our case)
def CostFunction(node):
    return node.GetCost() + 1

# Heuristic Function With Manhattan Distance / 1.5
def HeuristicFunction(node):

    goal = gameBoard.GetGoalCoordinates() # coordinate of goal

    distances = [] # since 2x1 surface represented as 2 coordinates, there can be 2 distance

    for coordinate in node.GetCoordinates():
        manhattanDis = abs (coordinate[0] - goal[0]) + abs (coordinate[1] - goal[1]) 
        heuristic = manhattanDis / 1.5
        distances.append(heuristic)

    return (min(distances)) # return min distance for a given box

# Successor State Function for given node
# Create all the alternative single moves for the box except returning to the previous state
def SuccessorStateFunction(node, visitedCoordinates, algorithm):

    coordinates = node.GetCoordinates() # get coordinates of the box for the given state
    x,y = coordinates[0][0], coordinates[0][1] # get (x,y)

    nextCoordinates = []
    successors = [] # successor nodes of the given node

    # Create coordinates of the successors
    # If box standing on 1x1 surface
    if len(coordinates) == 1:  
        nextCoordinates = [ [(x+1,y),(x+2,y)],    # next alternative coordinates of the box 
                             [(x,y-2),(x,y-1)],
                             [(x-2,y),(x-1,y)],
                             [(x,y+1),(x,y+2)] ] 
    
    # If box standing on 2x1 surface and horizontal to x axis
    elif len(coordinates) == 2 and (coordinates[0][1] == coordinates[1][1]):
        nextCoordinates = [ [(x+2,y)],            # next alternative coordinates of the box 
                             [(x,y-1),(x+1,y-1)],
                             [(x-1,y)],
                             [(x,y+1),(x+1,y+1)] ] 
    
    # If box standing on 2x1 surface and horizontal to y axis
    elif len(coordinates) == 2 and (coordinates[0][0] == coordinates[1][0]):
        nextCoordinates = [ [(x+1,y),(x+1,y+1)],    # next alternative coordinates of the box 
                             [(x,y+2)],
                             [(x-1,y),(x-1,y+1)],
                             [(x,y-1)]] 
    
    # filter out the invalid and visited coordinates
    nextCoordinates = list(filter(gameBoard.IsCoordinatesValid, nextCoordinates))
    nextCoordinates = list(filter(lambda x: visitedCoordinates.count(x) == 0, nextCoordinates)) 

    # create nodes for the given coordinates and add to the graph
    for coordinates in nextCoordinates:

        if algorithm == "UCS": # use cost function only for UCS
            newNode = Node(coordinates, CostFunction(node))
        elif algorithm == "AStar": # also use Heuristic Function for A*
            newNode = Node(coordinates, CostFunction(node), HeuristicFunction(node))

        newNode.SetParent(node)
        node.AddChild(newNode)

        successors.append(newNode)

    return successors

# Check if the node represents goal state or not
def GoalTest(node, gameBoard):
    
    # If block is at the goal coordinate and on it's 1x1 surface
    if (len(node.GetCoordinates()) == 1) and (node.GetCoordinates()[0] == gameBoard.GetGoalCoordinates()):
        return True
    return False

# Print the solution path
def PrintSolution(solutionPath):

    coordinates = []

    # get coordinates of the result path from root to node
    coordinates = list(map(lambda node: node.GetCoordinates(), solutionPath)) # take coordinates from the solution path nodes
    coordinates.reverse() # reverse the order in order to make it root coordinate to goal coordinate format
    
    # if there is no solution
    if len(coordinates) == 0: 
        print("There is no solution for the given problem!")
    
    # if there is a solution
    else: 
        print("Start:", coordinates[0]) # starting coordinate
        
        # print each step until reaching the goal
        for i in range(1,len(coordinates) - 1 ):
            print("Step"+str(i)+":",coordinates[i])
        
        print("Goal:", coordinates[len(coordinates)-1]) # goal coordinate

#endregion

# region UCS and A* implementations

# Note: There is no need for seperate AStar and UCS functions, only difference is passing either "AStar" or "UCS" while calling the SuccessorStateFunction.
# Implemented both of them just for readability issues.

# A*
def AStar():

    frontier = NodePQueue() # create frontier (node priority queue)
    visitedCoordinates = [] # track visited nodes to prevent infinite loops

    initNode = Node(gameBoard.GetBoxCoordinates(), 0, 0) # create initial node for initial state of the box

    frontier.insert(initNode) # add initial node to the frontier
    visitedCoordinates.append(initNode.GetCoordinates()) # add initial coordinates to visited coordinates

    # while frontier is not empty
    while not frontier.isEmpty():
        
        node = frontier.pop() # pop fron priority queue

        visitedCoordinates.append(node.GetCoordinates()) # add to visited coordinates

        # Check if node is the goal state
        if GoalTest(node, gameBoard):
            solutionPath = node.GetAllParents() # return the path from goal to the root node
            return solutionPath
        
        # Add succesors of the node to the frontier
        for successor in SuccessorStateFunction(node, visitedCoordinates, "AStar"):
            if(visitedCoordinates.count(successor.GetCoordinates())) == 0:
                frontier.insert(successor)
            
    
    return [] # if a solution does not exist

# UCS
def UCS():
    
    frontier = NodePQueue() # create frontier (node priority queue)
    visitedCoordinates = [] # track visited nodes to prevent infinite loops

    initNode = Node(gameBoard.GetBoxCoordinates(), 0, 0) # create initial node for initial state of the box

    frontier.insert(initNode) # add initial node to the frontier
    visitedCoordinates.append(initNode.GetCoordinates()) # add initial coordinates to visited coordinates
    
    # while frontier is not empty
    while not frontier.isEmpty():
        
        node = frontier.pop() # pop fron priority queue

        visitedCoordinates.append(node.GetCoordinates()) # add to visited coordinates

        # Check if node is the goal state
        if GoalTest(node, gameBoard):
            solutionPath = node.GetAllParents() # return the path from goal to the root node
            return solutionPath
        
        # Add succesors of the node to the frontier
        for successor in SuccessorStateFunction(node, visitedCoordinates, "UCS"):
            
            if(visitedCoordinates.count(successor.GetCoordinates())) == 0:
                frontier.insert(successor)
            
    
    return [] # if a solution does not exist

#endregion

# region Main function of the program

if __name__ == '__main__':

    # region Print solution and time for UCS 

    print("\nRESULT OF UCS\n-------------------------")

    tStart = time.time() # start time

    h = hpy()

    resultPath = UCS()

    if resultPath != []:
        print ("Memory:", (h.heap().size / 10**6.0), "MB") # print memory consuption of UCS in MB

        tEnd = time.time() # end time

        totalTime = tEnd - tStart # calculate the duration
        print("Time:", "{:.7f}".format(totalTime), "sec.\n") # print the duration

    PrintSolution( resultPath ) # print the solution path for UCS

    # endregion

    # region Print solution and time for A* 

    print("\nRESULT OF A*\n-------------------------")

    tStart = time.time() # start time

    h2 = hpy()
    resultPath = AStar()

    if resultPath != []:
        print ("Memory:", (h2.heap().size / 10**6.0), "MB") # print memory consuption of A* in MB

        tEnd = time.time() # end time
    
        totalTime = tEnd - tStart # calculate the duration
        print("Time:", "{:.7f}".format(totalTime), "sec.\n") # print the duration
        
    PrintSolution( resultPath ) # print the solution path for A*

    # endregion

#endregion