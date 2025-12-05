print('hellow world')

#1
l1=[1, 3, 5, 7, 9]
count=0
for i in l1:
 if i%3==0 or i%5==0:
  count+=1

print(count)


#2
str1="hello world python"
l1=str1.split()
c=''
for i in l1[::-1]:
 c+=i+' '
print(c)


#3
str1="aabc"
str2="abc"
count=0
for i in str1:
 if i in str2:
  count=1
 else:
  count=0
if count==1:
 print("True")
else:
 print("False")


#4
a=4
b='*'
for i in range(a):
 print(b)
 b=" "+b

 
  
#5
str1="madam racecar apple".split()
for i in range(len(str1)):
 for j in range(i+1,len(str1)):
  if str1[i]