numbers=[1,2,3,4,5,6,7,8,9,10]
def double_me(num):
    return num*2

new_list_double=map(double_me,numbers)
print(list(new_list_double))