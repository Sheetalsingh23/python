import socket

op=input("1. URL to IP\n2. IP to URL\nEnter your option : ") 
var=input("Enter URL/IP : ")

addr1 = socket.gethostbyname(var)
addr6 = socket.gethostbyaddr(var)

if op==1: 
	print(addr1)

else:
	print(addr6)