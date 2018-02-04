def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    
    1. Begin with test value equal to smaller of two input arg
    2. iteratively reduce test value by 1 until reach case where test divides both a and b without remainder
    '''
    testA = a
    testB = b
    if b > a:
        while testA > 0:
            if a % testA == 0 and b % testA == 0:
                return testA
            testA -= 1
    elif b < a:
        while testB > 0:
            if b % testB == 0 and a % testB == 0:
                return testB
            testB -= 1
        
print(gcdIter(17, 12))