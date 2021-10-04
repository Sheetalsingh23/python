for _ in range(int(input())): #test cases
    n = int(input())
    s = input()
    l = ['a','i','e','o','u']
    c = 0
    for i in range(n-1):
        if (s[i] not in l and s[i+1] in l):
            c += 1
    print(c)
