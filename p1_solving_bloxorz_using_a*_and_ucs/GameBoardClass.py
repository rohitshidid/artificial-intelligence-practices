# Gameboard represented as a matrix class

class GameBoard:

    def __init__(self):  
        self.board = self.__GetBoard() # gameboard as a matrix (empty spaces removed)
        
    # returns current coordinate/s of the box
    def GetBoxCoordinates(self):

        boxCoordinates = []

        # append 'S' coordinates to box location
        for y in range(len(self.board)): 
            for x in range(len(self.board[y])):
                if self.board[y][x] == 'S':
                    boxCoordinates.append( (x,y) )

        return boxCoordinates

    def GetGoalCoordinates(self):
        for y in range(len(self.board)): 
            for x in range(len(self.board[y])):
                if self.board[y][x] == 'G':
                    return (x,y)
        
    # check if the given coordinate/s is/are valid for block to move
    def IsCoordinatesValid(self, coordinates):
        
        # Check for each coordinates
        for coordinate in coordinates:
            x,y = coordinate[0], coordinate[1]

            #if coordinates are out of the scope of the gameboard 
            if x < 0 or y < 0 or y >= len(self.board) or x >= len(self.board[0]) or self.board[y][x] == 'X':
                return False
        return True

    # Read the gameboard from a file and create a corresponding gameboard
    def __GetBoard(self):

        # open the gameboard file and read as lines

        fileName = input("Enter a valid file name : ")
        file = open(fileName,'r')
        lines = file.readlines()

        # extract "\n" from the gameboard rows
        for i in range(len(lines)):
            if lines[i][len(lines[i]) - 1] == "\n":
                lines[i] = lines[i][0:len(lines[i]) - 1]
        
        board = self.__FormattedBoard(lines) # remove empty spaces from the board representation
        return board

    # remove empty spaces from the board
    def __FormattedBoard(self, board):

        formattedBoard = []

        for line in board:

            line = line.replace(' ','') # remove empty spaces
            if line != '':
                formattedBoard.append(line)

        return formattedBoard      