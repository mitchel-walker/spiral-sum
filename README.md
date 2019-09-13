# spiral-sum

This is a simple program that first creates a 2D, square array of numbers spiraling outwards from the middle, and starts counting at 1. It builds the array from a given dimension, s, which represents an s x s 2d array. For there to be a 'middle', s must be odd. 

Next, given a particular number, n, within the array, the program sums all adjacent numbers to n, including diagonally adjacent numbers. The sum does not wrap around to the other side of the square. For example, if n lies on the edge of the square, it will only sum numbers above, below, and to the left of n (again, including diagonals).

The program must be first given the dimensions of the square, and can then handle several numbers, n, to calculate the 'adjacent sum'. All given values (i.e. spiral dimensions, the numbers n) must be given in a text document called 'spiral.txt', containing only number ascii values and newline characters fo delimit the values. The format of the text document is as follows:

s
n1
n2
.
.
.
nk

All given 'n' values must reside within the array (i.e. n < s^2). For every given 'n', the adjacent sum is printed on a new line.
