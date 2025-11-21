def check():
    a = input("Enter a number: ")
    b = input("Enter another number: ")

    try:
        c = int(a) / int(b)
        print(f"{a} divided by {b} is equal to: {c}")
    except Exception as e:
        print("Sorry, some error occurred:", e)
        return

    finally:
        print("This will be executed no matter what")
    print("The program ended")

x=check()
print(x)