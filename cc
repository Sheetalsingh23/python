import statistics
for _ in range(int(input())):
    n = int(input())
    a =list(map(int,input().split()))
    if (len(a)==2):
        print(1)
    elif (len(a)==2 and a[0]==a[1]):
        print(0)
    else:
        m = statistics.mode(a)
        #print(a.count(m))
        print(n-(a.count(m)))
