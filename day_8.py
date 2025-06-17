# List 

l1 =["abc" , "xyz" ,"pqr"]
print(l1)
print(type(l1))

# count length of list
print(len(l1))        

l2 = [1,2,3, 4.5 ,"abc" ,"hello"]
print(l2)

# concatnation
l3 = l1 + l2
print("concatnation :",l3)

# indexing
print(l3[4])

print(l3[1:4])

print(l3[ :4])

print(l3[-1:])      # staring from last

# updateing
l4 = [10,20,30,40]
l4[2] = "python"
print(l4)

l4[1:3]=['a','b']       # range update
print(l4)

#inserting
l4.insert(0,"python")
l4.insert(3,12)
print(l4)

# appending
l4.append(100)
l4.append("s")      # add at the end
print(l4)

#extending
l4.extend([1,2,3])      # add multiple element at the end
print(l4)


# remove :- remove particular element
l4.remove(12)
print(l4)

#pop :- remove with indexing
l4.pop(0)
print(l4)

# reversing list
l4.reverse()
print("reverse list :",l4)


# del :- delete all list with memory space
del l1

# clear : onle remove element
l4.clear()
print(l4)

# sorting
l5 =[2,3,1,4,6,5]
l5.sort()
print(l5)

l6 =['s','a','m','r','u','d','d','h','i']
l6.sort()
print(l6)


# list loop
for i in l6:
    print(i)






