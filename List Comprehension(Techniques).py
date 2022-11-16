"""Q1-> Write a Python program which will accept list of numerical integers.
     filter even and odd numbers from list of numbers)"""
print("Enter Integers value using Space:")
lst=[int(val) for val in input().split()]
e_num=tuple(filter(lambda x:x%2==0,lst))
o_num=list(filter(lambda x:x%2!=0,lst))
print("\t Even number are from lst={}".format(e_num))
print("\t Odd number are from lst={}".format(o_num))

"""Q2--> Write a Python Program which will accept line of text and filter
     vowels, consonents, digits and Special Character?"""

line=input("Enter a line Text:")
vcount=tuple(filter(lambda x: x in ['a','e','i','o','u','A','E','I','O','U'],line))
ccount=tuple(filter(lambda x: x not in ['a','e','i','o','u','A','E','I','O','U'],line))
print("\t Vowel are in text data={}".format(vcount))
print("\t Consonent are in text data={}".format(ccount))
