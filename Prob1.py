from pgl import *

#1a
def create_histogram_array(data:list[int]) -> list[int]:    # Defining a function that creates a list for histogram data
    new_list = [0 for num in range(max(data)+1)]            # List comprehension for data points in a list
    for value in data:                                      # For a value in the data
        new_list[value] += 1                                # A value is added to the list comprehension
    return new_list                                         # Returns the new list 

#1b
def print_histogram(hist:list[int]) -> None:                          # Defining the list that prints the histogram 
    [print(num,": ",hist[num] * "*") for num in range(len(hist))]     # List comprehension that prints out all columns with data points
        
#1c
def graph_histogram(hist:list[int], width:int, height:int) -> None:   # Defining a function that graphs the histogram
    gw = GWindow(width,height)                                        # Creating the graphics window for the histogram
    x = 0                                                             # Initial width of a single column (not created at this point)
    
    def my_rect(x,y,w,h,color):             # Defining the columns in the graphics window
        rect = GRect(x,y,w,h)               # A column's parameters
        rect.set_filled(True)               # Completely fill the column
        rect.set_color(color)               # Set color of the columns
        gw.add(rect)                        # Adds the columns to the screen
    
    for num in range(len(hist)):                                                  # For a number in range of the length of the histogram list
        my_rect(x,height-hist[num]*height//4,width//10,hist[num]*height,"Red")    # Places each column of the histogram from the hist list in the graohics window
        x += width//10                                                            # The width of each column in the histogram
    
# Some testing printouts for your use!
PI_DIGITS = [3,1,4,1,5,9,2,6,5,3,5,5,8,9,7,9]           # Given list of pi digits
hist = create_histogram_array(PI_DIGITS)                # The list of histogram values
print(hist)                                             # Print the histogram list
print_histogram(hist) # uncomment to test
graph_histogram(hist, 400, 400) # uncomment to test
