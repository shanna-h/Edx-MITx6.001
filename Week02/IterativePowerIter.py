def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    
    result = 1
    while exp > 0:
        exp -= 1
        result = result*base
    return result
        
print(iterPower(4, 3))      