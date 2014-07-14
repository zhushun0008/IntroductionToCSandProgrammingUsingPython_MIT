# -*- coding: utf-8 -*-
def firstLongestAlphabeticalSubtrings(orignalString) :
    """
    Return the first longest subtring in which the letters occur 
    in alphabetical order.
    inputs:
        orignalString - a tring of the lower case
    outputs：
       subString - the first longest subtring in orignalString 
    """   
    if not orignalString.islower() :
        print('Please input lower case string!')
        return None
    subStringLength  = orignalStringLength = len(orignalString)
    subString = None
    while subStringLength >= 0 :
        startIndex = 0
        endIndex = subStringLength
        while endIndex <= orignalStringLength :
            tempSubtring = orignalString[startIndex:endIndex]
            if isAlphabeticalOrder(tempSubtring):
                subString = tempSubtring
                return subString
            startIndex += 1
            endIndex += 1
        subStringLength -= 1
    return None
    
def isAlphabeticalOrder(originalString):
    if originalString == None :
        print('This is not a string')
        return False
    currentIndex = len(originalString) - 1
    preIndex = currentIndex - 1
    while preIndex >= 0:
        if originalString[currentIndex] < originalString[preIndex] :    
            return False
        currentIndex -= 1
        preIndex -= 1   
    return True
    
s1 = 'azcbobobegghakl'
s2 = 'abcbcd'
print('Longest substring in alphabetical order is: ' + firstLongestAlphabeticalSubtrings(s1))
print('Longest substring in alphabetical order is: ' + firstLongestAlphabeticalSubtrings(s2))