# a=input("Enter the word 'quit' in small letters")
# if(a!='quit'):
#     raise ValueError("You are supposed to enter the word 'quit' in small letters")


a = input("Enter the value between 2 and 9: ")
if(a=="quit"):
    print("no error")

elif(int(a)<2 or int(a)>9):
    raise ValueError("a should be the integer between the 2 and 9")

