# 1. Python Basics

# Variables and Data Types
    # Variables: 
        # Used to store data that can be referenced and manipulated during program execution.
        # Does not require varaible declaration.
        # Variables can only contain letters, digits, and underscores.
        # Cannot start with a digit. 
        # Case sensitive and avoid using keywords. 
        # Can assgin mutliple variables to the same value.
        # Can assign different variables in the same line. 
        # int() = compatible values to an integer, float() = values into floating-pointing numbers
        # and str() = converts any datay type into a string.
        # Local Variables: defined inside a function are local to that function. 
        # Global Variables: defined outside any function are global and can be accessed inside
        # using the global keyword. 
        # Can remove a variable using the del keyword. creates memory
    
    # Python is dynamically typed, so you do not need to declare variables types

x = 10
y = 3.14
name = " Alice "
is_student = True

# Number and Operators
    # Operators: 
        # Used to perform mathematical operations. 
        # Includes addition(+), subtraction(-), multiplication(*), division(/), and modulus(%).
        # Float Division: The quotient returned by this operator is always a float number, no 
        # matter if two numbers are integers. 
        # Floor Division: The quotient returned by this operator is dependent on the argument being 
        # passed. 
        # Modulus: It is used to find the remainder when the first operand is divided by the second. 
        # Exponentiation: **, used to raise the first operand to the power of the second. 
    # Python supports basic arthimetic operations: 

a = 10
b = 3
print(a / b)
print(a // b)
print(a % b)
print( a ** b)

# Strings 
    # Strings: 
        # Sequence of characters, including letterss, numbers, and symbols. 
        # Can be created using either single or double quotes. 
        # If we need a string to span multiple lines then we can use triple quotes. 
        # Indexed starting from 0 and -1 from end. 
        # Allows negative indexing, which starts from left to right. 
        # Slicing: extract portion of a string by specifying the start and end indexes. 
        # Syntax: string[start:end]
        # Are immutable meaning the cannot change after being created. 
        # Not possible to delete individual characters from a string but can delete whole string using 
        # del keyword. 
        # len(): returns the total number of characters in a string.
        # upper() and lower(): upper() converts all character to uppercase and lower() 
        # converts all characters to lowercase.
        # strip() and replace(): strip() removes leading and trailing whitespace from string
        # and replace() replaces all occurrences of a specified substring with another. 
        # Can combine string using + and repeat them using * operator
        # Simplest way to formatstring is by using f-strings. 
    # String can be indexed, sliced, and concentrated

s = 'Hello, World!'
print(s[0])
print(s[7:12])
print(s + '!!!')
print(len(s))

# 2 Lists
# Creating and Manipulating Lists
    # List
        # Is a built-in dynamic sized array. 
        # Can store a mixed of data types. 
        # Can be modified and can containn duplicate items. 
        # Are accessed directly using their postion(index), starting from 0.
        # Lists can be created with a construtor or square brackets. 
        # A list with repeated elements are created using the multiplication operator.
        # Indexing with a list begins at 0, so a[0], and negative indexing allows us to access
        # elements from the end of the list. a[-1] is the last element. 
        # append(): Adds an element at the end of the list.
        # extend(): Adds multiple elements to the end of the list.
        # insert(): Adds an element at a specific position. 
        # Update a value by accessing it using its index. 
        # remove(): Remove the first occurence of an element. 
        # pop(): Removes the element at a specific index or the last element if no index is specified. 
        # del statement: deletes an element at a specific index. 
        # Using a for-loop to iterate through a list. 
        # A nested list is a list within another list, which is useful for representing 
        # matrices or tables. We can access nested elements by chaining indexes. 
    # Lists are mutable and can hold multiple data types

my_list = [1, 2, 3, 'Python', True]
my_list.append(4)
my_list.insert(1, 1.5)
my_list.remove('Python')
popped_item = my_list.pop()

# List Comprehensions
        # Generate a new list by apllying an expression to each item in an
        # an exisitng iterable. 
        # List does the same task as a for-loop, just in a single line. 
        # Includes conditional statements to filter or modify items based on criteria. 
        # Syntax: # [expression for item in iterable if condition]
    # A concise way to create lists:

squares = [x**2 for x in range(10)]
even_numbers = [x for x in range(10) if x % 2 == 0]

# 3 Tuples 
        # Is a collection of objects sepearated by commas. 
        # Similar to a list in terms of indexing, nested objects, and repetition
        # But the difference is that a tuple is immutable (cannot be modifiied).
        # Using square brackets, we can get the values from tuples.
        # You can also use a negative index, meaning starting from the left to right.
        # Traversal occures through a for-loop.
        # Concatenation: Adding together two tuples using +. 
        # Slicing: Same syntax as list slicing, wtih starting with beginning index and ends
        # with last index. 
        # Can delete a tuple using del keyword. 
        # Finding the length includes len() aand using the tuple as the parameter.
        # Heterogeneous: Supports elements with multiple data types. 
        # List can be converted into a tuple using tuple() constructor and passing list
        # as a parameter. 
        # Creating a Tuple: 
            # Using round brackets
            # Without brackets
            # Tuple Constructor
            # Empty Tuple
            # Single Element Tuple
            # Using Tuple Packing

# Immutable Sequences 
    # Tuples are similar to lists but immutable (cannot be changed):

my_tuple = (1, 2, 3)
print(my_tuple(0))

# Packing and Unpacking

a, b, c = (1, 2, 3)
print(a, b, c)

# 4 Sets
    # Used to store a collection of items with the following: 
        # No duplicate elements
        # An unordered collection.
        # Internally use hasing that makes set efficient for search, insert, and delete.
        # Mutable.
    # set() method is used for type casting. 
    # You can stil add or remove elements from a set dispite not modifying it.
    # Can store a micture of string, integer, boolean, etc datatypes. 
    # Frozen sets are immutable objects that only support methods and operators
    # that produce a result without affecting the frozen set or sets to which
    # they are applied. 
    # Insert in the set is done through the set.add() function. 
    # Can be merged together using union() or | operator. 
    # Can find the intersection of two sets using intersection() or & operator.
    # Can find the difference between two sets using difference() or - operator. 
    # Set Clear() method empties the whole set inplace. 

# Unique Elements
    # Sets store unique elements and support mathematical operations:

my_set = {1, 2, 3, 3}
my_set.add(4)
another_set = {3, 4, 5}
print(my_set.union(another_set))
print(my_set.intersection(another_set))

# 5 Dictionaries
    # Introduction: 
        # Supports key: value pairs.
        # Values can be any data type and can be duplicated, while keys cannot. 
        # Syntax: d1 = {1: "andrew",} 
        # Dictionary keys are case sensitive.
        # Keys must be immutable
        # Keys must be unique
        # To access, we can use get() function
        # Using assignment can also add and update dictionary items. 
        # del keyword removes an item by key
        # pop(): removes an item by key and returns its value.
        # clear(): empties the dictionary.
        # popitem(): removes an returns the last-key value pair. 
        # Can itreate over keys[using keys() method], values[using values() method]
        # or both [using item() method] with a for-loop. 


    # Dictionaries store data as key-value pairs

my_dict = {'name': 'Alice', 'age': 25}
print(my_dict['name'])
my_dict['age'] = 26
my_dict['city'] = 'New York'

# Dictionary Comprehension
    # Syntax:
        # {key: value for (key, value) in iterable}

squares = {x: x**2 for x in range(5)}

# 6 Control Flow 

# Conditional Statements
    # if, else, elif
        # if statement is the most simple decsion-making statement. If the condition
        # evaluates to True, the block of code inside the if statement is executed.
        # if...else statement is a control statement that helps in decisio-making based
        # on specfic conditions. When the if condition is False. If the condition in the 
        # if statement is not true, then the else block will be executed. 
        # Nested if...else statement occurs when if...else structure is placed inside 
        # another if or else block. Nested if...else allows the execution of specific 
        # code blocks based on a series of conditional checks. 
        # if...elif...else statement in Python is used for multi-way decision-making. 
        # This allows you to check multiple conditions sequentially and execute a specific
        # block of code when a condition is True. If none of the conditions are true, the 
        # else block is executed. 



x = 10 
if x > 10:
    print('x is greater than 10')
elif x == 10:
    print('x is 10')
else: 
    print('x is less than 10')

# Loops

# For loop
    # Syntax: 
        # for iterator_var in sequence: 
            # statement(s)
    # Used for sequential traversal. 
    # Traversing a list or array or string. 
    # Can be used to iterate lists, tuples, stirngs and dictionaries.
    # Use the index of elements in the sequence to iterate. Calculate the length
    # of the list and in iterate over the sequence within the range of the list. 
    # Combine the elese statement with for loop like in while loop. 

for i in range(5):
    print(1)

# while loop
    # Syntax:
        # while expression: 
            # statement(s)
    # Executed a block of statements repeatedly until a given condition is satisfied.
    # When the condition becomes false, the line immediately after the loop in the 
    # program is exectued.
    # Else clause is only executed when our while condition becomes false. If we break
    # out of the loop or if an exception is raised then it won't be executed. 
    # Syntax: 
        # while condition: 
            #  execute these statement(s)
        # else: 
            # executre these statement(s)
    

x = 10
while x < 5:
    print(x)
    x += 1

# Loop Control
    # Change execution from their normal sequence. 
    # The continue statement in Python returns the control to the beginning of the loop.
    # The break statement in Python brings control out of the loop.
    # We use the pass statmeent in Python to write empty loops. Pass is also used for 
    # empty control statements, functions and classes. 

for i in range(10):
    if 1 == 5:
        break
    if 1 % 2 == 0:
        continue
    print(1)

# 7 Functions

# Define Functions
    # Syntax:
        # def function_name(parameters):
            # statement
            # return expression
    # There are built-in library functions.
    # There are user-defined functions.
    # Created using the def keyword.
    # Is called using the name of the function().
    # use def to define a function

def greet(name):
    return f'Hello, {name}'

print(greet('Alice'))

# Default Arguments
    # Arguments re the values passed inside the parenthesis of the function.
    # Supports various types of arguments that can be passed at the time of
    # the function call. 
    # A default argument is a parameter that assumes a default value if a value 
    # i not provided in the function call for that argument. 
    # Defualt values for parameters
    
def power(x, n = 2):
    return x ** n

# Lambda Functions
    # An anonymous function means that a function is without a name. As we 
    # already know the def keyword is sued to define the normal functions and the 
    # lambda keyword is used to create anonymous functions. 
    # Small anonymous functions:
square = lambda x: x ** 2
print(square(5))

# 8 Advanced Topics

# List as Stack (LIFO)
    # Stack is a linear data strucutre that stores items in a Last-In/Last-Out manner.
    # A new element is added at one end and an element is removed from that end only. 
    # empty(): returns whether the stack is empty.
    # size(): returns the size of the stack
    # top(): / peek(): returns a reference to the topmost element of the stack
    # push(a): inserts the element 'a' at the top of the stack
    # pop(): deletes the topmost element of the stack
    # append() is used to add element to the top of the stack while pop() removes
    # the element in LIFO order. 

stack = []
stack.append(1)
stack.append(2)
stack.pop()

# List as Queue (FIFO)
    # Inserted into queue using the put() function and get() takes data out from
    # the queue. 
    # maxsize: number of items allowed in the queue. 
    # empty(): return True if the queue is empty, False otherwise. 
    # full(): Return True if there are maxszie items in the queue. If the queue was
    # intialized with maxsisze = 0; then full() never returns True. 
    # get(): remove and return an item from the queue. 
    # Use as collections.deque for efficient queues

from collections import deque
queue = deque()
queue.append(1)
queue.append(2)
queue.popleft()

# Enumerate and Zip
    # Enumerate() function adds a counter to each item in a list 
    # Syntax: 
        # enumerate(iterable, start = 0)
    # Using enumerate() starts indexing from 0, we can customize this using the 
    # start paramater.
    # First prints tuples of index, and element pairs, then it changes the starting
    # index while printing them together, then prints the index and element separately
    # each on its own line. 
    # Serves as an iterator, inheriting all associated iterator functions and methods. 
    # Use the next() function.
    # Each time the next() is called, the internal pointer of the enumerate object 
    # moves to the next element, returning the corresponding tuple of index and value. 
    # Ennumerate for index and value

    # zip() is used to combine the two lists into a single iterable 'res'
    # Each element from names is paired with corresponding element from scores
    # list() converts the iterator from zip() into a list of tuples, making it easier
    # to visualize or manipulate the combined data.
    # Syntax: 
        # zip(*iterable)
    # Iterables refers to iterable objects like lists and tuples
    # If no paraeters are passed, zip() returns an empter iterator. 
    # If only one iterable is passed, the result will be a series of single-element
    # tuples.
    # if multiple iterables are passed, each tuple will contain one element from each iterable.
    # When using iterables of different lengths, the zip() will only pair up to the 
    # shortest iterable. 
    # Can also reverse the operation by unzipping the data using the * operator. 
    # zip() to combine dictionary keys and values, or even iterate over multipe dictionaries
    # simultaneously. 


for i, value in enumerate(['a', 'b', 'c']):
    print(i, value)

    # Zip to loop over multiple sequences: 

names = ['Alice', 'Bob']
ages = [25, 30]
for name, age in zip(names, ages):
    print(name, age)

# 9 Condtions and Comparisons

# Chained Comparisons
    # Allows cleaner and more readable code when evaluating multiple conditions.
    # Traditional Comparison Syntax:
        # if a < b and b < c:
            # Code Block
    # Using Chaining Syntax:
        # if a < b < c:
            # Code Block
    # In a chained comparison, y is evaluated only once, making it more efficient. 
    # Python does not assume a direct relatiomnship between non-adjacent elements
    # in a chained comparison.
    # Python allows mixing different types of comparison operators within a single
    # chained expression. 
    # Supports chaining with is and in operators, allowing for more complex and 
    # readable conditions.
    

x = 5
print(1 < x < 10)

# Boolean Operators 
    # and, or, not:
    # and: Returns True if both the operands are true 

        # Syntax: 
            # x and y 
    # or: Treturns True if both the operands are true
        # Syntax:
            # x or y
    # not: Returns True if the operand is false
    # Python always evaluates the expression from left to right. 


x = 5 
print( x > 0 and x < 10)
print(x < 0 or x > 10)
print(not x == 5)

# 10 PEP 8 Style Guide

# Follow PEP 8 for clean and readable code

def my_function():
    print('Hello, World!')

