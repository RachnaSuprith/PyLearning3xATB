from collections import OrderedDict
od=OrderedDict()
od['a']=45
od['c']=24
od['b']=34
od['d']=45
od['a']=785
print(od)

my_dict=dict()
my_dict['z']=23
my_dict['b']=17
my_dict['c']=45
my_dict['e']=34
print(my_dict)
for k,v in my_dict.items():
    print(k,v)