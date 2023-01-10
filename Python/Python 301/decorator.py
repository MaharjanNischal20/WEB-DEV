def my_decorator(func):
    def wrapper():
        print("I_ live in Agnishala, Lalitpur")
        func()
        print("I am studying Bacheror in Engineering")
    return wrapper

@my_decorator
def my_fuc():
    print("Hello, My name is Nischal Maharjan")

my_fuc()