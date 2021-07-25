p,c,m,e,h = 0,0,0,0,0
t = 0
for _ in range(int(input())):
    t+=1
    a = input().split()
    p+=int(a[1])
    c+=int(a[2])
    m+=int(a[3])
    e+=int(a[4])
    h+=int(a[5])
arr = []
arr.append(str("{:.2f}".format(p/t)))
arr.append(str("{:.2f}".format(c/t)))
arr.append(str("{:.2f}".format(m/t)))
arr.append(str("{:.2f}".format(e/t)))
arr.append(str("{:.2f}".format(h/t)))

print(" ".join(arr))
