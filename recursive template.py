
a = 100
b = 10

def recursive_divide(x,y, count=0): #base case is defined in the header
    if ( x >= y):
        x -= y
        count += 1
        return recursive_divide(x, y, count) #note use return when making the recursive function
    else:
        return count

print(recursive_divide(a,b))