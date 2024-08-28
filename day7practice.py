list1 = [1,2,3,4,5,6,7,8]
print(list1)
print(list1[0:3])

list1[0]=0
print(list1)

list1.append(9)
print(list1)
list1.insert(3,5)
print(list1)
list1.remove(3)
print(list1)
list1.pop(2)
print(list1)
print(len(list1))
list1.sort()

list2 = [x*2 for x in range(10)]
print(list2)


tuple1=(3,5,7,2,6)
print(tuple1)

tuple2 = tuple1+(3,4,7,2,44)
print(tuple2)


print(tuple2.index(44))