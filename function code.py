def my_decorator(func):
    def wrapper():
        print("something happing before the function is calling")
        func()
        print("something happing after the function is calling")
    return wrapper
    
@my_decorator
def say_hello():
    print('hello')
say_hello()

