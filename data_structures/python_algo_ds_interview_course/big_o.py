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

print(sum1(10))

def sum2(n):
    '''
    Takes an input of n and sums numbers from 0 to n
    '''
    return (n*(n+1)) / 2

print(sum2(10))
assert sum2(10) == 55

'''
=======================
Start of Big-O Notation
=======================


'''
