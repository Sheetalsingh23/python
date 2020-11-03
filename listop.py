#Roll no : TECOA166

#Execute following all List operations using appropriate data.

#1. append()

list1 = ['Sheetal', 'Sachin', 'Siya']
list1.append('Sangeeta')
print ("updated list : ", list1)

#output
updated list : ['Sheetal', 'Sachin', 'Siya','Sangeeta']

#2. copy()

oldlist = [1, 2, 3]
newlist = old_list
newlist.append('a')
print('Old List:', oldlist)
print('New List:', newlist)

#ouput
Old List: [1, 2, 3, 'a']
New List: [1, 2, 3, 'a']

#3. clear()

list= [6, 0, 4, 1] 
print('List before clear:', GEEK)  
 
list.clear()  
print('List after clear:', GEEK)  

#output:
List before clear: [6, 0, 4, 1]
List after clear: []

#4. extend()

list1 = ['physics', 'chemistry', 'maths']
list2 = list(range(5))    
list1.extend(list2)
print ('Extended List :', list1)

#output
Extended List :  ['physics', 'chemistry', 'maths', 0, 1, 2, 3, 4]

#5. index()

list1 = ['physics', 'chemistry', 'maths']
list1.insert(1, 'Biology')
print ('Final list : ', list1)

#output
Final list :  ['physics', 'Biology', 'chemistry', 'maths']

#6. count()

aList = [123, 'xyz', 'zara', 'abc', 123];

print ("Count for 123 : ", aList.count(123))
print ("Count for zara : ", aList.count('zara'))

#output
Count for 123 :  2
Count for zara :  1

#7. insert()

list1 = ['physics', 'chemistry', 'maths']
list1.insert(1, 'Biology')
print ('Final list : ', list1)

#output
Final list :  ['physics', 'Biology', 'chemistry', 'maths']

#8. pop()

list1 = ['physics', 'Biology', 'chemistry', 'maths']
list1.pop()
print ("list now : ", list1)

list1.pop(1)
print ("list now : ", list1)

#output
list now :  ['physics', 'Biology', 'chemistry']
list now :  ['physics', 'chemistry'] 

#9. remove()

list1 = ['physics', 'Biology', 'chemistry', 'maths']
list1.remove('Biology')
print ("list now : ", list1)
list1.remove('maths')
print ("list now : ", list1)

#output
list now :  ['physics', 'chemistry', 'maths']
list now :  ['physics', 'chemistry']

#10. sort()

list1 = ['physics', 'Biology', 'chemistry', 'maths']
list1.sort()
print ("list now : ", list1)

#output
list now :  ['Biology', 'chemistry', 'maths', 'physics']

#11. reverse()

list1 = ['physics', 'Biology', 'chemistry', 'maths']
list1.reverse()
print ("list now : ", list1)

#output
list now :  ['maths', 'chemistry', 'Biology', 'physics']
