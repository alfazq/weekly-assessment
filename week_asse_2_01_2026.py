print('hellow world')

#q-1
lst1=[3, 1, 2, 4, 7, 6]
for i in range(len(lst1)):
 for j in range(i+1,len(lst1)):
  if lst1[i]%2==0:
   lst1[i],lst1[j]=lst1[j],lst1[i]
print(lst1)


#q-2
lst=[16, 17, 4, 3, 5, 2]
lst1=[]
for i in range(len(lst)):
 for j in range(i+1,len(lst)):
  if lst[i]<lst[j]:
   break
 else:
  lst1.append(lst[i])
print(lst1)

#q-3
lst=[1, 2, 3,3]
for i in range(len(lst)+1):
 for j in range(i+2,len(lst)):
  if lst[i]+lst[j-1]==lst[j]:
   print('true')


#q-4
lst1=[-1, 2, -3, 4, -5, 6]
pos=[]
neg=[]
result=[]
for i in lst1:
 if i<0:
  pos.append(i)
 else:
  neg.append(i)
result.extend(pos)
result.extend(neg)
print(result)

#q-5
lst=[1, 3, 5, 2, 2]
lst1=[]
for i in range(len(lst)):
 if sum(lst[:i])==sum(lst[i+1:]):
  lst1.append(i)
print(lst1)
   
   