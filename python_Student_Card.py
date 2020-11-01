# TECOA139
#Sheetal Singh
import numpy as np

class Student:
  def __init__(self, name, Class,PRN):
    self.name = name
    self.Class = Class
    self.PRN = PRN
    self.marks = []
    
  def __display(self):
    print(f"\nStudent Info:\nName: {self.name}\nClass: {self.Class}\nPRN number: {self.PRN}")
    
  def calculate(self,currSem):
    m = []
    print("\nEnter semester wise matks of student(marks greater than 40 only)")
    for i in range(1,currSem+1):
      semMarks = [int(x) for x in input(f"Enter 5 subjects marks for Sem-{i}: ").split()]
      m.append(semMarks)
    self.marks = np.array(m)

    self.__display()
    print("\nScore Card:-\n")
    print("Semester wise Percentage:-")
    Sum = self.marks.sum(axis = 1)
    for i in range(currSem):
      print(f"Sem {i+1} Total marks: {Sum[i]} out of 500 Percentage: {Sum[i]/5}%")
    print(f"\nOverall Aggregate Total marks:{Sum.sum()} out of {500*currSem}\nPercentage: {Sum.sum()/(5*currSem)}%")
  
    print("\nSemester wise Min/Max Marks:-")
    Min = self.marks.min(axis = 1)
    Max = self.marks.max(axis = 1)
    for i in range(currSem):
      print(f"Sem {i+1} Max: {Max[i]} Min: {Min[i]}")
    print(f"\nOverall Max Marks: {Max.max()}\nOverall Min Marks:{Min.min()}")
      
if __name__=="__main__": 
  currSem = int(input("Enter Current Semester: "))
  ch = 0
  studentList = []
  while True:
    print("\n1.Add Student")
    print("2.Display Student Card")
    print("3.Exit")
    ch = int(input("Enter Your Choice: "))
    if ch==1:
      name = input("Enter Name of Student: ")
      Class = input("Entet Class: ")
      PRN = input("Enter PRN number: ")
      studentList.append(Student(name,Class,PRN))
    elif ch==2:
      searchPRN = input("Enter PRN of student: ")
      flag = 0
      for s in studentList:
        if s.PRN==searchPRN:
          flag = 1
          try:
            s.calculate(currSem)
          except:
            print("\nException Occured...\nTry Again...\n")
      if not flag:
        print("\nPRN number not found...")
    elif ch==3:
      break
    else:
      print("Enter Valid Choice...")

'''
Output:-
Enter Current Semester: 5

1.Add Student
2.Display Student Card
3.Exit

Enter Your Choice: 1

Enter Name of Student: Sheetal Singh

Entet Class: TEA

Enter PRN number: abc

1.Add Student
2.Display Student Card
3.Exit

Enter Your Choice: 1

Enter Name of Student: Pooja dev

Entet Class: TEA

Enter PRN number: xyz

1.Add Student
2.Display Student Card
3.Exit

Enter Your Choice: 2

Enter PRN of student: abc

Enter semester wise matks of student(marks greater than 40 only)

Enter 5 subjects marks for Sem-1: 55 44 66 77 88 99

Enter 5 subjects marks for Sem-2: 54 65 75 85 62 52

Enter 5 subjects marks for Sem-3: 52 71 62 82 43 85

Enter 5 subjects marks for Sem-4: 54 82 94 61 42 73

Enter 5 subjects marks for Sem-5: 54 62 75 86 93 42

Student Info:
Name: Sheetal Singh
Class: TEA
PRN number: abc

Score Card:-

Semester wise Percentage:-
Sem 1 Total marks: 429 out of 500 Percentage: 85.8%
Sem 2 Total marks: 393 out of 500 Percentage: 78.6%
Sem 3 Total marks: 395 out of 500 Percentage: 79.0%
Sem 4 Total marks: 406 out of 500 Percentage: 81.2%
Sem 5 Total marks: 412 out of 500 Percentage: 82.4%

Overall Aggregate Total marks:2035 out of 2500
Percentage: 81.4%

Semester wise Min/Max Marks:-
Sem 1 Max: 99 Min: 44
Sem 2 Max: 85 Min: 52
Sem 3 Max: 85 Min: 43
Sem 4 Max: 94 Min: 42
Sem 5 Max: 93 Min: 42

Overall Max Marks: 99
Overall Min Marks:42

1.Add Student
2.Display Student Card
3.Exit

Enter Your Choice: 2

Enter PRN of student: xyz

Enter semester wise matks of student(marks greater than 40 only)

Enter 5 subjects marks for Sem-1: 77 88 95 91 83

Enter 5 subjects marks for Sem-2: 74 76 81 93 82

Enter 5 subjects marks for Sem-3: 62 72 85 91 93

Enter 5 subjects marks for Sem-4: 65 85 72 73 81

Enter 5 subjects marks for Sem-5: 85 61 85 76 92

Student Info:
Name: Pooja Dev
Class: TEA
PRN number: xyz

Score Card:-

Semester wise Percentage:-
Sem 1 Total marks: 434 out of 500 Percentage: 86.8%
Sem 2 Total marks: 406 out of 500 Percentage: 81.2%
Sem 3 Total marks: 403 out of 500 Percentage: 80.6%
Sem 4 Total marks: 376 out of 500 Percentage: 75.2%
Sem 5 Total marks: 399 out of 500 Percentage: 79.8%

Overall Aggregate Total marks:2018 out of 2500
Percentage: 80.72%

Semester wise Min/Max Marks:-
Sem 1 Max: 95 Min: 77
Sem 2 Max: 93 Min: 74
Sem 3 Max: 93 Min: 62
Sem 4 Max: 85 Min: 65
Sem 5 Max: 92 Min: 61

Overall Max Marks: 95
Overall Min Marks:61

1.Add Student
2.Display Student Card
3.Exit

Enter Your Choice: 2

Enter PRN of student: abc

Enter semester wise matks of student(marks greater than 40 only)

Enter 5 subjects marks for Sem-1: wrong input

Exception Occured...
Try Again...


1.Add Student
2.Display Student Card
3.Exit

Enter Your Choice: 3

'''