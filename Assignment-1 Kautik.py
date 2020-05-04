#!/usr/bin/env python
# coding: utf-8




import time

print()
print("************************************************************************************************************************")
print("                                                 Kautik Project")
print("                                                  Assignment-1 ")
print("************************************************************************************************************************")
print()
print()
print("========================================================================================================================")
print(" 1.Install Jupyter notebook and run the first program and share the screenshot of the output")
print("========================================================================================================================")
print()
print("Calculator")
a = input ("Enter Value A :")
c = str(input ("Enter Formula :"))
b = input ("Enter Value B :")
if c == "+":
    d = float(a)+float(b)
elif c == "-":
    d = float(a)-float(b)
elif c == "*":
    d = float(a)*float(b)
elif c == "/":
    d = float(a)/float(b)
else:
    print("Wrong Input")
    
print("Answer Is :" ,  d)
 
print()
print("========================================================================================================================")
print(" 2.Write a program which will find all such numbers which are divisible by 7 but are not a multiple")
print("   of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a")
print("   comma-separated sequence on a single line.")
print("========================================================================================================================")
print()

h = []
e = int(input ("Enter Range Start Value A :"))
print()
f = int(input ("Enter Range Start Value B :"))
print()
for g in range(e,f):
    if g % 7 == 0 and g % 5 !=0:
        h.append(g)
        
print("This number are divisible by 7 but are not a multiple of 5 :")
print()
print(h)

print()
print("========================================================================================================================")
print(" 3.Write a Python program to accept the user's first and last name and then getting them printed in")
print("   the the reverse order with a space between first name and last name.")
print("========================================================================================================================")
print()



fn= input ("Enter First Name :") 
ln = input("Enter Last Name : ") 
print()
print("Full Name Is:",fn,ln)
print()
print("Full Name In Reverse:",fn[::-1],ln[::-1])

print()
print("========================================================================================================================")
print(" 4.Write a Python program to find the volume of a sphere with diameter 12 cm.")
print("========================================================================================================================")
print()




i = input ("Enter Diameter :")
j = float(i)
k = j/2
print("Radious Is :" , k )
l = (4/3) * (22/7) * k * k * k
print()
print("The Volume Of A Sphere With Diameter" , i ,"Cm Is", l)

print()
print("========================================================================================================================")
print("  5.Write a program which accepts a sequence of comma-separated numbers from console and generate a list.")
print("========================================================================================================================")
print()

values = input("Input some comma seprated numbers : ")
list = values.split(",")
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)

print()
print("========================================================================================================================")
print(" 6.Create the below pattern using nested for loop in Python")
print("========================================================================================================================")
print()


m = int(input ("Enter Number :"))
print()

for n in range(1,m):
       
            for j in range(1,n+1):
                print("*",end="")  
            print()
            
for o in range(-m,-1):
       
            for j in range(o+1,-1):
                print("*",end="")
            print()
print()
print("========================================================================================================================")
print(" 7.Write a Python program to reverse a word after accepting the input from the user")
print("========================================================================================================================")
print()


p = input ("Enter Name :")
print()
q = p[::-1]                
print("Reverse Name:" , q)       


print()
print("========================================================================================================================")
print(" 8.Write a Python Program to print the given string in the format specified in the sample output.")
print("========================================================================================================================")
print()



print("  \t    THE PEOPLE OF INDIA, \n \t\thaving solemnly resolved to constitute India into a SOVEREIGN,\n \t\t\t!SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC \n \t\t\t  and to secure to all its citizens")



time.sleep(6000)

