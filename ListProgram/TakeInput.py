
def ListIntegerInput(info):
    length = int(input("Please Enter Your List Length: "))
    return [int(input("{}".format(info)))  for i in range(length)]
