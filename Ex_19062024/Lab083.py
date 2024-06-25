# list = [1, 2, 3, 4, 5]
# temp_list=[]
# for i in list:
#     temp = i * 2
#     temp_list.append(temp)
#
# print(temp_list)
#


my_list=[1,2,3,4,5]
def double_item(num):
    return num*2
double_list=list(map(double_item,my_list))
print(double_list)