list1=["race", "care", "note", "tone", "state", "taste", "abc", "bca"]
for i in range(len(list1)):
 print(list1[i])


#2done
d1 = {'x': 10, 'y': 20, 'z': 30}
d2 = {'y': 15, 'z': 45, 'w': 50}


for i in d2:
 if i in d1:
  d1[i]=d2[i]+d1[i]
 else:
  d1.update({i:d2[i]})

print(d1)


#4done
b={'k': 90, 'l': 40, 'm': 70, 'n': 20, 'o': 60}
b1=sorted(b.values())
print(b1)
c=b1[-3]
print(c)

for i in b:
 if b[i]==c:
  print(i)


#5done
dict1={'u': 12, 'v': 5, 'w': 25, 'x': 7}
b=sorted(dict1,key=dict1.get)
c=sorted(dict1.values())
print(c)
print(b)

res=dict(zip(b,c))
print(res)


#
dict2={'u': 12, 'v': 5, 'w': 25, 'x': 7}
b=dict2.values()
c=dict2.keys()
print(list(c))
print(list(b))


 
