# a = input("Enter a number: ")
# b = input("Enter another number: ")

# try:
#     c = int(a) / int(b)
#     print(f"{a} divided by {b} is equal to: {c}")
# except Exception as e:
#     print("Sorry, some error occurred:", e)


# print("The program ended")


# try:
#     c=int(a)+int(b)
#     print(f"The sum of {a} and {b} is {c}")
# except Exception as e:
#     print("Invalid input!! it must be integer")


try:
    filename = input("Enter the file name: ")
    with open(filename, 'r') as f:
        content = f.read()
        print("File content:\n", content)
except FileNotFoundError:
    print("Error: The file does not exist.")
except PermissionError:
    print("Error: You do not have permission to read this file.")
except Exception as e:
    print("Something went wrong:", e)
