dict = { } 
S = "I am Rajesh I am Rajesh"
I = S.split()
for word in I:
	if word in dict :
		dict[word]+=1
	else:
		dict[word]=1
print(dict)