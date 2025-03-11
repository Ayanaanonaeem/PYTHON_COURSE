# We can also give default value to parameter if user doesnot give any value we can use this

def greet_user(name="Ayan"):
    print("hello",name)

greet_user("Wali")


# we can also give default value while calling

def mul_arg(p1,p2,p3,k1,k2,k3):
    print(p1,p2,p3,k1,k2,k3)

mul_arg(3,4,5,k1=6,k3=7,k2=8)
