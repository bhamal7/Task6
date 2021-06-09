def decorater(dec):
    def func():
        print("this is the inside function")


        dec()
        print("this is first function.")


    return func()

def fig():

    print("fig function")

decorater(fig)

