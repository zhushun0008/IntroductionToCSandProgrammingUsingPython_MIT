x = (1, 2, (3, 'John', 4), 'Hi')
x[0]
x = [1, 2, [3, 'John', 4], 'Hi'] 
x[0]


def oddTuples(aTup):
    '''
    Write a procedure called oddTuples, which takes a tuple as input, and 
    returns a new tuple as output, where every other element of the input tuple 
    is copied, starting with the first one. So if test is the tuple 
    ('I', 'am', 'a', 'test', 'tuple'), then evaluating oddTuples on this input 
    would return the tuple ('I', 'a', 'tuple').
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    result = ()
    for i in range(len(aTup)) :
        if (i+1) % 2 != 0 :
            result += (aTup[i],)
    return result
    
    # Here is another solution to the problem that uses tuple 
    #  slicing by 2 to achieve the same result
    #return aTup[::2]
    
print(oddTuples(('I', 'am', 'a', 'test', 'tuple')))