# dictionary
dict = {"brand":"ford",
        "model":"mustang",
        "year":1964}
print(dict)
print(type(dict))

# pass key for value
print(dict["brand"])

# key always unique
dict = {"brand":"ford",
        "model":"mustang",
        "year":1964,        # it does not print
        "year":2020}
print(dict["year"])


# len 
print(len(dict))


# multiple value allow in one key
dic = {"color:":["red","blue","green"]}
print(dic)


# get for access value
print(dict.get("model"))

#keys() for access key
print(dict.keys())

#values() for access value
print(dict.values())


# find key present  or not
print("year" in dict)
print ("year" not in dict)
print("abc" in dict)


# using copy()
dic = dict.copy()
print("copy the dictionary:",dic)


# update
dict["year"] = 2025
print(dict)

    #OR

dict.update({"year":2023})
print(dict)


# pop() remove key and value
dict.pop("brand")
print(dict)

# popitems() remove random value
dict.popitem()
print(dict)

# clear() 
dict.clear()
print(dict)



# using for loop
dict1 = {"brand":"ford",
        "model":"mustang",
        "year":1964,        # it does not print
        "year":2020}
print(dict1["year"])

for i in dict1:         # for key
    print(i)

    #OR
for i in dict1:
    print(i,"-",dict1[i])      # for key value

    #OR
for i in dict1.values():
    print(i)

    #OR
for x,y in dict1.items():
    print(x,"-",y)



