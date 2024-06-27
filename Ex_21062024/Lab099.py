def decorator1():
    def wrapper():
        print("Decor1")
        func()
    return wrapper


def decorator2(func):
    def wrapper():
      print("Decor2")
    func()
    return wrapper


@decorator1
@decorator2
def say_hello():
    print("Hello!")


say_hello()
