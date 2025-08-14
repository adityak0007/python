import array as arr
a = arr.array('i',[1,2,3,4])
print(a)
for i in range (0,4):
    print(a[i],end="")

a.insert(1,55)   
print(a) 

a.remove(4)
print(a)

a.append(10)
print(a)

a.