# q) TYPE1: given column is 3 and row is 4 find pascal traingle element?

# T.C => O(n) and S.C => O(n)

# BRUTE force
def factorial(x):
    if x==1 or x==0:
        return 1
    fact = x*factorial(x-1)
    return fact

def find_element(C,R):
    n = R-1
    r = C-1
    value = factorial(n)/(factorial(r)*factorial(n-r))
    print(value)
    
find_element(3,4)
    
    
    
    
# q) TYPE2: print nth row of pascal triangle

def print_nth_row(n):
    ans = 1
    print(ans)
    for i in range(n):
        ans = ans*(n-i)/i
        print(ans)
    

                          