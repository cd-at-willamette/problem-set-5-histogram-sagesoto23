##################################################
# Name: Sage Soto
# Collaborators: N/A
# Estimate of time spent (hr): 35 min
##################################################

def is_magic_square(array:list[list[int]]) -> bool:     # Defining the function to calculate a magic square
    num = len(array)                                    # Variable to define the length of the array
    for row in array:                                   # For a row in the array
        if len(row) != num:                             # If the length of a row does not equal the length of the array
            return False                                # It is not a square; returns a False
    first_row_sum = 0                                   # Sum of the 1st row (used for other rows and diagonals)
    for value in array[0]:                              # For a value in the array starting from the first term
        first_row_sum += value                          # Sum of the first row is added to the calculated value
    for row in array:                                   # For a row in the array
        if sum(row) != first_row_sum:                   # If the sum of a row does not equal the sum of the 1st row
            return False                                # Returns a False
    for column in range(num):                                               # For a column in range of the length of the array
        if sum(array[row][column] for row in range(num)) != first_row_sum:  # If the sum of the array's rows or columns does not equal the sum of 1st row
            return False                                                    # Returns a False    
    if sum(array[i][i] for i in range(num)) != first_row_sum:               # If the sum of the array's left diagonal does not equal the sum of 1st row
        return False                                                        # Returns a False
    if sum(array[i][num-i-1] for i in range(num)) != first_row_sum:         # If the sum of the array's right diagonal does not equal the sum of 1st row
        return False                                                        # Returns a False
    return True                                         # If the given array has all equal sums, then it is a magic square (returns a True)

small = [[8,1,6],[3,5,7],[4,9,2]]                       # The given array 
print(is_magic_square(small))                           # Will either print True or False if the array follows the is_magic_square criteria
