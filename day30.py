# def factorial(n):
#     if(n==1 or n==0):
#         return n
#     elif(n<0):
#         return "invalid"
#     else:
#         return n*factorial(n-1)
    
# n=int(input("Enter the number to find out the factorial of that number:"))
# print(factorial(n))



def fib(n):
    if(n==0 or n==1):
        return n
    else:
        return fib(n-2)+fib(n-1)
    
for i in range(10):
    print(fib(i))
