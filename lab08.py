"""
A module with several recursive functions

Tricia Park, tp294
10/17/17
"""


# IMPLEMENT ALL OF THESE FUNCTIONS

def numberof(thelist, v):
    """
    Returns the number of times v occurs in thelist.
    
    Parameter thelist: The list to count from
    Precondition: thelist is a list of ints
    
    Parameter v: The value to count
    Precondition: v is an int
    """
    if len(thelist) == 0:
        return 0
    left = thelist[0]
    if left == v:
        count = 1
    else:
        count = 0
    right = numberof(thelist[1:],v)
    return count + right

def replace(thelist,a,b):
    """
    Returns a COPY of thelist but with all occurrences of a replaced by b. 
    
    Example: replace([1,2,3,1], 1, 4) = [4,2,3,4].
    
    Parameter thelist: The list to count from
    Precondition: thelist is a list of ints
    
    Parameter a: The value to replace
    Precondition: a is an int
    
    Parameter b: The value to replace with
    Precondition: b is an int
    """
    if len(thelist) == 0:
        return thelist
    left = thelist[0]
    if left == a:
        x = [b]
    else:
        x = thelist[0:1]
    right = replace(thelist[1:],a,b)
    return x + right


def remove_dups(thelist):
    """
    Returns a COPY of thelist with adjacent duplicates removed.
    
    Example: for thelist = [1,2,2,3,3,3,4,5,1,1,1]
    the answer is [1,2,3,4,5,1]
    
    Parameter thelist: The list to modify
    Precondition: thelist is a list of ints
    """
    new = []
    if len(thelist) <= 1:
        return thelist
    left = thelist[0:1]
    x = thelist[1:2]
    right = remove_dups(thelist[1:])
    if left == x:
        new = right
    else:
        new = left + right
    return new


def oddsevens(thelist):
    """
    Returns a COPY of the list with odds at front, evens in the back.
    
    Odd numbers are in the same order as thelist. Evens are reversed.
    
    Example: 
        oddsevens([3,4,5,6]) returns [3,5,6,4].
        oddsevens([2,3,4,5,6]) returns [3,5,6,4,2].
        oddsevens([1,2,3,4,5,6]) returns [1,3,5,6,4,2].
    
    Parameter thelist: The list to modify
    Precondition: thelist is a list of ints (may be empty)
    """
    # HINT: How you break up the list is important.  A bad division will
    # make it almost impossible to combine the answer together.
    # However, if you look at the examples in the specification you 
    # will see a pattern that should help you define the recursion.
    new = []
    if len(thelist) == 0:
        return thelist
    left = thelist[0:1]
    right = oddsevens(thelist[1:])
    if thelist[0] % 2 == 1:
        return left + right
    elif thelist[0] % 2 == 0:
        return right + left
