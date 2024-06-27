pramod_details2 = {"name": "Pramod", "90": 34.34, "Ismale":"True","Address":"KA"}
print(pramod_details2.get("Address"))
print(pramod_details2["Address"])
print(pramod_details2.values())
print(pramod_details2.keys())

my_dict={'a':1,'b':2,'c':3,'a':95}
print(my_dict)
print(len(my_dict))

my_dict1={'a':1,'b':2,'c':3,'d':95,'e':2}
print(my_dict1)
print(list(my_dict1.keys()))
for i in list(my_dict1.values()):
    print(i)
for k,v in my_dict1.items():
    print(k,v)
