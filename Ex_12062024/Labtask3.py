# #factorial of anumber
# num=int(input("Enter a number here:"))
# fact=1
# if num<0:
#     print("Factorial of num does not exist")
# if num==0:
#     print("Factorial of num is",1)
# if num>0:
#     for i in range(1,num+1):
#      fact=fact*i
#     print("Factorial of given num is ", fact)

def fact(a):
    if a==0:
        return 1
    else:
        return((a*fact(a-1)))
num=int(input("enter a num:"))
result=fact(num)
print("The factorial of given number is" , result)