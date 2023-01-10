"""
Write a Python Program to calculate union of two set
A = {3,2,4,5,6,7,8} B = {4,12,5,1,6,8}
"""

print("Union two Set")

a= {3,2,4,5,6,7,8}
b= {4,12,5,1,6,8}

c= a.union(b)

print (c)

"""
Write a Python Program to calculate union of Three set
A = {5,12,52,0,8} B = {2,5,1,9,8}, C = {4,5,6,0,10}
"""

d= {5,12,52,0,8}
e= {2,5,1,9,8}
f= {4,5,6,0,10}

g= d.union(e,f)

print(g)