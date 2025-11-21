# with open('day51.txt', 'r') as f:
    # print(type(f))         # Just confirms it's a file object
    # f.seek(10)             # Moves the pointer to the 10th byte
    # data = f.read(5)       # Reads 5 characters starting from the 10th position
    # print(data)            # Prints: a goo
    # print(f.tell())        # Shows: 15 which means ailey kun position ma xau.. since 10+5=15

with open('day51.1.txt','w') as f:      #w coz truncate le modify garxa
    f.write("Hello Smriti Imma give you the world")
    f.truncate(20)          #esley agadi ko 20 letters matra linxa #it is used to shorten the length of file

with open('day51.1.txt','r') as f:
    print(f.read())



