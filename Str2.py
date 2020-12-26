num = 7
 
print('{0:0>5d}'.format(num))  # left
print('{0:0<5d}'.format(num))  # right
 
print('{:05d}'.format(num))
 
print("%0*d" % (5, num))
print(format(num, "05d"))
 
temp = 'test'
print(temp.rjust(10, '0'))
print(temp.ljust(10, '0'))
