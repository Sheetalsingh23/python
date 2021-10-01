n=int(input())
a=[int(x)for x in input().rstrip().split()] #list comprehension
a.sort() #sorting list in ascending order
print(min(a[-1]-a[1],a[-2]-a[0])) # prints the minimum of the two values provided
            
