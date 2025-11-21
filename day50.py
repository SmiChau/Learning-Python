# f=open('day50.txt','r')
# while True:
#     line=f.readline()
#     print(line)
#     if not line:
#         print("She is more to be described but end for now")
#         break
    
# f = open('day50.1.txt', 'r')

# # Read all lines at once instead of using readline()
# lines = f.readlines()

# # Split each line into a list of marks and remove any whitespace/newlines
# math = lines[0].strip().split(", ")
# english = lines[1].strip().split(", ")
# science = lines[2].strip().split(", ")

# i = 0
# while i < len(math):
#     m1 = math[i]
#     m2 = english[i]
#     m3 = science[i]

#     print(f"The marks of the student {i+1} in math is: {m1}")
#     print(f"The marks of the student {i+1} in english is: {m2}")
#     print(f"The marks of the student {i+1} in science is: {m3}")
#     print()  # for better readability

#     i = i + 1

# f.close()

f=open('day50.1.2.txt','w')
lines=['line 1\n','line 2\n','line 3\n']
f.writelines(lines)
f.close()