import random 

num = random.randint(1,10)
print (num)
status = True

# while status :
#     a = int(input('Enter number :'))
#     if num == a :
#         print("Yes",num)
#         status = False
#     else:
#         print('No')


def boom_number():
    a = int(input('Enter number :'))
    if num == a :
        print ("Yes",num)
        
    else:
        print ('No')
        boom_number()


boom_number()




