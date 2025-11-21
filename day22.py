l=[1,2,3,4,5,"hello",bool]
print(l)
print(type(l))
for i in l:
    print(i)
print(l[1:7:2])
print(l[1:len(l)])
print(l[-3])   #total length-3 which is 7-3=4 and in the fourth index it is 5

if 4 in l:
    print("yes")
else:
    print("no")



if "riti" in "smriti":
    print("yes")
else:
    print("no")


lst=[i*i for i in range(10)]
print(lst)

lst=[i*i for i in range(10) if i%2==0]
print(lst)