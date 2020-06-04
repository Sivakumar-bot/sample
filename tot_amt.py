"""
Accept Dictionary, names as keys and amount paid by each of them as interger Values
then Return the amount of values
"""
def tot_amt(val):
        if type(val)==dict:
            for i in val.values():
                if type(i) is not int :
                     raise TypeError("Please Enter integer Dictionary values")
                else:
                    #get the amount from dict using values function
                    #Total the amount using sum function
                    return sum(val.values())
        else:
             raise TypeError("Please Enter the Dictionary type sequence")

            
    