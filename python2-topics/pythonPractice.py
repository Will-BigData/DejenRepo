'''
import matplotlib.pyplot as plt
import numpy as np
plt.plot(np.random.randn(50).cumsum())
plt.savefig("test1.png")

l2=[1,2,3,4] # a list named array
pivot=2
less=[]
greater=[]

for num in l2:
    if num < pivot:
        less.append(num)
    else:
        greater.append(num)

print(less)
print(greater)




def append_element(some_list, element):
    some_list.append(element)

data = [1, 2, 3]
append_element(data, 4)
print(data)


#Mutable and Immutable Objects

#Most objects in Python, such as lists, dicts, NumPy arrays, and most userdefined types (classes), are mutable, i.e. the object or values that they contain can be modified:
a_list = ['foo', 2, [4, 5]]
print(a_list)
a_list[2] = (3, 4)
print(a_list)
#['foo', 2, (3, 4)]

#Others, like strings and tuples, are immutable:
# a_tuple = (3, 5, (4, 5))
# a_tuple[2] = (1,2)

#---------------------------------------------------------------------------
#TypeError                                 Traceback (most recent call last)
#Input In [33], in <module>
#----> 1 a_tuple[2] = (1, 2)
#
#TypeError: 'tuple' object does not support item assignment


# The backslash character \ is an escape character, meaning that it is used to specify special characters like newline \n or Unicode characters. To write a string literal with backslashes, you need to escape them:
s= '12\\34'
print(s)

s = r'this\has\no\special\characters'
print(s)
#'this\\has\\no\\special\\characters'

# template = '{0:2f} {1:s} are worth US${2:d}'
# print(template)
# print(template.format(4.5560, 'Argentine Pesos', 1))

#Dates and Times
from datetime import datetime, date, time
dt = datetime(2022, 1, 27, 20, 35, 15)
print(dt.day)
#27
print(dt.minute)
#35
print(dt.date())
#datetime.date(2022, 1, 27)
print(dt.time())
#datetime.time(20, 35, 15)

print(dt.strftime('%m/%d/%Y %H:%M'))
#'01/27/2022 20:35'

print(datetime.strptime('20220127', '%Y%m%d'))
#2022-01-27 00:00:00

dt.replace(minute=0, second=0)
#datetime.datetime(2022, 1, 27, 20, 0)

dt2 = datetime(2022, 2, 15, 22, 30)
delta = dt2 - dt
delta
#datetime.timedelta(days=19, seconds=6885)
type(delta)
#datetime.timedelta


#Control Flow

x=-6
if x < 0:
    print("It's negative")

if x < 0:
    print("It's negative")
elif x == 0:
    print("Equal to zero")
elif 0 < x < 5:
    print("Positive but smaller than 5")
else:
    print("Positive and larger than or equal to 5")


#Compound Conditionals
a = 5; b = 7
c = 8; d = 4
if a < b or c > d:
    print('Made it')


sequence = [1, 2, None, 4, None, 5]
total = 0
for value in sequence:
    if value is None:
        continue
    total += value
#print(total)


# for i in range(4):
#     for j in range(4):
#         if j > i:
#             break
#         print((i, j))

#While loop

x = 256
total = 0
while x > 0:
    if total > 500:
        break
    total += x
    x = x // 2
#print(total)

#pass
x=500
if x < 0:
    print('negative!')
elif x == 0:
# TODO: put something smart here
    pass
else:
    print('positive!')


#Range

# print(list(range(10)))
# print(list(range(0, 10)))

# print(list(range(0, 20, 2)))
# print(list(range(0, 10, -1)))

seq = [1, 2, 3, 4]
val = []
for i in range(len(seq)):
    val.append(seq[i])
    print(val)

    # sum
    sum = 0
for i in range(100000):
    # % is the modulo operator
    if i % 3 == 0 or i % 5 == 0:
        sum += i

# Ternary expressions
#Ternary expression in Python allows you to combine an if-else block that produces a value into a single line or expression. The syntax for this in Python is:
  #value = true-expr if condition else false-expr

#List, Set, and Dict Comprehensions

list_strings = ['b', 'is', 'cat', 'far', 'love', 'python']
x = [y.upper() for y in list_strings if len(y) > 2]
print(x)
#['CAT', 'FAR', 'LOVE', 'PYTHON']


string_lengths = {len(x) for x in list_strings}
print(string_lengths)
#{1, 2, 3, 4, 6}

string_lengths2 = set(map(len, list_strings))
print(string_lengths2)
#{1, 2, 3, 4, 6}

loc_mapping = {val : index for index, val in enumerate(list_strings)}
print(loc_mapping)
#{'b': 0, 'is': 1, 'cat': 2, 'far': 3, 'love': 4, 'python': 5}


states = [' Alabama ', 'Georgia!', 'Georgia', 'georgia', 'FlOrIda', 'south carolina##', 'West virginia?']
import re
def clean_strings(strings):
    result = []
    for value in strings:
        value = value.strip()
        value = re.sub('[!#?]', '', value)
        value = value.title()
        result.append(value)
    return result
# print(states)
# print(clean_strings(states))

def remove_punctuation(value):
    return re.sub('[!#?]', '', value)

clean_ops = [str.strip, remove_punctuation, str.title]
def clean_strings(strings, ops):
    result = []
    for value in strings:
        for function in ops:
            value = function(value)
        result.append(value)
    return result
# print(states)
# print(clean_strings(states, clean_ops))

#other way to do the same thing
for x in map(remove_punctuation, states):
    print(x)

[x for x in map(remove_punctuation, states)]


'''


# Nested list comprehensions
all_data = [['John', 'Emily', 'Michael', 'Mary', 'Steven', 'Stevenee'],
            ['Maria', 'Juan', 'Javier', 'Natalia', 'Pilar']]
#Now, suppose we wanted to get a single list containing all names with two or more e’s in them. We could certainly do this with a simple for loop:
names_of_interest = []
for names in all_data:
    enough_es = [name for name in names if name.count('e') >= 2]
    names_of_interest.extend(enough_es)
print(names_of_interest)