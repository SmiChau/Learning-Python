x=int(input("Enter the value of x:"))
match x:
    case 0:
        print("The number is zero")
    case 1:
        print("The number is one")
    case 2:
        print("The number is two")
    case _ if x==90:
        print("It is the default number not equal to 90")
    case _ if x==89:
        print("It is the default number equal to 89")
    case _ if x>70 & x<80:
        print("It is the default number between 70 and 80")