#  AND OPERATOR
""" And main donon true honge to true hoga 
    warna False hoga
"""


x=3
y=2

z=x > y and y < x
print(z)#true

z=x < y and y < x
print(z)


# OR OPERATOR
""" OR main agr donon main se ek true hoga to true hoga 
    aur agr donon false honge to false hoga
"""
z= x == y or y != x
print("line no 22",z)#true

z= x == y or y == x
print("line n 25",z)#false

# NOT OPERATOR 

a=not False and True # true
b=not (False and True)#true
print(a)
print(b)