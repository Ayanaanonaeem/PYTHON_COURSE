# it is like destructuring of tuples, in this the values of name is assign to str1,str2,str3 

names=("ayan","ali","umer")
str1,str2,str3=names

print(str1)


# agr hamare pass value zyada hai lkn hamen do variables main store krna hai to hum variable se pehle staric lagadenge

str1,*str2=names
print(str2)
