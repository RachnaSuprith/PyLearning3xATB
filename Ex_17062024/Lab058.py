# def say_Hello():
#     print("Hello")
#
#
# say_Hello()


def say_Hello_arg(name):
   print("Hello",name)

say_Hello_arg("Rachna")


def say_Hello_arg_default(name="Rachna"):
   print("Hello",name)

say_Hello_arg_default("Vaishnavi")
say_Hello_arg_default("")
say_Hello_arg_default("Sachin")

def sum_num_arguement_ret(a,b):
    return a+b


result=sum_num_arguement_ret(3,4)
print(result)

