'''
Start off assuming we don't know Big-O notation.

algorithm is simply a procedure or formula for solving a problem!

'''

# First function
def sum1(n):
    '''
    Take an input of n and return the sum of the numbers from 0 to n

    '''
    final_sum = 0
    for x in range(n+1):
        final_sum += x

    return final_sum
