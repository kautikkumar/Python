#!/usr/bin/env python
# coding: utf-8

# In[9]:


print()
print()
print("\t\t\tAssignment-3 ")

print(""" Task 1 1. Write a function to compute 5/0 and use try/except to catch the exceptions.""")
print()
def div():
    return 5/0

try:
    div()

except:
    print("\t\tNo Number devide by Zero. output is  infinite")
print()
print()


# In[10]:


print()
print()
print(""""""""" Task 1: 2.Implement a Python program to generate all sentences where subject is in
["Americans", "Indians"] and verb is in ["Play", "watch"] and the object is in
["Baseball","cricket"].""""""""" )  
    
print()

subjects = ["Americans", "Indians"]
verbs = ["Play", "watch"]
objs = ["Baseball","cricket"]

    
for i in subjects:
    for j in verbs:
        for k in objs:
            print(i,j,k)
print()
print()           


# In[1]:


print()
print()
print("""Task 2: 1.Write a function so that the columns of the output matrix are powers of the input vector.
The order of the powers is determined by the increasing boolean argument. Specifically, when
increasing is False, the i-th output column is the input vector raised element-wise to the power
of N - i - 1. """)


import numpy as np

x = np.array([1,2,3,4,5])
N = 4
np.vander(x,N)
print()
print()


# In[ ]:




