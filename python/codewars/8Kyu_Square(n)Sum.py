#Complete the square sum function so that it squares each number passed into it and then sums the results together.
#For example, for [1, 2, 2] it should return 9 because 1^2+2^2+2^2=9.

def square_sum(numbers):
    #your code here
    number_sum = 0
    for num in numbers:
        number_sum += num**2
    return(number_sum)
    
square_sum([1, 2])