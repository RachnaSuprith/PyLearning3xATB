# def sum3(a,b,c):
#     return a+b+c
# result=sum3(4,5,6)
# print(result)
def sum3(a=1,b=4,c=9):
    return a+b+c
result1=sum3(4,5,6)
result2=sum3()
result3=sum3(b=4,a=1,c=7)
result4=sum3(b=4,a=1)
print(result1,result2,result3,result4)