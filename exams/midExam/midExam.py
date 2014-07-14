# __author__ = 'zhushun0008'

stuff = (["BB", "iPad"],)
for thing in stuff:
    if thing == 'iPad':
        print "Found it"


def Square(x):
    return SquareHelper(abs(x), abs(x))

def SquareHelper(n, x):
    if n == 0:
        return 0
    return SquareHelper(n-1, x) + x

print Square(0)



### Problem 04
def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    # Your Code Here
    if b > x :
        return 0
    else :
        return 1 + myLog(x/b,b)

print myLog(1, 2)
print myLog(16, 4)
print myLog(15, 3)
##############################################
#            Problem 05                      #
##############################################

# Suppose you are given two strings (they may be empty), s1 and s2. You would like to "lace" these strings together, by
# successively alternating elements of each string (starting with the first character of s1). If one string is longer than
# the other, then the remaining elements of the longer string should simply be added at the end of the new string.
# For example, if we lace 'abcd' and 'efghi', we would get the new string: 'aebfcgdhi'.
# Write an iterative procedure, called laceStrings(s1, s2) that does this.


def laceStrings(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length,
    then the extra elements should appear at the end.
    """
    # Your Code Here
    result = ""
    if s1 and s2 :
        stringIndex = 0
        lenS1 = len(s1)
        lenS2 = len(s2)
        while stringIndex < lenS1 and stringIndex < lenS2 :
            result = result + s1[stringIndex] + s2[stringIndex]
            stringIndex += 1
        if lenS1 < lenS2 :
            result += s2[stringIndex:]
        else :
            result += s1[stringIndex:]
    else :
        result = s1 + s2
    return result
print "laceStrings...."
print laceStrings('abcd', 'efghi')
print laceStrings('cyaouthg', 'vwts')
print laceStrings('', '')




def laceStringsRecur(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length,
    then the extra elements should appear at the end.
    """
    def helpLaceStrings(s1, s2, out):
        if s1 == '':
            return out + s2
        if s2 == '':
            return out + s1
        else:
            return helpLaceStrings(s1[1:],s2[1:],out + s1[0] + s2[0])
    return helpLaceStrings(s1, s2, '')

print "laceStringsRecur...."
print laceStringsRecur('abcd', 'efghi')
print laceStringsRecur('cyaouthg', 'vwts')
print laceStringsRecur('', '')



print "McNuggets...."

# def McNuggets(n):
#     """
#     n is an int
#
#     Returns True if some integer combination of 6, 9 and 20 equals n
#     Otherwise returns False.
#     """
#     # Your Code Here
#     package1 = 6
#     package2 = 9
#     package3 = 20
#     out = [0,0,0,False]
#     def McMuggetsCombination(package1,package2,package3, n, out) :
#
#         if n == 0 or n % package1 == 0 or n % package2 == 0 or n % package3 == 0:
#             out[3] = True
#             if n % package1 == 0 :
#                 out[0] += n / package1
#             elif n % package2 == 0 :
#                 out[1] += n / package2
#             else :
#                 out[2] += n / package3
#             return out
#         elif n < 0 :
#             out[3] = False
#             return out
#         else :
#             if n - package3 >= 0 :
#                 out[2] += 1
#                 return McMuggetsCombination(package1,package2,package3, n - package3, out)
#             elif n - package2 >= 0 :
#                 out[1] += 1
#                 return McMuggetsCombination(package1,package2,package3, n - package2, out)
#             else :
#                 out[0] += 1
#                 return McMuggetsCombination(package1,package2,package3, n - package1, out)
#
#     return McMuggetsCombination(package1,package2,package3, n, out)



def McNuggets(n):
    """
    n is an int

     Returns True if some integer combination of 6, 9 and 20 equals n
     Otherwise returns False.
    """
     # Your Code Here

    # package1 = 6
    # package2 = 9
    # package3 = 20
    # for i in range(n/package1 + 1) :
    #     for j in range(n/package2 + 1) :
    #         for k in range(n/package3 + 1) :
    #             if package1 * i + package2 * j + package3 * k == n :
    #                 return True
    # return False

    if n < 0 :
        return False
    else :
        return n % 6 == 0 or n % 9 == 0 or n % 20 == 0 or McNuggets(n - 6) or McNuggets(n - 9) or McNuggets(n - 20)



print McNuggets(15)



def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    # Your Code Here
    package1 = 6
    package2 = 9
    package3 = 20
    out = False
    def McMuggetsCombination(package1,package2,package3, n, out) :

        if n == 0 or n % package1 == 0 or n % package2 == 0 or n % package3 == 0:
            return True
        elif n < 0 :
            return False
        else :
            if n - package3 >= 0 :
                return McMuggetsCombination(package1,package2,package3, n - package3, out)
            elif n - package2 >= 0 :
                return McMuggetsCombination(package1,package2,package3, n - package2, out)
            else :
                return McMuggetsCombination(package1,package2,package3, n - package1, out)

    return McMuggetsCombination(package1,package2,package3, n, out)


print "sqrt...."

def fixedPoint(f, epsilon):
    """
    f: a function of one argument that returns a float
    epsilon: a small float

    returns the best guess when that guess is less than epsilon
    away from f(guess) or after 100 trials, whichever comes first.
    """
    guess = 1.0
    for i in range(100):
        if abs(f(guess) - guess) < epsilon:
            return guess
        else:
            guess = f(guess)
    return guess

a = 4
def sqrt(a):
    def tryit(x):
        return 0.5 * (a/x + x)
    return fixedPoint(tryit(a), 0.0001)

print sqrt(4)