def my_decorator(func):
    def wrapper():
        print("something is happening....")
        func()
        print("after the function.")

    return wrapper


@my_decorator
def say_hello():
    print("Hello")


say_hello()
