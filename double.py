def doubler(function):
    def wrapper():
        function()
        function()

    return wrapper


@doubler
def say_hello():
    print("hello")


say_hello()
