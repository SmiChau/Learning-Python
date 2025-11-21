marks=[12,56,32,98,12,45,1,4]

# index=0
# for mark in marks:
#     print(mark)
#     if(index==3):
#         print("Smriti is a cutie")
#     index+=1


#just does same thing but more efficient and better
for position, mark in enumerate(marks, start=1): #start=1 narakhey pani hunxa but index as a default 0 bata start hunxa
    print(mark)
    if(position==3):
        print("Smriti is a cutie")