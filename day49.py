# f=open('day49.txt','r')    #r mode"reading" is default even if we do not use
# text=f.read()
# print(text)
# f.close()


# f=open('day49.1.txt','w')       #it automatically creates a new txt file of that file name if doesnt exist 
# f.write("I am proud of you smriti")     #to write inside the file
# f.close()


with open('day49.txt','a') as f:
    f.write("I am inside this file")