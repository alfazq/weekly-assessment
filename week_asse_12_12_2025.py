print('hellow world')

#q-1
str1="hello"
c=''
def rev(str1):
 if len(str1)!=0:
  global c
  c+=str1[-1]
  rev(str1[:-1])

rev(str1)
print(c)
  


#q-2
a=123 
b=321

sum1=0
sum2=0

while a>0:
 rem=a%10
 sum1=rem+sum1
 a=a//10

while b>0:
 rem=b%10
 sum2=rem+sum2
 b=b//10

if sum1==sum2:
 print(True)
else:
 print(False)


#q-3
a=9875
sum=0
while a>0:
 rem=a%10
 sum=rem+sum
 a=a//10
 if sum>9 and a==0:
  a=sum
  sum=0

print(sum)

#q-4
A=[1, 5, 3]
B=[0, 5, 2]

c=list(zip(A,B))
#print(c)
count=0
for i in c:
 if i[0]>i[1]:
  count+=1

print(count)

#q-5
str1="abcaad"
character = 'a'
l=[]
l2=[]
for i in range(len(str1)):
 if str1[i]==character:
  l.append(i)

#print(l)
for i in range(len(l)-1):
 l2.append(abs(l[i]-l[i+1]))
print(min(l2))
 




