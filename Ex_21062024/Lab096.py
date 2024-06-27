def my_decorator(func):
    def wrapper():
        print("starting...")
        func()
        print("*****")
        print("ending...")

    return wrapper()

@my_decorator
def say_hello():
    print("say hello")


