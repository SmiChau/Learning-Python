# Default value
# def average(a=5,b=7):
#     print("the average value of a and b is",(a+b)/2)
# average() #we will get the default value
# average(3,6)     #it will ignore the default value
# average(b=9)  #it will take "a" as the default value and b as the given value


# def average(*numbers): # *numbers accept all the numbers you provide as the tuples in python
#     total = 0
#     print(type(numbers))  # This shows it's a tuple
#     for i in numbers:
#         total += i
#     if len(numbers) == 0:
#         print("No numbers provided.")
#     else:
#         print("Average is:", total / len(numbers))

# average(10,20,30,40)



# def name(**name):   # **name takes dictionary of key=value pairs
#     print("Hello,",name["fname"],name["mname"],name["lname"])


# name(mname="Kumar",lname="chaudhary",fname="sabin")




def averagenum(*num):
    total=0
    for i in num:
        total=total+i
    return (total/len(num))
    

c=averagenum(7,6,4,8)
print(c)
