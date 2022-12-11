# This is a template. 
# You should modify the functions below to match
# the signatures determined by the project specification


def sumvalues(values: list) -> int: #DONE 2 marks
    """Returns the sum of the values in the list
    Parameters - values : list
    Returns - sumofvalues : int
    """    
    sumofvalues = 0
    for num in values:
        if type(num) == int or type(num) == float:
            sumofvalues += num
        else:
            raise TypeError("The list contains non-numerical values")
    return sumofvalues

def maxvalue(values: list) -> int: #DONE 2 marks
    """Returns index of the maximum value in the list
    Parameters - values : list
    Returns - index of maximum values : int"""    
    maxvalue = values[0]
    maxindex = 0
    for i in range(1, len(values)):
        if type(values[i]) == int or type(values[i]) == float:
            if values[i] > maxvalue:
                maxvalue = values[i]
                maxindex = i
        else:
            raise TypeError("The list contains non-numerical values")
    return maxindex

def minvalue(values: list) -> int: #DONE 2 marks
    """Returns index of the minimum value in the list
    Parameters - values : list
    Returns - index of minimum values : int"""    
    minvalue = values[0]
    minindex = 0
    for i in range(1, len(values)):
        if type(values[i]) == int or type(values[i]) == float:
            if values[i] < minvalue:
                minvalue = values[i]
                minindex = i
        else:
            raise TypeError("The list contains non-numerical values")
    return minindex

def meannvalue(values: list) -> float: #DONE 2 marks
    """Returns mean average of the values in the list
    Parameters - values : list
    Returns - mean of values : float"""
    mean = sumvalues(values)/len(values)
    return mean

def countvalue(values: list, x: any) -> int: #DONE 2 marks
    """Returns occurrences of the value x in the list values
    Parameters - values : list, x : int/float
    Returns - occurrences of x : int"""  
    count = 0  
    for each in values:
        if each == x:
            count += 1
    return count
