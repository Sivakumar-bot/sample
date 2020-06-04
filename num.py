"""
Prints the numbers from 1 to N

if the number is multiples of three,print “Fizz” instead of the number 

and for the multiples of five print “Buzz”
"""
def num(n):
    """num fucntion accept only the Natural interger number(greater than 0)"""
    try:
        #check if the given number is Negative then it will raise Exception
        if n<=0 :
            raise TypeError 
        #iterate given number through the loop using range function
        for i in range(n):
            #checking the condition if "i" multiples of three
            if (i+1)%3==0:
                print("Fizz",end="," if (i+1)!=n else "")
                
            #checking the condition if "i" multiples of five
            elif (i+1)%5==0:
                print("Buzz",end="," if (i+1)!=n else "")
            else:
                print(i+1,end="," if (i+1)!=n else "")
    except :
        raise TypeError ("Please Enter the Natural interger number(greater than 0)")
        
if __name__=='__main__':
    num(17)
