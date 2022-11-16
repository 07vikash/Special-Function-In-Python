"""Syntax====>   varname=filter(FunctionName,Iterable_Object)
   How it's work--> The execution process of filter() is that 'Each Values of Iterable object sends to Function Name.
   If the function return True then the element will be filtered.If the function returns false then that element will
   be neglected'. This process will be continue until all element of Iterable Object completed.
"""
print("""Q1--> Write a Python Program which sort of the original list of digits 
      and separate them into two different list as positive list and negative list?""")
print("="*50+"Using Normal Funtion"+"="*50)
# programmer Function
def pnum(n):
    if n>0:
        return True
    else:
        return False
def pneg(n):
    if n<0:
        return True
    else:
        return False

#main program
lst=[10,25,95,-25,-65,84,-65,58,-55]
P_Number=list(filter(pnum, lst))
N_Number=list(filter(pneg, lst))
print("\tPositive Numbers in lst are={}".format(P_Number))
print("\tNegative Number in lst are={}".format(N_Number))

print("="*50+"Using Normal Funtion"+"="*50)
_p_number=list(filter(lambda n:n>0,lst))
_n_number=list(filter(lambda n:n<0,lst))
print("\tPositive Numbers in lst are={}".format(_p_number))
print("\tNegative Number in lst are={}".format(_n_number))