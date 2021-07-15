# cook your dish here
for _ in range(int(input())):
    a = []
    for i in range(int(input())):
        si = input()
        a.append(si)
    if ('cakewalk' in a and 'simple' in a and 'easy' in a and ('easy-medium' in a or 'medium' in a) and ('medium-hard' in a or 'hard' in a)):
        print("Yes")
    else:
        print("No")
