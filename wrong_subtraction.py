import math 
import sys



def check_the_far_right_element(string_n):
    if string_n[len(string_n) - 1] == '0':
        return True
    else:
        return False



def main():
    #getting the inputs 
    n, k = map(int, input().split())
    #check my restrictions 
    if n < 2 or n > pow(10, 9) or k > 50 or k < 1:
        sys.exit('error please check restrictions')
    else:
        #while k > 0
        while(k > 0 and n > 0):
            #converting the number n to a string to use it as an array 
            string_n = str(n)
            if check_the_far_right_element(string_n):
                #it's a zero so we need to remove it 
                string_n = string_n[: -1]
                n = int(string_n)
            else:
                #it's a non-zero so we need to sub 1 from the number n 
                n -= 1
            k -= 1 
            
        print(n)
        

main()
