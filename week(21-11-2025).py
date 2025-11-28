#print('hellow world')
#q-1
d1={
    "x": {
        "y": {
            "z": 50
        }
    }
}
d2={}
def flat(dict1,str1=''):
 for i in dict1:
  if isinstance(dict1[i],dict):
   flat(dict1[i],str1+i+".")
  else:
   d2[str1+i]=dict1[i]

flat(d1)
print(d2)



#q-2
l1=[4, 5, 4, 6, 5, 7]
l2=[]
for i in l1:
 if i not in l2:
  l2.append(i)
print(l2)




#q=3
l1=[1, 5, 2, 5, 3]
l2=[]
for i in range(len(l1)):
 if l1[i] in l1[i+1:]:
  print(l1[i])
 


#q-4

str1="   Learning   Python   now   "
c=''
count=0
for i in str1:
 if i!=' ':
  c+=i
 elif c:
  count+=1
  c=''
if c:
 count+=1

print(count)



#q-5
d1={'m': 22, 'n': 10, 'o': 35, 'p': 18}
d2=sorted(d1,key=d1.get)
d3=d1.values()
d4=sorted(d3)
d5=dict(zip(d2,d4))
print(d5)
