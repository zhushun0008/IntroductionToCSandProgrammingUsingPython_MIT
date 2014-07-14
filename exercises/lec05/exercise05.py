# -*- coding: utf-8 -*-
def iterPower(base, exp):
    '''
    returns: int or float, base^exp
    Write an iterative function iterPower(base, exp) that calculates the 
    exponential base^exp by simply using successive multiplication. 
    For example, iterPower(base, exp) should compute base^exp by multiplying base 
    times itself exp times. Write such a function below.
    (Use of the ** operator is not allowed)
    Inputs:
        base - can be a float or an integer
        exp - will be an integer ≥ 0
    Outputs:
        Return one numerical value. Your code must be iterative 
    '''
    # Your code here
    result = 1
    while exp > 0 :
        result *= base
        exp -= 1
    return result
    
def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    # Base case
    if exp == 0 :
        return 1
    # Otherwise, exp must be > 0, so return 
    #  base* base^(exp-1). This is the recursive case.
    else :
        return base * recurPower(base, exp - 1)        
        
        
def recurPowerNew(base, exp):
    '''
    base: int or float.
    exp: int >= 0
    
    returns: int or float; base^exp
    Another way to solve this problem just using multiplication (and remainder) 
    is to note that 
        base^exp=(base^2)^(exp/2)        if exp > 0 and exp is even
        base^exp = base * base^(exp-1)   if exp > 0 and exp is odd
        base^exp = 1                     if exp = 0
    Write a procedure recurPowerNew which recursively computes exponentials 
    using this idea.
    '''
    # Your code here      
    # Base case is when exp = 0
    if exp <= 0:
        return 1

    # Recursive case 1: exp > 0 and even
    elif exp % 2 == 0:
        return recurPowerNew(base*base, exp/2)

    # Otherwise, exp must be > 0 and odd, so use the second
    #  recursive case.
    return base * recurPowerNew(base, exp - 1)
    
    
def gcdIter(a, b):
    '''
    The greatest common divisor of two positive integers is the largest integer that divides each of them without remainder. For example,
        gcd(2, 12) = 2
        gcd(6, 12) = 6
        gcd(9, 12) = 3
        gcd(17, 12) = 1

    Write an iterative function, gcdIter(a, b), that implements this idea.
    One easy way to do this is to begin with a test value equal to the smaller 
    of the two input arguments, and iteratively reduce this test value by 1 
    until you either reach a case where the test divides both a and b without 
    remainder, or you reach 1.
    inputs: 
        a, b - positive integers
    outputs
        return a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    potentialDivisor = min(a,b)
    while potentialDivisor >= 1 :
        # Find the first common divosor
        if a % potentialDivisor == 0 and b % potentialDivisor == 0:
            return potentialDivisor
             
        potentialDivisor -= 1
        
    # Official solution
    #testValue = min(a, b)
    # Keep looping until testValue divides both a & b evenly
    # while a % testValue != 0 or b % testValue != 0:
    #     testValue -= 1
    #return testValue
    
def gcdRecur(a, b):
    '''
    A clever mathematical trick (due to Euclid) makes it easy to find greatest 
    common divisors. Suppose that a and b are two positive integers:
        If b = 0,
            then the answer is a
        Otherwise, 
            gcd(a, b) is the same as gcd(b, a % b)
            
    a, b: positive integers
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if b == 0 :
        return a
    else :
        return gcdRecur(b, a % b)
  
def lenIter(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    
    # Initialize a variable to hold our final count
    count = 0

    # Counting each char
    for char in aStr:
        count += 1
    return count
    
def lenRecur(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    Hint1
        String slicing may be useful in this problem...
    Hint2
        How would you check if a string is empty without using len()? 
        An easy way you can check if a string, s, is empty is to check the 
        condition
            s == '' 
    '''
    s = aStr
    if s == '' :
        return 0
    else :
        return 1 + lenRecur(aStr[1:])
    
    
def isIn(char, aStr):
    '''
    We can use the idea of bisection search to determine if a character is in 
    a string, so long as the string is sorted in alphabetical order.

    First, test the middle character of a string against the character you're 
    looking for (the "test character"). If they are the same, we are done - 
    we've found the character we're looking for!
    If they're not the same, check if the test character is "smaller" than 
    the middle character. If so, we need only consider the lower half of the 
    string; otherwise, we only consider the upper half of the string. 
    (Note that you can compare characters using Python's < function.)

    Implement the function isIn(char, aStr) which implements the above idea 
    recursively to test if char is in aStr. char will be a single character 
    and aStr will be a string that is in alphabetical order. The function 
    should return a boolean value.

    As you design the function, think very carefully about what the base cases 
    should be.
    Inouts:
        char - a single character
        aStr - an alphabetized string
    Outputs:
        returns: True if char is in aStr; False otherwise
    '''
    middleIndex = len(aStr)/2
    if aStr == '' :
        return False
    elif middleIndex > 0 :
        middleChar = aStr[middleIndex] 
        if char == middleChar:
            return True
        elif char < middleChar  :
            return isIn(char, aStr[:middleIndex]) 
        else :
            return isIn(char, aStr[middleIndex + 1 :])
    elif char == aStr[middleIndex]:
        return True
    else :
        return False
          
def semordnilap(str1, str2):
    '''
    str1: a string
    str2: a string
    
    returns: True if str1 and str2 are semordnilap;
             False otherwise.
    '''
    if len(str1) != len(str2) :
        return False
    if len(str1) == 1 :
        if str1 == str2 :
            return True
        else :
            return False
            
    if str1[0] != str2[-1] :
        return False
    else :
        return semordnilap(str1[1:], str2[:-1])
    
    
    
    
    
    
    
    
print('maximun common divisor is : ' + str(gcdIter(10,4)))
print('maximun common divisor is : ' + str(gcdRecur(10,4)))
print('length  is : ' + str(lenRecur('abc')))

print('length  is : ' + str(isIn('a', '')))