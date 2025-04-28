print("Alhamdulillah")

list1= [ 1, 5, 2,34,4, 5]
print(list1)

# add  at the last
list1.append(555)
print(list1)


# Add at specific index
list1.insert(1, 7777)
print(list1)

# multiple data insert kora jay
list1.insert(2, "Xenon")
print(list1)

#remove function (first occurence remove korbe)
list1.remove(5)
print(list1)


# last value rempve
list1.pop()
print(list1)

# specific index remove
list1.pop(1)
print(list1)

# Reference ( list2 change korle list1 change hoye jabe) [ reference use kora ke shallow copy bole]
list2= list1
print(list2)

list2.append("Modify")
print(list1)
print(list2)

# Copy ( direct copy hobe, ekta change korle onnotay effect korbe na)
list3= list1.copy()
print(list3)