# number = "9,323,221,423,342,444,21"
# cleannumber = ''
# for i in range(0,len(number)):
#     # if number[i] not in "0123456789":
#        if number[i] in "0123456789":
#         cleannumber +=number[i]
# # print(cleannumber)
# num = int(cleannumber)
# print(num)

number = "9,323,221,423,342,444,21"
clean = ''
for char in number:
    if char in '0123456789':
        clean += char;
newNumber = int(clean)
print("The Number is {}".format(newNumber))


for sa in ["your", "are not", "In range of","age kindly","look another holiday"]:
    print(sa)


for i in range(0,100,5):
    print("i is {}".format(i))

for i in range(1,13):
    for j in range(1,11):
        print("{1} times {0} is {2}".format(i,j,i*j))
    print("======================")