countryStates = ["Karnataka", "Chhattisgarh", "Delhi", "Maharastra", "Gujrat", "Panbaj", "J&K", "UtterPradesh"]
List_Demo = [(1,2),(1,1),(3,3)]
even = [2,4,6,8]
odd = [1,3,5,7,9]

def SortedListPrint():
    countryStates.sort() #based on ASCI Character value.
    for state in countryStates:
      print("India State Name: {}".format(state))

def ReverseListPrint():
    countryStates.sort(reverse= True) #based on ASCI Character value.
    for state in countryStates:
        print("India State Name: {}".format(state))

def sortSecond(val):
    return val[1]

def SortSecondValueList():
    List_Demo.sort(key=sortSecond)
    print(List_Demo)

    # In Reverse order
    print()
    List_Demo.sort(key=sortSecond,reverse=True)
    print(List_Demo)

def SortedFunction():
     number = even + odd
     # it print concatinate value
     print(number)

     # Python habitually returns None from functions and methods that mutate the data, such as list.sort ,
     # list.append , and random.shuffle , with the idea being that it hints to the fact that it was mutating.
     # If you want to take an iterable and return a new, sorted list of its items, use the sorted builtin function.

     #print(number.sort())
     #print(number)

     #solution using Sorted Function

     new = sorted(number)
     print(new)
     print(number)


#SortSecondValueList()

SortedFunction()

