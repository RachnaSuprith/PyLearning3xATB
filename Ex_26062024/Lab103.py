numbers=[1,2,3,4,5,6,7,8,9,10]
def is_even(num):
    return num%2==0

new_numbers_even=filter(is_even,numbers)
print(list(new_numbers_even))

def is_greater_5(num):
    return num>5
new_numbers_five=filter(is_greater_5,numbers)
print(list(new_numbers_five))