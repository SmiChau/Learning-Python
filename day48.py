# x=5         #global variable
# def localVar():
#     x=3     #local variable
#     y=1     #local variable
#     print(x,y)

# localVar()
# print(x)

x=5         #global variable
def localVar():
    global x
    x=3     # modified global variable
    y=1     #local variable
    print(x,y)

localVar()
print(x)