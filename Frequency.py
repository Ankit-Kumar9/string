#Accepting the string

s=input("Enter the word ")

#Using dict.get()

r={}
for keys in s:
	 r[keys]=r.get(keys,0)+1
	 
	 #printing the result
	 
print("No. of characters in "+s+" is : \n"+str(r))
