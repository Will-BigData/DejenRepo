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

#re module provides support for regular expressions in Python. Regular expressions are useful for pattern matching and text manipulation (e.g., removing unwanted characters).

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


#An alternative approach that you may find useful is to make a list of theoperations you want to apply to a particular set of strings:

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

# we can wrap this whole operation up in a single nested list comprehension, like below:
flattenedName=[x for List in all_data for x in List]
result = [name for name in flattenedName if name.count('e') >=1]
print(result)


#Take another example where we “flatten” a list of tuples of integers into a simple list of integers:
some_tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
flattened = [x for tup in some_tuples for x in tup]
print(flattened)
#[1, 2, 3, 4, 5, 6, 7, 8, 9]


flattened = []
for tup in some_tuples:
    for x in tup:
        flattened.append(x)
print(flattened)

#list of lists
some_list= [[x for x in tup] for tup in some_tuples]
some_list[0][0]=0
print(some_list)

#Anonymous (Lambda) Functions
def short_function(x):
    return x * 2

equiv_anon = lambda x: x * 2


print(short_function(2))
x = equiv_anon(2)
print(x)

##
def apply_to_list(some_list, f):
    return [f(x) for x in some_list]
ints = [4, 0, 1, 5, 6]
y = apply_to_list(ints, lambda x: x * 2)
print(y)

print([x * 2 for x in ints])


#As another example, suppose you wanted to sort a collection of strings by the number of distinct letters in each string:
strings=['foo','card','bar','aaaa','abab']
strings2=sorted(strings,key=lambda x: len(x))
print(strings2)

strings.sort(key=lambda x: len(x))
print(strings)

#define the difference sort and sorted
#The sort method on a list modifies the list in-place, rather than returning a new list. If you don’t want to modify the original list, you can use the sorted function:
#The sorted function returns a new list containing the sorted values and leaves the original list unchanged.


#Generators

some_dict = {'a': 1, 'b': 2, 'c': 3}
for key in some_dict:
    print(key)

#abc

#When you write for key in some_dict, the Python interpreter first attempts to create an iterator out of some_dict:
dict_iterator = iter(some_dict)
print(dict_iterator)


l = list(dict_iterator)
print(l)

#A generator is a concise way to construct a new iterable object. Whereas normal functions execute and return a single result at a time, generators return a sequence of multiple results lazily, pausing after each one until the next one is requested. To create a generator, use the yield keyword instead of return in a function:
def squares(n=10):
    print('Generating squares from 1 to {0}'.format(n ** 2))
    for i in range(1, n + 1):
        yield i ** 2
gen = squares()
print(gen)

#It is not until you request elements from the generator that it begins executing its code:

for x in gen:
    print(x, end= ' ')

#Generating squares from 1 to 100
#1 4 9 16 25 36 49 64 81 100


#Generator expressions

gen = (x ** 2 for x in range(100))
print(gen)
#This is completely equivalent to the following more verbose generator:

def _make_gen():
    for x in range(100):
        yield x ** 2
gen = _make_gen()
# print(gen)

#Generator expressions can be used instead of list comprehensions as function arguments in many cases:
sum(x ** 2 for x in range(100))

#or with dictionaries for example:

dgen = dict((i, i **2) for i in range(5))
# print(dgen)


#{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

#Itertools Module

#NumPy

import numpy as np
'''
arr1 = np.arange(10000000)
print(arr1[0:10])
print(type(arr1))
l = list(range(10000000))
print(l[0:10])
print(type(l))'''

np.random.seed(0)
data = np.random.randn(2, 3)
"""print(data)

print(data.shape)
print(data*10)
print(data.dtype)"""

#The easiest way to create an array is to use the array function
data1 = [9, 17.5, 12, 0, 0.5]
arr1 = np.array(data1)
print(arr1)
print(arr1.shape)
#array([ 9. , 17.5, 12. ,  0. ,  0.5])

#In addition to np.array, there are a number of other functions for creating new arrays.
np.zeros(10)
#array([ 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])
np.zeros((3, 6))

np.empty((2, 3, 2))

np.arange(15)
#array([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])

#Pandas


import pandas as pd

first_letter1=lambda x:(x[0],x)
names = ['Alan','Adm','Wes','Will','Albert','Steven']
namesPairs=list(map(first_letter1,names))
print(namesPairs)

df = pd.DataFrame(namesPairs, columns =['first letter','name'])
print(df)
x=df.groupby('first letter').groups
print(x)
