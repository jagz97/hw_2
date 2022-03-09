def func_counter(func):
    def wrapper(*args, **kwargs):
        wrapper.counter += 1
        return func(*args, **kwargs)

    wrapper.counter = 0
    return wrapper

@func_counter
def foo(y):
    return y+2**3-34

foo(23)
foo(21)
print(foo.counter) # expect 2 as output