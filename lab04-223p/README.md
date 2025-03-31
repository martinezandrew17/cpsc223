Laboratory 4
Advanced Data Structures, Looping Techniques, and Enhanced Dictionary Operations in Python
Objective:
Create a Python program to practice and demonstrate the following concepts:
•	Tuples and Sequences: Packing/unpacking tuples, handling empty tuples and one-item tuples.
•	Sets: Creating sets, performing membership tests, executing set operations (union, intersection, difference, and symmetric difference), and using set comprehensions.
•	Dictionaries: Creating, updating, and merging dictionaries, using dictionary comprehensions, and applying dictionary methods.
•	Looping Techniques: Iterating over dictionaries with .items(), lists with enumerate(), pairing sequences with zip(), and looping in reverse or sorted order.
•	Conditions and Comparisons: Using membership operators, chained comparisons, Boolean logic (including short-circuit evaluation), and lexicographical ordering.
•	Additional Challenges: Merging multiple dictionaries and checking if a sequence is strictly increasing.
________________________________________
Assignment Tasks
1. Create functions.py
At the top of the file, include your name, date, and a brief description of the file’s purpose as comments.
Implement the following functions. For each function, include:
•	Function name:
•	Description:
•	Arguments:
•	Return:
Make sure that the Arguments and Return sections are formatted so that the description for each item lines up correctly.
________________________________________
A. Tuples and Sequences
1.	Function name: create_tuple
Description:
Pack the provided arguments into a tuple and return it.
Arguments:
*args : A variable number of arguments to be packed into a tuple.
Return:
A tuple containing all the provided arguments.
2.	Function name: unpack_tuple
Description:
Unpack the tuple into individual variables and return them as a list.
(Assume the tuple has a fixed, known number of elements.)
Arguments:
t : A tuple to be unpacked.
Return:
A list of the unpacked elements.
3.	Function name: tuple_details
Description:
Return a dictionary containing details about the tuple such as its length, the first element, and the last element.
Handle the case of an empty tuple appropriately.
Arguments:
t : A tuple whose details are to be extracted.
Return:
A dictionary with keys such as 'length', 'first', and 'last'.
________________________________________
B. Set Operations
4.	Function name: create_set
Description:
Create a set from the given iterable.
Arguments:
iterable : An iterable from which to create a set.
Return:
A set containing unique elements from the iterable.
5.	Function name: set_operations
Description:
Given two sets, perform various set operations and return the results in a dictionary.
Arguments:
s1 : The first set.
s2 : The second set.
Return:
A dictionary with the following keys:
- 'union' : The union of s1 and s2.
- 'intersection' : The intersection of s1 and s2.
- 'difference' : The difference (elements in s1 but not in s2).
- 'symmetric_difference': The symmetric difference of s1 and s2.
6.	Function name: unique_sorted
Description:
Return a sorted list of unique elements from the provided iterable.
Arguments:
iterable : An iterable that may contain duplicate elements.
Return:
A sorted list of the unique elements.
________________________________________
C. Dictionary Operations
7.	Function name: create_dictionary
Description:
Create a dictionary from a list of key-value pair tuples.
Arguments:
pairs : A list of tuples, where each tuple is a key-value pair.
Return:
A dictionary constructed from the provided pairs.
8.	Function name: update_dictionary
Description:
Update the dictionary with the provided key-value pair.
If the key exists, its value is overwritten.
Arguments:
d : The dictionary to update.
key : The key to update or add.
value : The value associated with the key.
Return:
The updated dictionary.
9.	Function name: delete_key
Description:
Remove the specified key from the dictionary.
If the key does not exist, return an error message or raise an exception.
Arguments:
d : The dictionary from which to delete a key.
key : The key to be removed.
Return:
The dictionary after removal of the key, or an error message if the key is not found.
10.	Function name: dict_comprehension_example
Description:
Create a dictionary using comprehension that maps each element of the iterable
to its square (if numeric) or its length (if a string).
Arguments:
iterable : An iterable containing numbers and/or strings.
Return:
A dictionary with each element as a key and its corresponding computed value.
11.	Function name: merge_dictionaries
Description:
Merge a list of dictionaries into a single dictionary.
If the same key appears in multiple dictionaries, combine their values into a list.
Arguments:
dicts : A list of dictionaries to merge.
Return:
A dictionary where each key maps to a list of all values associated with that key from the input dictionaries.
________________________________________
D. Looping Techniques
12.	Function name: iterate_dictionary
Description:
Iterate over the dictionary and return a list of formatted strings showing key-value pairs.
Arguments:
d : The dictionary to iterate over.
Return:
A list of strings in the format "key: value".
13.	Function name: enumerate_list
Description:
Enumerate over the list and return a list of tuples containing the index and the corresponding element.
Arguments:
lst : The list to enumerate.
Return:
A list of tuples where each tuple is (index, element).
14.	Function name: zip_lists
Description:
Pair elements from two lists using the zip function and return the resulting list of tuples.
Arguments:
lst1 : The first list.
lst2 : The second list.
Return:
A list of tuples, each containing one element from lst1 and the corresponding element from lst2.
15.	Function name: reverse_and_sort
Description:
Return both a reversed version of the list and a sorted version of the list.
Arguments:
lst : The list to be processed.
Return:
A tuple with two lists:
- The first is the reversed list.
- The second is the sorted list.
________________________________________
E. Conditions and Sequence Comparisons
16.	Function name: check_membership
Description:
Check if a value exists within a sequence.
Arguments:
sequence : The sequence to search.
value : The value to check for.
Return:
True if the value is found, otherwise False.
17.	Function name: chained_comparison
Description:
Evaluate the chained comparison a < b == c and return the result.
Arguments:
a : The first value.
b : The second value.
c : The third value.
Return:
True if the comparison holds; otherwise, False.
18.	Function name: boolean_evaluation
Description:
Evaluate the Boolean expression (a and not b) or c using short-circuit evaluation.
Arguments:
a : A Boolean or value evaluated in a Boolean context.
b : A Boolean or value evaluated in a Boolean context.
c : A Boolean or value evaluated in a Boolean context.
Return:
The result of the Boolean expression.
19.	Function name: compare_sequences
Description:
Compare two sequences lexicographically.
Arguments:
seq1 : The first sequence.
seq2 : The second sequence.
Return:
-1 if seq1 is less than seq2;
0 if they are equal;
1 if seq1 is greater than seq2.
20.	Function name: is_strictly_increasing
Description:
Check if a sequence of numbers is strictly increasing
(i.e., each element is less than the next one).
Arguments:
sequence : A list or tuple of numbers.
Return:
True if the sequence is strictly increasing, otherwise False.
2. Create main.py (Driver Program)
At the top of the file, include your name, date, and a brief description of the file’s purpose as comments.
In main.py:
•	Import Functions:
Import all functions from functions.py.
•	Testing Your Functions:
For each function, write sample test cases that display the function’s input and output.
Use inline comments to explain the test case and the expected result.
•	Execution Block:
Use the following block to ensure tests run only when the module is executed directly:
## Submission
Submit a zip file containing all the code files on Canvas.
Naming Convention: `CWID_LastName_Firstname.zip`
Your zipped folder should contain the following files:
```
                  | > functions.py
                  | > main.py
                  | > test.py
                  | > test.sh (for UNIX-based systems)
                  | > win_test.bat (for Windows systems)
```
    
## Grading
1. All points add up to a total of 100 points possible as detailed below. Partial credit will be given where applicable.

| Points | Description |
| --- | --- |
|50|Environment setup and Lab Submission|
|20|All required files are submitted|
|30|All unit tests passed|
