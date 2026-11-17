# x=10
# def show():
#     x=20
#     print(x)
# show()
# print(x)

# x=10
# def show():
#     global x
#     x = 20
#     print(x)
# show()
# print(x)

# def outer():
#     x = "outer"
#     def inner():
#         nonlocal x
#         x = "inner"
#     inner()
#     print("x after inner():", x)
# outer()

# def outer():
#     x = "outer"
#     def inner():
    
#         x = "inner"
#     inner()
#     print("x after inner():", x)
# outer()

x="global"
def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print("inner x:", x)
    inner()
    print("outer x:, x")
outer()
print("global x:", x)