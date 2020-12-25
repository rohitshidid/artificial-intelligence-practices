# TODO: check if the input is in the L format

##########################
# Min = Player, Max = AI #
##########################

# region Imports

from Board import Board # Game board
import copy
import random

# endregion Imports

def findPossibleLMoves(playerID):

    possibleBoards = []
    playerPos = board.getPlayerPosition # get all coordinates of the player

    row, column = len(board.getBoard()), len(board.getBoard()[0])

    # Check every possible moves for L and blocks
    # Note: It is not the most efficient nested loops. Just for readibilty issues.
    #       Instead, check only 4 position per L rotation and check block positions among empty grids only
    for y in range(row):
        for x in range(column):
            for blockID in ['A','B']: # block IDs
                for by in range(row):
                    for bx in range(column):
                        
                        # All possible L rotations
                        all_L_coordinate_combinations = [
                                                         [(x,y),(x+1,y),(x,y+1),(x,y+2)],
                                                         [(x,y),(x-1,y),(x,y+1),(x,y+2)],
                                                         [(x,y),(x,y+1),(x,y+2),(x+1,y+2)],
                                                         [(x,y),(x,y+1),(x,y+2),(x-1,y+2)],
                                                         [(x,y),(x+1,y),(x+2,y),(x+2,y-1)],
                                                         [(x,y),(x+1,y),(x+2,y),(x+2,y+1)],
                                                         [(x,y),(x,y+1),(x+1,y+1),(x+2,y+1)],
                                                         [(x,y+2),(x,y+1),(x+1,y+1),(x+2,y+1)],
                                                        ] 

                        # Check moves for each L rotation and block positions
                        for L_coordinates in all_L_coordinate_combinations:

                            board_temp = copy.deepcopy(board)
                            # If the move is possible add the result board to the possible boards list
                            if board_temp.move(playerID, L_coordinates, blockID, (bx,by)):
                                possibleBoards.append(board_temp)

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


def minimax():
    return 1

def aiMove(playerID, possibleMoves):
    bestScore = float('-inf')
    bestMove = None

    for move in possibleMoves:
        score = minimax()
        if score > bestScore:
            bestScore = score
            bestMove = move
            if bestScore == 1:
                break
    
    board.assign(bestMove)




    
# region Main

if __name__ == "__main__":
    
    global board # Current gameboard
    board = Board() 

    #Main game loop
    while True:

        # Check if player 2 wins
        possibleMovesPlayer1 = findPossibleLMoves('1')
        if(len(possibleMovesPlayer1) <= 0): # If no option left for the player 1, end the game
            print('Player 2 (AI) wins!')
            break

        playerMove('1') # Player 1's turn
        print(board)


        # Check if player 1 wins
        possibleMovesAI = findPossibleLMoves('2')
        if(len(possibleMovesAI) <= 0): # If no option left for the player 2, end the game
            print('Player 1 wins!')
            break
        
        aiMove('2', possibleMovesAI) # Player 2's turn
        print(board)

# endregion Main