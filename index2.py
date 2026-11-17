# x = "global"
# def outer():
#     x = "enclosing"
#     def inner():
#         print("inner x:",x)
#     inner()
# outer()

x = "global"
def outer():
    x = "enclosing"
    def inner():
        print("inner x:",x)
    inner()
    print("outer x:",x)
outer()