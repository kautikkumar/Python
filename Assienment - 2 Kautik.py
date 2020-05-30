#!/usr/bin/env python
# coding: utf-8

# In[1]:


print()
print()
print("\t\t\t\tAssienment-2")
print("""1.1 Write a Python Program to implement your own myreduce() function which works exactly
like Python's built-in function reduce()""")
print()
print()
def myreduce(formula,l):
    c = 0
    for i in l:
        c = formula(c,i)
    
    return c

def sum1(a,b):
    return a+b


l = [1,2,3,4,5,6,7,8,9,10]
print("List is " , l)

print("sum of list is " , myreduce(sum1,l))
print()
print()


# In[2]:


print()
print()
print('''1.2 Write a Python program to implement your own myfilter() function which works exactly
like Pythons built-in function filter() ''')
print()
print()      
      
def myfilter(formula,l):
    m = [] 
    for i in l:
        m.append(formula(i))
        
    for i in range(len(m)):
        for j in m:
            if j == None:
                m.remove(None)
        
    print(m)
def even(a):
    if a%5 == 0 :
        return a
          
l = [2,3,4,5,6,7,8,9,12,15,456,67,5,25,35,45]
print( "origanal list " ,l)

print("filter list")
n = myfilter(even,l)
print()
print()


# In[3]:


print()
print()
print('''
2.Implement List comprehensions to produce the following lists 
  Write List comprehensions to produce the following Lists

1. ['A', 'C', 'A', 'D', 'G', 'I', 'L', 'D']

2. ['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']

3. ['x', 'y', 'z', 'xx', 'yy', 'zz', 'xx', 'yy', 'zz', 'xxxx', 'yyyy', 'zzzz']

4. [[2], [3], [4], [3], [4], [5], [4], [5], [6]]

5. [[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]

6. [(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]
''')

a = [i for i in "ACADGILD"]
print(a)

b = [i * j for j in ["x","y","z"] for i in [1,2,3,4] ]
print(b)

c = [ [i+j] for j in [0,1,2] for i in [2,3,4]]
print(c)

d = [[i+j for j in [0,1,2,3]] for i in [2,3,4,5]]
print(d)

e = [(i,j) for j in [1,2,4] for i in [1,2,3]]
print(e)
print()
print()


# In[3]:


print()
print()
print(" 3.Implement a function longestWord() that takes a list of words and returns the longest one.")
print()
print()

l = ["kautik", "kheni","kantibhai","hardikkheni"]

def longestWord(list1): 
    max = list1[0] 
   
     
    for x in list1: 
        if x > max : 
             max = x 
    
    return max
list1 =[]

for i in l:
    list1.append(len(i))
print("longest Word")
print(l[list1.index(longestWord(list1))])
print()
print("Longest Word Length")
print(len(l[list1.index(longestWord(list1))]))
print()
print()


# In[4]:


print()
print()
print('''
1.1 Write a Python Program(with class concepts) to find the area of the triangle using the below
formula.
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
Function to take the length of the sides of triangle from user should be defined in the parent
class and function to calculate the area should be defined in subclass.
''')
print()

class perentclass:

    def __init__(s, n):
        s.no_of_sides = n

    def print_num_sides(s):
        print('No of side is ', format(s.no_of_sides ))
        
class side(perentclass):

    def __init__(s, lofsides):
        perentclass.__init__(s, 3)
        s.lofsides = lofsides 

    def area(s):
        
        a, b, c = s.lofsides

        s = (a + b + c) / 2
        return (s*(s-a)*(s-b)*(s-c)) ** 0.5
    

triagle = side([5,5,5])
print("Area is")
print(triagle.area())
print()
triagle.print_num_sides()
print()
print()


# In[9]:


print()
print()
print('''
1.2 Write a function filter_long_words() that takes a list of words and an integer n and returns
the list of words that are longer than n.
''')
def filter_long_words(w, n):
    return filter(lambda x: len(x) > n, w)


list(filter_long_words(['kautik', 'kheni', 'kantibhai','hardikkheni'], 5))
print()
print()


# In[7]:


print()
print()
print('''
2.1 Write a Python program using function concept that maps list of words into a list of integers
representing the lengths of the corresponding words.
Hint: If a list [ ab,cde,erty] is passed on to the python function output should come as [2,3,4]
Here 2,3 and 4 are the lengths of the words in the list.
''')

l= ['ab', 'cde', 'erty']

def lenth(n):
    return len(n)
print ("list is " , l)
print("lenth of list" ,list(map(lenth,l)))        
print()
print()
    


# In[8]:


print()
print()
print('''
2.2 Write a Python function which takes a character (i.e. a string of length 1) and returns True if
it is a vowel, False otherwise.
''')

def vowel(char):
    v = ('a', 'e', 'i', 'o', 'u')
    if char not in v:
        return False
    return True

char = input("Enter Word")
print(' '+ str(char) +'  character is vowel?' , vowel(char))
print()
print()


# In[ ]:




