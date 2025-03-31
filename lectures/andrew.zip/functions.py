# Andrew Martinez
# Date: February 20, 2025
# This file contains functions to practice and demostrate advanced data structures,
# looping techniques, and enhanced dictionary operations in Python.

# 1) Tuples and Sequences

# Name: [Your Name]
# Date: [Today's Date]
# Description: This file contains functions to practice and demonstrate advanced data structures,
# looping techniques, and enhanced dictionary operations in Python.

# A. Tuples and Sequences

def create_tuple(*args):
    """
    Pack the provided arguments into a tuple and return it.
    
    Arguments:
    *args : A variable number of arguments to be packed into a tuple.
    
    Return:
    A tuple containing all the provided arguments.
    """
    return args

def unpack_tuple(t):
    """
    Unpack the tuple into individual variables and return them as a list.
    (Assume the tuple has a fixed, known number of elements.)
    
    Arguments:
    t : A tuple to be unpacked.
    
    Return:
    A list of the unpacked elements.
    """
    return list(t)

def tuple_details(t):
    """
    Return a dictionary containing details about the tuple such as its length, the first element, and the last element.
    Handle the case of an empty tuple appropriately.
    
    Arguments:
    t : A tuple whose details are to be extracted.
    
    Return:
    A dictionary with keys such as 'length', 'first', and 'last'.
    """
    details = {}
    details['length'] = len(t)
    details['first'] = t[0] if t else None
    details['last'] = t[-1] if t else None
    return details

# B. Set Operations

def create_set(iterable):
    """
    Create a set from the given iterable.
    
    Arguments:
    iterable : An iterable from which to create a set.
    
    Return:
    A set containing unique elements from the iterable.
    """
    return set(iterable)

def set_operations(s1, s2):
    """
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
    """
    operations = {}
    operations['union'] = s1 | s2
    operations['intersection'] = s1 & s2
    operations['difference'] = s1 - s2
    operations['symmetric_difference'] = s1 ^ s2
    return operations

def unique_sorted(iterable):
    """
    Return a sorted list of unique elements from the provided iterable.
    
    Arguments:
    iterable : An iterable that may contain duplicate elements.
    
    Return:
    A sorted list of the unique elements.
    """
    return sorted(set(iterable))

# C. Dictionary Operations

def create_dictionary(pairs):
    """
    Create a dictionary from a list of key-value pair tuples.
    
    Arguments:
    pairs : A list of tuples, where each tuple is a key-value pair.
    
    Return:
    A dictionary constructed from the provided pairs.
    """
    return dict(pairs)

def update_dictionary(d, key, value):
    """
    Update the dictionary with the provided key-value pair.
    If the key exists, its value is overwritten.
    
    Arguments:
    d : The dictionary to update.
    key : The key to update or add.
    value : The value associated with the key.
    
    Return:
    The updated dictionary.
    """
    d[key] = value
    return d

def delete_key(d, key):
    """
    Remove the specified key from the dictionary.
    If the key does not exist, return an error message or raise an exception.
    
    Arguments:
    d : The dictionary from which to delete a key.
    key : The key to be removed.
    
    Return:
    The dictionary after removal of the key, or an error message if the key is not found.
    """
    if key in d:
        del d[key]
        return d
    else:
        raise KeyError(f"'{key}' not found in dictionary.")

def dict_comprehension_example(iterable):
    """
    Create a dictionary using comprehension that maps each element of the iterable
    to its square (if numeric) or its length (if a string).
    
    Arguments:
    iterable : An iterable containing numbers and/or strings.
    
    Return:
    A dictionary with each element as a key and its corresponding computed value.
    """
    return {item: item**2 if isinstance(item, (int, float)) else len(item) for item in iterable}

def merge_dictionaries(dicts):
    """
    Merge a list of dictionaries into a single dictionary.
    If the same key appears in multiple dictionaries, combine their values into a list.
    
    Arguments:
    dicts : A list of dictionaries to merge.
    
    Return:
    A dictionary where each key maps to a list of all values associated with that key from the input dictionaries.
    """
    merged = {}
    for d in dicts:
        for key, value in d.items():
            if key in merged:
                merged[key].append(value)
            else:
                merged[key] = [value]
    return merged

# D. Looping Techniques

def iterate_dictionary(d):
    """
    Iterate over the dictionary and return a list of formatted strings showing key-value pairs.
    
    Arguments:
    d : The dictionary to iterate over.
    
    Return:
    A list of strings in the format "key: value".
    """
    return [f"{key}: {value}" for key, value in d.items()]

def enumerate_list(lst):
    """
    Enumerate over the list and return a list of tuples containing the index and the corresponding element.
    
    Arguments:
    lst : The list to enumerate.
    
    Return:
    A list of tuples where each tuple is (index, element).
    """
    return list(enumerate(lst))

def zip_lists(lst1, lst2):
    """
    Pair elements from two lists using the zip function and return the resulting list of tuples.
    
    Arguments:
    lst1 : The first list.
    lst2 : The second list.
    
    Return:
    A list of tuples, each containing one element from lst1 and the corresponding element from lst2.
    """
    return list(zip(lst1, lst2))

def reverse_and_sort(lst):
    """
    Return both a reversed version of the list and a sorted version of the list.
    
    Arguments:
    lst : The list to be processed.
    
    Return:
    A tuple with two lists:
    - The first is the reversed list.
    - The second is the sorted list.
    """
    return lst[::-1], sorted(lst)

# E. Conditions and Sequence Comparisons

def check_membership(sequence, value):
    """
    Check if a value exists within a sequence.
    
    Arguments:
    sequence : The sequence to search.
    value : The value to check for.
    
    Return:
    True if the value is found, otherwise False.
    """
    return value in sequence

def chained_comparison(a, b, c):
    """
    Evaluate the chained comparison a < b == c and return the result.
    
    Arguments:
    a : The first value.
    b : The second value.
    c : The third value.
    
    Return:
    True if the comparison holds; otherwise, False.
    """
    return a < b == c

def boolean_evaluation(a, b, c):
    """
    Evaluate the Boolean expression (a and not b) or c using short-circuit evaluation.
    
    Arguments:
    a : A Boolean or value evaluated in a Boolean context.
    b : A Boolean or value evaluated in a Boolean context.
    c : A Boolean or value evaluated in a Boolean context.
    
    Return:
    The result of the Boolean expression.
    """
    return (a and not b) or c

def compare_sequences(seq1, seq2):
    """
    Compare two sequences lexicographically.
    
    Arguments:
    seq1 : The first sequence.
    seq2 : The second sequence.
    
    Return:
    -1 if seq1 is less than seq2;
    0 if they are equal;
    1 if seq1 is greater than seq2.
    """
    if seq1 < seq2:
        return -1
    elif seq1 == seq2:
        return 0
    else:
        return 1

def is_strictly_increasing(sequence):
    """
    Check if a sequence of numbers is strictly increasing
    (i.e., each element is less than the next one).
    
    Arguments:
    sequence : A list or tuple of numbers.
    
    Return:
    True if the sequence is strictly increasing, otherwise False.
    """
    return all(sequence[i] < sequence[i+1] for i in range(len(sequence)-1))