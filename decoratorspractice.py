def deco(func):
    def wrapper(*args, ** kwargs):
        print("Start")
        a = 10 + 1
        func(a, *args, ** kwargs)
        print("End")
    return wrapper


# @deco
def f1(value):
    print("Hello", value)
