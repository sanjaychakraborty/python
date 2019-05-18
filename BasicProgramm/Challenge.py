try:
    name = input("Enter your Name")
    age = int(input("Enter you age"))
    if(name != ' ' and  age != ' '):
        if(18<age<30):
            print("Welcome to your Holiday")
        else:
            print("your are not In range of age kindly look another holiday")
    else:
        print("Input should not be empty \n Name: {} \n Age:{}".format(name,age))
except:
    print("An exception occurred")