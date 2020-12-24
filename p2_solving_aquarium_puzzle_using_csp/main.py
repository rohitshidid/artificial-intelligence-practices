######################
######################
# Author: Alp Cihan 
# ####################
# #######################################################################
# # Solving Aquarium Puzzle using CSP (Constraint Satisfaction Problem) 
# #######################################################################
# ##########################################################################################################
# # Aquarium puzzle uses a rectangular grid of cells divided into blocks (called aquari-ums),               
# # with numeric clues on each row and column. 
# #
# # The aim is to fill some of the cells with water according to following rules:
# #
# # Rule1: The water level of a block should be the same across its full width.
# #
# # Rule2: A block can be filled up to a certain level, obeying the gravity law.
# #   If a cell in a block is filled with water, the cells below it should also be filled in that block.
# #
# # Rule3: The clues denote the number of filled cells in each row and column.
# ##########################################################################################################
############################################################################################################

# region Imports

from constraint import *

# endregion Imports

# region Functions

# region Helper Functions

# Print the values of the variables if there is a solution
def ViewFilledAquarium(problem, lenRow, lenCol, fileName):
    
    print("Searching for a solution (it may take some time)...")
    solution = problem.getSolution() # get the solution

    # If there is no solution
    if solution == None: 
        print("\nThere is no solution.\n")
        return

    # If there is a solution
    # Print the result to the terminal
    # Write the result into the "fileName + "output.txt"" file

    outputFileName = fileName[:fileName.rfind('.')] + "_solution.txt" # output file name
    outPutFile = open(outputFileName, "w") # open output file to write
    
    print("\nSolution (0 = empty, 1 = filled with water")
    outPutFile.write("Solution (0 = empty, 1 = filled with water)\n")
    row = ""

    for variable in range(lenRow*lenCol): # for each variable
        if variable % lenRow == 0 and variable != 0: # print row by row
            print(row) # print the row
            outPutFile.write(row+'\n') # write the row into the output file
            row = "" # reset the row

        row += str(solution[variable]) # add to the row

    print(row+'\n') # print the last row
    outPutFile.write(row) # write last row into the output file

    print('Solution has written into \''+outputFileName +'\'')
    outPutFile.close() # close the output file

# Return the aquarium matrix and clues
def Get_Aquarium():

    fileName = input("Enter name of the aquarium file: ") # get file name (ex: aquarium1.txt)

    aquarium = [] # aguarium as a matrix
    clueCol, clueRow = [],[] # column and row clues

    try: 
        aquariumFile = open(fileName, "r") # open file

        print('\nGetting the aquarium information...')

        lines = aquariumFile.readlines() # read lines

        clueCol = list(filter(lambda x: x != '', lines[0].replace('\n','').split(' ') )) # get column clue numbers as list
        lines = lines[1:] # remove 0th since it only contain column clue numbers

        # fill the aquarium matrix and get row clue numbers
        for line in lines:

            chars = line.replace('\n',' ').split(' ') # remove '\n' from the line and split by ' '

            # Get row clue of the line
            if chars[0] != '': # if first char of a line is not '', then it is row clue
                clueRow.append(chars[0])
                chars = chars[1:] # remove clueRow from the char
            
            row = list(filter(lambda x: x != '', chars)) # not '' characters are row information
            
            aquarium.append(row) # append row information to the aquarium matrix
        
        aquariumFile.close() # close the aquarium file

    except:
        print("File has not found.")

    clueCol = list(map(int, clueCol)) # string list to int list
    clueRow = list(map(int, clueRow)) # string list to int list
    
    return aquarium, clueCol, clueRow, fileName

# endregion Helper Functions

# region Variable Function

# Add variables to the problem
# variables = range(len(clueCol)*len(clueRow))
# aquarium[0][0] -> 0 and aquarium[len(clueRow)][len(clueCol)] -> len(clueCol)*len(clueRow)
def AddVariables(problem, aquarium, clueCol, clueRow):
    
    print('Adding the variables...')

    blockCount = len(clueCol) * len(clueRow) # there is #clueCol * #clueRow empty blocks
    problem.addVariables(range(blockCount), [1,0]) # 1 = filled, 0 = empty

# endregion Variable Function

# region Constraint Functions

# Add column clue and row clue constraints
# Each row should have clueRow 1
# Each column should have clueCol 1
def AddClueConstraints(problem, aquarium, clueCol, clueRow):

    blockCount = len(clueCol) * len(clueRow) # number of blocks

    # Add column Constraints
    for i in range(len(clueCol)):
        number = clueCol[i] # number of total 1 in ith column
        indexes = [i for i in range(i, blockCount,len(clueCol) )] # all indexes with column number = i
        problem.addConstraint(ExactSumConstraint(number), indexes) # sum of indexes (number of 1's) must be equal to clueCol[i] 
    
    # Add row Constraints
    for i in range(len(clueRow)):
        number = clueRow[i] # number of total 1 in ith row
        indexes = [i for i in range(i*len(clueCol), (i+1)*len(clueCol) )] # all indexes with row number = i
        problem.addConstraint(ExactSumConstraint(number),indexes) # sum of indexes (number of 1's) must be equal to clueRow[i] 

# add width constraints
# Rule1: The water level of a block should be the same across its full width.
# if there is no boundry between two consecutive variable with same row, their values must be equal
# compare a variable with its right variable
def WidthConstraints(problem, aquarium, variable, rowLen, columnLen):
    
    column = int(2*(variable%rowLen) + 1) # row of variable in aquarim matrix
    row = int(2*(variable - (variable%rowLen)) / rowLen + 1) # column of variable in aquarium matrix

    # if there is no boundry between variable and its left (variable - 1) then, value of variable must equal to value of variable - 1
    if aquarium[row][column + 1] == '.': # if variable is not the left most block and there is no boundry between variable and variable + 1
        problem.addConstraint(lambda x1, x2: x1 == x2, # value of variable and value of variable - 1 must be same
                             (variable, variable + 1) )

# add below constraints
# Rule2: If a cell in a block is filled with water, the cells below it should also be filled in that block.
# if there is no boundry between two consecutive variable with same column, their values must be equal
# compare a variable with its below variable
def BelowConstraints(problem, aquarium, variable, rowLen, columnLen):
    
    column = int(2*(variable%rowLen) + 1) # row of variable in aquarim matrix
    row = int(2*(variable - (variable%rowLen)) / rowLen + 1) # column of variable in aquarium matrix
    
    # if there is no boundry between variable its below (variable + columnCount) then, value of variable must equal to value of variable + columnCount
    if variable < rowLen*(columnLen - 1) - 1 and aquarium[row + 1][column] == '.': # if variable is not the bottom most block and there is no boundry between variable and variable + columnCount
        problem.addConstraint(lambda x1, x2: not (x1 == 1 and x2 == 0), # if variable's value is 1, below variables's value cannot be 0
                             (variable, variable + rowLen) )

# Add all constaints to the problem
def AddConstraints(problem, aquarium, clueCol, clueRow):
    
    print('Adding the constraints...')

    AddClueConstraints(problem, aquarium, clueCol, clueRow) # add Rule 3 constraints
    
    for variable in range(len(clueCol)*len(clueRow)): # for every variable
        WidthConstraints(problem, aquarium, variable, len(clueCol), len(clueRow)) # add Rule 1 consraints
        BelowConstraints(problem, aquarium, variable, len(clueCol), len(clueRow)) # add Rule 2 constraints

# endregion Constraint Functions
  
# endregion Functions
  
# region Main

problem = Problem() # problem object from constraint library

aquarium, clueCol, clueRow, fileName = Get_Aquarium() # get the aquarium matrix and the clues
 
if aquarium != []: # if aquarium file is valid

    AddVariables(problem, aquarium, clueCol, clueRow) # add variables of the problem

    AddConstraints(problem, aquarium, clueCol, clueRow) # add constraints of the problem

    ViewFilledAquarium(problem, len(clueCol), len(clueRow), fileName) # print the solution

print('Program ending...')

# endregion End Main