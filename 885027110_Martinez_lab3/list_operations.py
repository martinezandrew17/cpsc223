# Advanced List Options

def append_item(list, item):
    list.append(item)
    print(f"Item {item} appended successfully!")
    print(f"*** CURRENT LIST: {list} ***")

def insert_item(list, index, item):
    list.insert(index, item)
    print(f"Item {item} inserted at index {index} successfully!")
    print(f"*** CURRENT LIST: {list} ***")

def remove_item(list, item):
    if item in list:
        list.remove(item)
    print(f"Item {item} removed successfully!")
    print(f"****** CURRENT LIST: '{list}' *** ")

def pop_item(list, index=-1):
    if len(list) == 0:
        print(f"List is empty. Cannot pop an item")
    else:
        popped_item = list.pop(index)
        print(f"Item {popped_item} popped from index {index} successfully!")
        print(f"*** CURRENT LIST: {list} ***")

def clear_item(list):
    list.clear()
    print(f"List cleared successfully!")
    print(f"*** CURRENT LIST: {list} ***")

def sort_item(list):
    list.sort()
    print(f"List sorted successfully!")
    print(f"*** CURRENT LIST: {list} ***")

def reverse_list(list):
    list.reverse_list()
    print(f"List reversed successfully!")
    print(f"*** CURRENT LIST: {list} ***")

def index_of_item(list, item):
    if item in list: 
        index = list.index(item)
        print(f"Item {item} found at index {index} ")
    else: 
        print(f"Item {item} not found in the list.")
    print("*** CURRENT LIST: {list} ***")

def count_item(list, item):
    count = list.count(item)
    print(f"Item {item} appears {count} time(s) in the list. ")
    print("*** CURRENT LIST {list} ***")

def slice_item(list, start, end):
    sliced = list[start:end]
    print(f"Slice from index {start} to {end}: {sliced}")
    print(f"*** CURRENT LIST: {list} ***")




    



