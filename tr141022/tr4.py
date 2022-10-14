def a_new_decorator(a_func):

    def wrapTheFunction():
        print("I am doing before")

        a_func()

        print("I am doing after")

    return wrapTheFunction
@a_new_decorator
def a_function_requiring_decoration():
    print("I am func that require the decoration")

print(a_function_requiring_decoration.__name__)



# a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)

a_function_requiring_decoration()