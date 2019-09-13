#  File: Spiral.py

#  Description: Program creates a 2D, square array of numbers spiraling outwards from the middle (starting at 1), and sums
#               all adjacent numbers to a given number within the square. The spiral dimensions and the numbers to use
#               for summation are given in a text document called 'spiral.txt', and sums are printed

#  Student Name: Mitchel Walker

#  Student UT EID: mlw3852

#  Course Name: CS 313E

#  Unique Number: 50725

#  Date Created: 1/28/19

#  Date Last Modified: 2/1/2019
import time
t0 = time.time()

def create_array(dim):
    #this function creates a 2-D square array number spiral
    #from the given dimension and return it
	
    #number (index) to determine the direction
    direction = 0
    #ints to hold the quantity of numbers left in the same direction
    count = 1
    current = count
    switch = False
    
    center = dim//2
    i = center
    j = center
    #initialize empty array
    arr = []
    for row in range(dim):
        column = []
        for col in range(dim):
            column.append(0)
        arr.append(column)
    #fill in values
    for num in range(dim**2):
        arr[i][j] = num +1  
        #increment i or j
        if direction == 0:
            #to the right
            j += 1
            current -= 1
        elif direction == 1:
            #downwards
            i += 1
            current -= 1
        elif direction == 2:
            #to the left
            j -= 1
            current -= 1
        elif direction == 3:       ####change this to else
            #upwards
            i -= 1
            current -= 1

        if current == 0:
            if switch == True:
                count += 1
            switch = not switch
            current = count
            direction = (direction+1)%4
    return arr
        
        
        



def get_sum(arr, num):
    #this function returns the sum of numbers surrounding
    #a given number in a given array and return it

    #find location of the number
    for i in range(len(arr)):
        if num in arr[i]:
            j = arr[i].index(num)
            break

    #sum numbers around it
    sm = set()
    for it_row in range(i-1,i+2):
        for it_col in range(j-1,j+2):
            if it_row!=i or it_col!=j:
                try:
                    sm.add(arr[abs(it_row)][abs(it_col)])
                except:
                    continue
    return sum(sm)


def main():
    #this function reads and operates spiral.txt then prints sum of
    #numbers surrounding the given numbers in spiral.txt
    spiral = open('spiral.txt','r')
    numbers = spiral.readlines()
    num = eval(numbers.pop(0).strip())
    for i in range(len(numbers)):
        numbers[i] = eval(numbers[i].strip())

    arr = create_array(num)
    for element in numbers:
        print(get_sum(arr, element))



main()


t1 = time.time()
print(t1-t0)



