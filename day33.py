# dictionary

# dic={
#     1: "Smriti",
#     2: "Ram",
#     3: "Jdk"
# }

# print(dic[3])



dic1={"name":"Smriti", "roll": 13, "age":15, 3:"num"}
print(dic1)
print(dic1["name"])         #same thing1 but throws error if such key doesnt exist
print(dic1.get("name"))     #same thing2 but doesnt throw error and shows none if such key doesnt exist
print(dic1.keys())      #gives keys only  output: dict_keys(['name', 'roll', 'age', 3])
print(dic1.values())       #gives values only output:  dict_values(['Smriti', 13, 15, 'num'])

for key in dic1.keys():
    print(dic1[key])   #values haru dinxa


print(dic1.items())    #dic1 ko sab value haru dinxa euta arkai format ma
for key,value in dic1.items():
    print(key,value)
