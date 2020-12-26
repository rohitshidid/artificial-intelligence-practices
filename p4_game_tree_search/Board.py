# Board class to store the gameboard states

class Board:

    def __init__(self):
        self.board = self.__getBoard() # game board represented as a matrix
        self.row = len(self.board) # total row
        self.column = len(self.board[0]) # total column

        self.posPlayer1 = self.__getPlayerPosition('1')
        self.posPlayer2 = self.__getPlayerPosition('2')
        self.posBA = self.__getBlockPosition('A')
        self.posBB = self.__getBlockPosition('B')

    # region Public

    # Move the L and the block with given coordinates if possible
    def move(self, playerID, coordinates_L, blockID, coordinate_B):
        
        # Return false if any of the given coordinate are out of the gaming board
        '''
        if not self.__isInTheBoard(coordinates_L, coordinate_B):
            return False
        '''

        ####################### First try to move the L #######################

        # First check if move is valid or not
        for coordinate in coordinates_L:
            x,y = coordinate[0],coordinate[1]
            if self.board[y][x] != '.' and self.board[y][x] != playerID:
                return False # return false if move is not valid
        
        # Remove the player
        coordinates_init = [] # coordinates of the player before the move
    
        for c in range(self.column):
            for r in range(self.row):
                if self.board[r][c] == playerID:
                    coordinates_init.append((c,r)) # first get the coordinates
                    self.board[r][c] = '.' # then remove
                if self.board[r][c] == blockID:
                    block_coor_init = (c,r)


        # Check if the new position of the L is different than initial coordinates
        count = 0
        for init in coordinates_init:
            for new in coordinates_L:
                if init == new:
                    count += 1
        if count == len(coordinates_L): # if coordinates has not changed return false
            return False

        
        # replace the player
        if playerID == '1':
            self.posPlayer1 = []
        else:
            self.posPlayer2 = []
        for coordinate in coordinates_L:
            self.board[coordinate[1]][coordinate[0]] = playerID
            if playerID == '1':
                self.posPlayer1.append(coordinate)
            else:
                self.posPlayer2.append(coordinate)

        ####################### Then try to move the block #######################

        # If block position is valid remove the block from previous position and replace in new position
        if self.board[coordinate_B[1]][coordinate_B[0]] == '.':

            self.board[block_coor_init[1]][block_coor_init[0]] = '.' # remove the block from its previous position
            self.board[coordinate_B[1]][coordinate_B[0]] = blockID # add the block to the new position
            if blockID == 'A':
                self.posBA = coordinate_B
            else:
                self.posBB = coordinate_B
            return True
        else:
            return False
    
    # Assignment overload (not sure if its the best practice in python)
    def assign(self, newBoard):
        self.board = newBoard.getBoard()

    # Print overload
    def __str__(self):

        strBoard = ""

        for row in self.board:
            for column in row:
                strBoard += column + ' '
            strBoard += '\n'


        return strBoard

    # endregion Public


    # region Getters

    def getBoard(self):
        return self.board

    def getPlayerPosition(self, playerID):
        if playerID == '1':
            return self.posPlayer1
        else:
            return self.posPlayer2

    def getBlockPosition(self, blockID):
        if blockID == 'A':
            return self.posBA
        else:
            return self.posBB

    # endregion Getters


    # region Private 

    # Get board from the user
    def __getBoard(self):

        board = []

        fileName = input("Enter the path of the game board (ex: board.txt): ")
       
        while True: # repeat until valid file name is entered
            try:
                boardFile = open(fileName,'r')
                break                             
            except IOError:
                fileName = input("Could not open file! Press Enter to retry: ")

        lines = boardFile.readlines()

        # extract "\n" from the gameboard rows
        for line in lines:
            line = line.replace("\n","") # remove "/n" 
            board.append(line.split(' '))

        return board
    
        # Return all 4 coordinates of the player  
    
    def __getPlayerPosition(self, playerID):
        coordinates = []
        for r in range(len(self.board)):
            for c in range(len(self.board[0])):
                if self.board[r][c] == playerID:
                    coordinates.append((r,c))
        return coordinates

    def __getBlockPosition(self, blockID):
        for r in range(len(self.board)):
            for c in range(len(self.board[0])):
                if self.board[r][c] == blockID:
                    return (c,r)

    # Check if the given L and block coordinates are on the game board
    def __isInTheBoard(self, coordinates_L, coordinate_B):
        
        # Check Block
        x,y = coordinate_B[0], coordinate_B[1]
        if x < 0 or x > self.column - 1:
            return False
        if y < 0 or y > self.row - 1:
            return False

        # Check L
        for coordinate in coordinates_L:
            x,y = coordinate[0], coordinate[1]
            if x < 0 or x > self.column - 1:
                return False
            if y < 0 or y > self.row - 1:
                return False

        return True
        
    # endregion Private
        
    