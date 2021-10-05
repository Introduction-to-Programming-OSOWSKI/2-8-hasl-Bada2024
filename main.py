#WRITE YOUR CODE IN THIS FILE
def hasL(x):
    b=list(x)
    # get a list version of variable
    for i in range(0,len(b)):
    #if i (current number in the range) for each i in range of len b
        if b[i]=="l":
            #if the list of the array at the postion of i which is the number of times the function has looped around check if the is a letter l
                return True
                #if there is a l return true to the terminal
    return False 
#if no l is found in the variable b return false.
print(hasL("floating"))
        