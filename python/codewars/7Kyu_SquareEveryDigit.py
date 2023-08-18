# Welcome. In this kata, you are asked to square every digit of a number and concatenate them.
# For example, if we run 9119 through the function, 811181 will come out, because 9 is 81 and 1 is 1. (81-1-1-81)
# Example #2: An input of 765 will/should return 493625 because 7 is 49, 6 is 36, and 5 is 25. (49-36-25)
# Note: The function accepts an integer and returns an integer.
# Happy Coding!

def square_digits(num):
    nums = []
    for i in str(num):
        nums.append(int(i)**2)
    result = ''.join(str(j) for j in nums)
    return(int(result))