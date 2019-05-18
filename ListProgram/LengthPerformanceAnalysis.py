from operator import length_hint
from ListProgram.TakeInput import ListIntegerInput
import time

def lengthViaLoop(List):
    count = 0
    start_time = time.time()
    for i in List:
        count+=1
    end_time = time.time() - start_time
    return end_time

def lengthViaLen(List):
    start_time = time.time()
    length = len(List)
    end_time = time.time() - start_time
    return end_time

def lengthViaLength_hint(List):
    start_time = time.time()
    length = length_hint(List)
    end_time = time.time() - start_time
    return end_time


def MainMethod():
    print("Time Taken by Loop: {}".format(lengthViaLoop(ListIntegerInput("Please Enter List Value: "))))
    print("Time Taken by Len: {}".format(lengthViaLen(ListIntegerInput("Please Enter List Value: "))))
    print("Time Taken by Length_hint: {}".format(lengthViaLength_hint(ListIntegerInput("Please Enter List Value: "))))

MainMethod()

