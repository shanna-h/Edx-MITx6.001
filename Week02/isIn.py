def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
   # Finding middle of string
    midStr = int((len(aStr)/2))
   
   # Base case - string length 1 or 0
    if len(aStr) <= 1:
        if char == aStr:
            return True
        else:
            return False

    elif char == aStr[midStr]:
        return True
        
    elif char < aStr[midStr]:
        return isIn(char, aStr[0:midStr])
    else:
        return isIn(char, aStr[midStr:])
        
print(isIn('z', 'abcdefghijklmno'))