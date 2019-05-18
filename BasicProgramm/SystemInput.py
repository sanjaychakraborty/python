name = input("Please Enter you name: ")
print("your name is :" + name)
print(name + 'is dump')
print('''i am "{0}"'''.format(name))
print('''Jan:{0}
Feb:{1}
Mar:{0}
Apr:{2}
'''.format(31, 28, 30))
age = 28
number = "1, 2, 3, 4, 5"
print(number[::3])
# error while run
# print(name+'age is'+age)

print(name + 'age is{0} '.format(age))
print(name + 'age is' + str(age))
# python 2
print(name + 'age is %d' % age)

# python 2
for i in range(1, 12):
    print('Number %2d square is %4d and cube is %4d' % (i, i ** 2, i ** 3))

print("PI value in float %15.50f" % (22 / 7))

for i in range(1, 12):
    print('Number {0:2} square is {1:4} and cube is {2:4}'.format(i, i ** 2, i ** 3))

for i in range(1, 12):
    print('Number {0:2} square is {1:<4} and cube is {2:<4}'.format(i, i ** 2, i ** 3))

for i in range(1, 12):
    print('Number {:2} square is {:<4} and cube is {:<4}'.format(i, i ** 2, i ** 3))
