import sys 

def find_max(a):
    max = a[0]
    for i in range(len(a)):
        #checking restriction over the value of the a elements
        if a[i] < 1 or a[i] > pow(10, 9):
            sys.exit('please check the restrictions')
        
        if a[i] >= max:
            max = a[i]
        
    return max 


def main():
    #getting the size n and the number k 
    n, k = map(int, input().split())

    #getting the array a 
    a = list(map(int, input().strip().split()))[:n] 

    #checking restrictions
    if n < 1 or n > 2*pow(10, 9) or k < 0 or k > n or len(a) != n:
        sys.exit('please check the restrictions')
    
    k_new = k  

    #loop over all x values to find one that fits 
    for x in range(10):
        # print('this is x from up top =', x)
        k_new = 0 
        started_counting = False
    
        for i in range(n):
            # print('this is intial i', i)
            # if k = 0 then this x fits our requirements and we're done 
            if a[i] <= x:
                # print('this is the old k =', k_new)
                # print('this is i =', i)
                # print('this is a[i] =', a[i])
                k_new += 1 
                started_counting = True
                #print('this is the new k =', k_new)
                
        #print('======NEW X CYCLE======')

        if k_new == k and started_counting == True:
            return x 
    
    else:
        return -1
      



print(main())