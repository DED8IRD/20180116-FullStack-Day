
#####################################################################

# def is_even(myNumber):
#
#     if myNumber % 2 == 0:
#         print('True')
#     else:
#         print("False")
#
# is_even(5)
# is_even(6)

#####################################################################

# def opposite(a, b):
#
#     if a > 0 and b < 0:
#         print('True')
#     elif a < 0 and b > 0:
#         print('True')
#     else:
#         print('False')
#
# opposite(10, -1)
# opposite(2, 3)
# opposite(-1, -1)

#####################################################################

# def near_100(num):
#
#     if num >= 90 and num <= 110:
#         print('True')
#     else:
#         print('False')
#
# near_100(50)
# near_100(99)
# near_100(105)

#####################################################################

# def maximum_of_three(a, b, c):
#
#     print(max(a, b, c))
#
# maximum_of_three(5,6,2)
# maximum_of_three(-4,3,10)

#####################################################################

# def powered(x):
#
#     i = 0
#     while i <= 20:
#         print(x ** i)
#         i += 1
#
# powered(2)

#####################################################################

# userText = input('Enter something here. \n> ')
# newText = ''
# i = 0
#
# while i < len(userText):
#     newText = userText[i] * 2
#     i += 1
#     print(newText, end="")

#####################################################################

def missing_char(word):

    word = 'kitten'

    list = []
    for i, x in enumerate(word):
        list.append(word.replace(x, ''))
    return list

print(missing_char('kitten'))

#####################################################################

# latest_letter = 'pneumonoultramicroscopicsilicovolcanoconiosis'
# print(max(latest_letter))

