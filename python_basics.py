#Roll no : TECOA166

#Problem 1 . Given two integer numbers return their product and if the product is greater than 1000, then return their sum? 

def mul_or_sum(n1, n2):
    product = n1 * n2
    if product <= 1000:
        return product
    else:
        return n1 + n2

n1 =  int(input("Enter 1st number : "))

n2 = int(input("Enter 2nd number : "))

print("\n")
result = mul_or_sum(n1, n2)
print("The result is", result)

#Problem 2. Given a range of first 10 numbers, Iterate from start number to the end number and print the sum of the current number and previous number.

def sumNum(num):
    previousNum = 0
    for i in range(num):
        sum = previousNum + i
        print("Current Number", i, "Previous Number ", previousNum," Sum: ", sum)
        previousNum = i

print("Printing current and previous number sum in a given range(10)")
sumNum(10)

#Problem 3. Given a string, display only those characters which are present at an even index number

def evenIndexChar(str):
  for i in range(0, len(str)-1, 2):
    print("index[",i,"]", str[i] )

inputStr = "PCCOEPUNE" 
print("Orginal String is ", inputStr)

print("Printing only even index chars")
evenIndexChar(inputStr)

#Problem 4. Given a string and an integer number n, remove characters from a string starting from zero up to n and return a new string

def removeChars(str, n):
  return str[n:]

print("Removing n number of chars")
print(removeChars("PCCOEPUNE", 5))

#Problem 5. Given a list of numbers, return True if first and last number of a list is same.

def firstLast(numberList):
    print("Given list is ", numberList)
    first = numberList[0]
    last = numberList[-1]
    if (first == last):
        return True
    else:
        return False

numList = [10, 20, 30, 40, 10]
print("result is", firstLast(numList))

#Problem 6. Given a list of numbers, Iterate it and print only those numbers which are divisible of 5.

def divisible(numberList):
    print("Given list is ", numberList)
    print("Divisible of 5 in a list")
    for num in numberList:
        if (num % 5 == 0):
            print(num)

numList = [10, 20, 33, 46, 55]
divisible(numList)

#Peoblem 7. Return the total count of sub-string “Emma” appears in the given string : 

str = “ABC is good developer. ABC is a writer”"
cnt = str.count("Emma")
print(cnt)

#Problem 8. Print the following pattern

for num in range(10):
    for i in range(num):
        print (num, end=" ") 
    print("\n")

#Problem 10: Given a two list of numbers create a new list such that new list should contain only odd numbers from the first list and even numbers from the second list

def mergeList(listOne, listTwo):
    print("First List ", listOne)
    print("Second List ", listTwo)
    thirdList = []
    
    for num in listOne:
        if (num % 2 != 0):
            thirdList.append(num)
    for num in listTwo:
        if (num % 2 == 0):
            thirdList.append(num)
    return thirdList

listOne = [10, 20, 23, 11, 17]
listTwo = [13, 43, 24, 36, 12]

print("result List is", mergeList(listOne, listTwo))

#Problem 11: Write a code to extract each digit from an integer, in the reverse order

number = 0976655
print("Given number", number)
while (number > 0):
    digit = number % 10
    number = number // 10
    print(digit, end=" ")

#Problem 14: Print downward Half-Pyramid Pattern with Star (asterisk)

for i in range(6, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print(" ")


