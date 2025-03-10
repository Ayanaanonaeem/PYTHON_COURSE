# it is like destructuring of tuples, in this the values of name is assign to str1,str2,str3 

names=("ayan","ali","umer")
str1,str2,str3=names

print(str1)


# agr hamare pass value zyada hai lkn hamen do variables main store krna hai to hum variable se pehle staric lagadenge

str1,*str2=names
print(str2)


# for making tuples a list we use 

names=list(names)
print(names,"line 18")

names[0]="faraz"

print(names)

# for making tuple a list we use this

names=tuple(names)
print(names)