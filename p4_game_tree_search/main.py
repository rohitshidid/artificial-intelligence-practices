##########################
# Min = Player, Max = AI #
#   ID = '1'     ID = '2'
##########################

# region Imports

from Board import Board # Game board
import copy
import random

# endregion Imports
allCoordinates = [(0,0),(0,1),(0,2),(0,3),(1,0),(1,1),(1,2),(1,3),(2,0),(2,1),(2,2),(2,3),(3,0),(3,1),(3,2),(3,3)]

nextMove = None # Next move of the AI

def updateNextMove(move):
    global nextMove
    nextMove = copy.deepcopy(move)

# Return L coordinates for the given (x,y) and rotation number
def getLByRotation(x,y,rotation):

    if rotation == 0:
        return [(x,y),(x+1,y),(x,y+1),(x,y+2)]
    elif rotation == 1:
        return [(x,y),(x-1,y),(x,y+1),(x,y+2)]
    elif rotation == 2:    
       return [(x,y),(x,y+1),(x,y+2),(x+1,y+2)]
    elif rotation == 3:
        return [(x,y),(x,y+1),(x,y+2),(x-1,y+2)]
    elif rotation == 4:
        return [(x,y),(x+1,y),(x+2,y),(x+2,y-1)]
    elif rotation == 5:
        return [(x,y),(x+1,y),(x+2,y),(x+2,y+1)]
    elif rotation == 6:
        return [(x,y),(x,y+1),(x+1,y+1),(x+2,y+1)]
    elif rotation == 7:
        return [(x,y),(x,y+1),(x+1,y),(x+2,y)]      

# Find possible moves of playerID from the given parentBoard
def findPossibleLMoves(playerID, parentBoard, isAllResults):

    # If parent board is empty, return
    if parentBoard == []:
        return []
    
    # ranges of each L rotation
    ranges = [
        ([0,1,2],[0,1]), # [(x,y),(x+1,y),(x,y+1),(x,y+2)]
        ([1,2,3],[0,1]), # [(x,y),(x-1,y),(x,y+1),(x,y+2)]
        ([0,1,2],[0,1]), # [(x,y),(x,y+1),(x,y+2),(x+1,y+2)]
        ([1,2,3],[0,1]), # [(x,y),(x,y+1),(x,y+2),(x-1,y+2)]
        ([0,1],[1,2,3]), # [(x,y),(x+1,y),(x+2,y),(x+2,y-1)]
        ([0,1],[0,1,2]), # [(x,y),(x+1,y),(x+2,y),(x+2,y+1)]
        ([0,1],[0,1,2]), # [(x,y),(x,y+1),(x+1,y+1),(x+2,y+1)]
        ([0,1],[0,1,2]), # [(x,y),(x,y+1),(x+1,y),(x+2,y)]  
                ]
    possibleBoards = []

    # Check every possible moves for L and blocks

    rotation = 0
    for rangeXY in ranges:
        rangeX = rangeXY[0]
        rangeY = rangeXY[1]
        for y in rangeY:
            for x in rangeX:
                checkBlocks = True
                for blockID in ['A','B']: # block IDs
                    L_coordinates = getLByRotation(x,y,rotation)
                    L2_coordinates = parentBoard.getPlayerPosition('1' if playerID == '2' else '2') # coordinate of other player

                    # Find empty coordinates that block can be replaced
                    emptyCoordinates = list(filter(lambda x: x not in L_coordinates and
                                                            x not in L2_coordinates and
                                                            x != parentBoard.getBlockPosition('A') and
                                                            x != parentBoard.getBlockPosition('B')
                                                            , allCoordinates))

                    for emptyCoordinate in emptyCoordinates:
                        board_temp = copy.deepcopy(parentBoard)
                            
                        # If the move is possible add the result board to the possible boards list
                        if board_temp.move(playerID, L_coordinates, blockID, emptyCoordinate):
                            possibleBoards.append(board_temp)
                        # If move is not possible no need to check for other blocks positions with same L
                        else: 
                            checkBlocks = False # stop checking for the other block
                            break # stop checking for the given block
                    

                    if checkBlocks == False:
                        break


        rotation += 1
    return possibleBoards

def playerMove(playerID):

    validMove = False

    # Get a valid input from the user
    while not validMove:

        print('\nEnter new L position ((0,0) is top left)')

        # Get L move
        new_L_coordinates = []
        for i in range(1,5):
            x = int(input('L x' + str(i) + ': '))
            y = int(input('L y' + str(i) + ': '))
            
            new_L_coordinates.append((x,y))
        
        # Get block move
        blockID = input('Enter ID of the block to move (ex: A): ')
        print('Enter new box position ((0,0) is top left)')
        bx = int(input('x: '))
        by = int(input('y: '))

        # If move is possible, move
        if copy.deepcopy(board).move(playerID, new_L_coordinates, blockID, (bx,by)):
            board.move(playerID, new_L_coordinates, blockID, (bx,by))
            validMove = True
        else:
            print("Invalid move, please try again.")

# evaluation function of the given position by its childs
def evaluation(childs, playerID):
    if childs != []:
        return 0
    elif playerID == '1':
        return 1
    else:
        return -1

# minimax with alpha-beta pruning
def minimax(currentBoard, depth, alpha, beta, playerID):

    childs = findPossibleLMoves(playerID, currentBoard, False) # find childs

    if depth == 0 or childs == []:
        return evaluation(childs, playerID)
    
    # If maximizing player
    if playerID == '2':
        maxEval = float('-inf')
        childs = findPossibleLMoves(playerID, currentBoard, True)
        for child in childs:
            newEval = minimax(child, depth-1, alpha, beta, '1')
            maxEval = max(maxEval, newEval)
            if (maxEval == newEval):
                updateNextMove(child)
            alpha = max(alpha, newEval)
            if beta <= alpha:
                break
        return maxEval
    
    # If minimizing player
    elif playerID == '1':
        minEval = float('+inf')
        childs = findPossibleLMoves(playerID, currentBoard, True)
        for child in childs:
            newEval = minimax(child, depth-1, alpha, beta, '2')
            minEval = min(minEval, newEval)
            beta = min(beta, newEval)
            if beta <= alpha:
                break
        
        return minEval

def aiMove(playerID, possibleMoves):

    print('AI is deciding... (It usually takes 20sec.)')
    score = minimax(board, 2, float('-inf'), float('inf'), '2')

    board.assign(nextMove)

# region Main

if __name__ == "__main__":
    global board # Current gameboard
    board = Board() 

    moves = findPossibleLMoves('1', board, True)

    #Main game loop
    while True:

        # Check if player 2 wins
        possibleMovesPlayer1 = findPossibleLMoves('1', board, True)
        if(len(possibleMovesPlayer1) <= 0): # If no option left for the player 1, end the game
            print('Player 2 (AI) wins!')
            break

        playerMove('1') # Player 1's turn

        print('\nPlayer 1 moved.\nBoard:')
        print(board)

        # Check if player 1 wins
        possibleMovesAI = findPossibleLMoves('2', board, True)
        if(len(possibleMovesAI) <= 0): # If no option left for the player 2, end the game
            print('Player 1 wins!')
            break
        
        aiMove('2', possibleMovesAI) # Player 2's turn
        print('Player 2 moved.\nBoard:')
        print(board)
        
# endregion Main