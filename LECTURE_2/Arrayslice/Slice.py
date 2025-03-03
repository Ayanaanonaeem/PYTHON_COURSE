# the square bracket is use for slice some string [startindex:length]

name="AbdulRehman"
firstName=name[0:5]
secondName=name[5:]
print(firstName)
print(secondName)

# the square bracket is use for slice some string [startindex:length:step] step ye hota hai kitne step se agey barhna hai

companyName="Saylani"
newName=companyName[0::2] #is main hum 2 step se agey barhenge yani 2 plus krdega aur woh print karega 
print(newName)

# for reversing the string 

#ye sbse se pehle -1 wala lega phr -1 main 0 plus karega jo hojayega -1 aur phr -1 main -1 plus karega jo hojayega -2
 
 # S  A  Y  L  A  N  I
 #-7 -6 -5 -4 -3 -2 -1

nextName=companyName[::-1] 
print(nextName)

