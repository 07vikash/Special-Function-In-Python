'''
Q1=> Write a Python program which will display a list of old salary
     and new salary after hiking the salary of 10%?
'''
def shike(n):
    k=n+(n*0.1)
    return k
print("Enter Old Salary separated by space: ")
olds=[int(val) for val in input().split()]
news=list(map(shike,olds))
new_s=dict(zip(olds,news))
print("="*50)
print("\tSalary")
print("="*50)
for v,k in new_s.items():
    print("\t{}--->\t{}".format(v,k))
print("="*50)
