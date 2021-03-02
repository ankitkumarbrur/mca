def sumTwoNum(x,y):
    '''
    Returns the sum of two numbers or concatenate two strings

    Parameters:
        x : required
        y : required
    '''
    z=x+y       # calculating the sum
    return z    # returning sum
    
def sumList(list1,list2):
    '''
    Returns the sum of two lists

    Parameters:
        list1 : <list> required
        list2 : <list> required
    '''
    n = len(list2) if len(list1) >= len(list2) else len(list1)

    sum_List = []                   # empty list to store sum of lists 
    for i in range(n):              # loop to traverse every single element of list
        sum1 = sumTwoNum(list1[i],list2[i])     # using our sumTwoNUm to get summation of two numbers
        sum_List.append(sum1)       # appendending sum of two elements to sum_list

    sum_List += list1[n:]           # appending remaining item in the list of any left
    sum_List += list2[n:]           # appending remaining item in the list of any left

    return sum_List                 # returning the sum of the list

x = [1,2,3,8]
y = [1,2,3]

print(sumList(x,y))