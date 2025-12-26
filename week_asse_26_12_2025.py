print('hellow world')

#q-2
employees = {
"Alice": 70000,
"Bob": 80000,
"Charlie": 120000,
"David": 60000,
"Eve": 110000
}

b=dict(sorted(employees.items(),key=lambda x:x[1]))
print(list(b.items())[-3:])

#q-3
attendance = {
"Monday": ["Ahmed", "Fatima", "Hassan"],
"Tuesday": ["Fatima", "Ali", "Zainab"],
"Wednesday": ["Ahmed", "Hassan", "Ayesha"],
"Thursday": ["Fatima", "Ali", "Hassan"],
"Friday": ["Ahmed", "Fatima", "Zainab", "Ayesha"]
}
dict1={}
for i in attendance:
 if isinstance(attendance[i],list):
  for j in attendance[i]:
   if j in dict1:
    dict1[j]+=1
   else:
    dict1[j]=1
print(dict1)

c=dict(sorted(dict1.items(),key=lambda x:x[1]))
print(list(c.items())[-1])

#q-4
students = [
{"name": "Ahmed", "marks": [85, 90, 78]},
{"name": "Fatima", "marks": [92, 88, 95]},
{"name": "Hassan", "marks": [65, 70, 68]},
{"name": "Ayesha", "marks": [88, 85, 90]}
]
#def avg(students):
 #students['average']=sum(students['marks'])/len(students['marks'])

#avg(students)
#print(students)


#q-5
lst=[1, 2, 0]
for i in range(1,len(lst)):
 if i not in lst:
  print(i)
  break
