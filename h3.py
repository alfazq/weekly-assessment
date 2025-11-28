print("hellow")
#q-1
str1="I love Python"
str2="Python is awesome"
str1=str1.split()
str2=str2.split()
c=[]
for i in str1:
 if i in str2:
  c.append(i)

print(c)

#q-2
l1=[1, 2, 3, 4, 6]
K = 6
l2=[]
for i in range(len(l1)-1):
 for j in range(i+1,len(l1)):
  if l1[i]*l1[j]==K:
   l2.append((l1[i],l1[j]))
print(l2)


#q-3
str1="hello"
vovel='aeiouAEIOU'
c=[]
k=-1
str2=''
for i in str1:
 if i in vovel:
  c.append(i)
for j in str1:
 if j in vovel:
  str2+=c[k]
  k+=-1
 else:
  str2+=j

print(str2)


#q-4
l1=[2, 5, 6, 7]
target = 4
l2=[]
for i in l1:
 l2.append(abs(target-i))
#print(l2)
c=min(l2)
d=l2.index(c)
print(l1[d])


#q-5
l1=["flower", "flow", "flight"]
l1.sort()
str1=''
for i in range(len(l1[0])):
 if l1[0][i]==l1[-1][i]:
  str1+=l1[0][i]
print(str1)
