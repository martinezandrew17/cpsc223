# Lists Operations Basic and Advanced

# list_of_fruits = ["Apple", "cherry", "banana", "orange"];
# # list_of_fruits.append("Mango") # Append is add element

# # list_of_fruits.extend(["kiwi", "grape"]) # Add multiple elements
# # list_of_fruits.insert(1, "grape") # Insert at a given position based off of index
# # list_of_fruits.remove("banana") # Remove an element from the list
# # list_of_fruits.pop(0) # Pop an element from the list based off of index
# # list_of_fruits.pop()
# # list_of_fruits.clear() # Clears the lists
# # print(list_of_fruits.index("cherry", 0, 3)) # Search the list for the given element
# # print(list_of_fruits.count("Apple")) # Count the number of occurence in the list 
# # list_of_fruits.sort() # Alphabitizes the list
# # list_of_fruits.reverse() # Rearranges the list
# list = list_of_fruits.copy # Creates a copy
# print(list)

# Lists as Stack (LIFO)

# list_of_stack = ['1', '2', '3']
# list_of_stack.append('4')
# list_of_stack.append('5')
# list_of_stack.append('6')
# print(list_of_stack)
# list_of_stack.pop()
# print(list_of_stack)
# list_of_stack.pop()
# print(list_of_stack)
# list_of_stack.pop()
# print(list_of_stack)
# list_of_stack.pop()
# print(list_of_stack)
# list_of_stack.pop()

# Queue Using List (FILO)

# Method 1 (Not Time Efficient)
# queue = ['1', '2', '3']
# queue.append('4')

# print(queue)
# queue.pop(0)
# print(queue)
# queue.append('5')
# print(queue)
# queue.pop(0)
# print(queue)

# Method 2 Using Libraries

# from collections import deque
# queue_a = deque(['1', '2', '3'])
# queue_a.append('4')
# print(queue_a)
# queue_a.append('5')
# print(queue_a)
# queue_a.popleft()
# print(queue_a)
# queue_a.popleft()
# print(queue_a)

# List Comprehension

# squares = []
# for x in range(10): # Using Basic Operations 
#     squares.append(x**2)
# squares = [x**2 for x in range (10)] # List Comprehension
# squares = list(map(lambda x: x**2, range (10))) 
# print(squares)

# combs = []
# for x in [1,2,3]:
#     for y in [3,1,4]:
#         if x != y:
#             combs.append((x,y))
# print(combs)

# Using List Comprehension 
# combs = [(x,y) for x in [1,2,3] for y in [3,1,4] if x != y]
# print(combs)

# list_of_squares = [-2, -4, 0, 6, 9]
# print([x**2 for x in list_of_squares]) # Squared
# print([x for x in list_of_squares if x >= 0]) # Returns positive values
# print([abs(x) for x in list_of_squares]) # Returns abs value

# fresh_fruit = ["  Banana ", "cherry  "," guave  "]
# print(fresh_fruit)
# print([x.strip() for x in fresh_fruit]) # Gets rid of the spaces
# print([x.lstrip() for x in fresh_fruit]) 
# print([x.rstrip() for x in fresh_fruit])

# list_of_no_and_their_squares = []
# print([(x,x**2) for x in range (10)]) # No with their squares

# list_of_vect = [[1,2,3], [4,5,6], [7,8,9]]
# print([num for elem in list_of_vect for num in elem]) # Flattens the list

# The Delete Statement 
# list_del = [1,2,3,4,5,6,7]
# del list_del[0] # Delete Single Element
# del list_del[2:4] # Delete the Range
# del list_del[:] # Returns Empty List
# del list_del # Erases it from the memory
# print(list_del)

# Tuples 
# tuple_t = (123,456,789)
# print(tuple_t)
# tuple_t[0] = 12345 # Cannot be changed

# Nested Tuples
# tuple_new = (tuple_t,('asdf','zxcv','zxcv'))
# print(tuple_new)

# Empty Tuple
# empty_tuple = ()
# print(len(empty_tuple))

# Tuple with single element
# single_element_tuple = ("Single")
# print(single_element_tuple)
# print(len(single_element_tuple)) 

# t = ('1', '2', '3')
# print(t)
# a,b,c = 1,2,3
# a,b,c = t
# print(a)
# print(b)
# print(c)

# Sets
# set_s = {'apple', 'banana', 'cherry', 'apple'}
# # # print(set_s)
# # if 'banana' in set_s:
# #     print("True")

# a = set('abracadabra')
# b = set('alacazam')
# # print(a) # unique in a
# # print(b)

# # print(a-b) # letters in a but not in b 
# # print(a | b) # letter in a or b or both
# # print( a & b ) # common in both a and b 
# # print(a^b) # letters in a or b but not both

# # Set Comprehension
# a = {x for x in 'abracadabra' if x not in 'abc'}
# print(a)

# Dictionaries

# banking = {4725: "checking", 5207: 'savings', 2786: 'loan'}
# # print(banking)

# stocks = {}
# # print(stocks) # empty dictionary or set 

# tel = {'jack': 4098, 'sape': 4139}
# # print(tel)
# tel['guido'] = 4127
# print(tel)
# print(tel['jack'])
# del tel['jack'] # delete element from the dictioniary
# print(tel)

# print(sorted(tel)) # alphabetically sorts
# print(list(tel)) # list of headings in dictionary
# if 'jack' in tel: # check element
#     print('true')
# if 'jack' not in tel: # check element not 
#     print('true')
# print(dict([('sape', 4129), ('guido', 4127), ('jack', 4098)]))

# dictionary comprehensions
# print({x: x**2 for x in (2, 4, 6)})

# declaring dictionary
# print(dict(sape = 4139, guido = 4127, jack = 4098))

# Looping Techniques in Data Strucutres
# knights = {'gallahad': 'the pure', 'robin': 'the brave'}
# for k, v in knights.items():
#     print(k,v)

# for i, v in enumerate(['tic', 'tac', 'toe']):
#     print(i,v)

# two or more sequences
# questions = ['name', 'quest', 'favorite color']
# answers = ['lancelot', 'the holy grail', 'blue']
# for q, a in zip(questions, answers):
#     print('What is your {0}? It is {1}.'.format(q,a))

# looping in reverse
# for i in reversed(range(1, 10, 2)):
#     print(i)

# looping in reverse with sorted order
# basket = ['apple', 'orange', 'apple', 'pear', 'orange',
#           'banana']
# for i in sorted(basket):
#     print(i)

# Using Set removes duplicated elements 
# basket = ['apple', 'orange', 'apple', 'pear', 'orange',
#           'banana']
# for f in sorted(set(basket)):
#     print(f)

# Filtering lists with the help of loop
# import math
# raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'),
#             47.8]

# filtered_data = []
# for value in raw_data:
#     if not math.isnan(value):
#         filtered_data.append(value)
# print(filtered_data)

# Conditions 
# if 'apple' not in ['grape', 'apple', 'orange']:
#     print('TRUE')
# else: 
#     print('FALSE')

# if 'apple' in ['grape', 'apple', 'orange']:
#     print('TRUE')
# else: 
#     print('FALSE')

# x = 'apple'
# y = ['apple']
# if x is y: 
#     print("TRUE")
# else: 
#     print("FALSE")

# a = 1 
# b = 2
# c = 3
# if a < b == c:
#     print('TRUE')
# else: 
#     print('FALSE')

# a = True
# b = False
# print(a and b) # false
# print(not(a and b)) # true 

# a = True
# b = False 
# c = False
# print(a and b and c)
# print(not(a and b and c))

# x = 1 
# if(x:= x + 1) == 2:
#     print('True')
# else: 
#     print('False')

# Comparing Sequences
# print((1, 2, 3) == (1, 2, 4)) # not equal
# print((1,2,3) < (1,2,4)) # equal
# print((1,2,3) > (1,2,4)) # not equal
# print(('ABC' < 'C' < 'Pascal' < 'Python')) # equal
# print(('ABC' < 'C' < 'Pascal' < 'Python' , 'bat')) # not equal
# print((1,2) < (1,2,-1)) # equal
# if [(1,2,('aa', 'ab')) < (1,2, ('abc', 'a',))]:
#     print('TRUE')

print(('aa', 'ab') < ('abc', 'a'))

