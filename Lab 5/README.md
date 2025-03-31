# Lab 5: Grocery Shopping

## Instruction:
1. Create a module `shopping.py` with the following functions:

    - Initialize an empty dictionary named `today_sale` to store customer carts.

    - `get_total_price(cart)`: This function takes a dictionary `cart` as a positional argument and returns the total price of all items in `cart`.
      
      Example:
      ```python
      your_cart = {'banana': 5.0, 'chicken': 1.0}
      total = get_total_price(your_cart)
      print(total)
      ```
      **Output:** `6.0`

    - `checkout_queue(...)`: This function accepts any number of positional string arguments representing customer names. It returns a queue (`deque`) of names in the order they were passed.
      
      Example:
      ```python
      queue = checkout_queue('John', 'David', 'Hu')
      print(queue)
      ```
      **Output:** `deque(['John', 'David', 'Hu'])`

    - `add_customer_cart(name, ...)`: This function accepts a positional argument `name` (customer name) and any number of keyword arguments representing items and their prices. It adds `name: {food: price, ...}` to `today_sale` and prints a message.
      
      Example:
      ```python
      add_customer_cart('John', pizza=5.0, chocolate=11.6)
      ```
      **Output:** `Added John cart into today sale`

    - `lookup_cart(name)`: This function accepts a positional argument `name`, looks up their cart in `today_sale`, and prints each item, its price, and the total price. It also applies any applicable discounts.
      
      Example:
      ```python
      lookup_cart('John')
      ```
      **Output:**
      ```
      John cart contains:
      pizza: 5.0
      chocolate: 11.6
      Total price: 16.6
      ```

    - `remove_item(name, item)`: This function accepts two positional arguments: `name` (customer name) and `item` (string representing an item in their cart). If the item is found, it is removed from their cart, and a message is printed. If the item is not found, print `"Item not found"`.

    - `apply_discount(name)`: This function takes a positional argument `name` and applies a 10% discount for each condition met:
      1. Name length is divisible by 3.
      2. Name starts with a vowel.
      
      The function prints the applied discounts and returns the total discount percentage.

    - `add_item(name, item, price=0)`: This function accepts a positional argument `name` and adds `item` with `price` to their cart. If the item has no price (default `0`), it prints a message indicating the item is free. If the name is not found in `today_sale`, print `"Name not found"`.
      
      Example:
      ```python
      add_item('Alice', 'bread')
      ```
      **Output:** `Added bread to Alice's cart (free item)`

    - `sale(queue)`: This function takes a `deque` object and processes checkout for each person in the queue. It prints the current queue, the person checking out, and their final total after applying discounts. The function continues until the queue is empty.
      
      Example:
      ```python
      sale(line_up)
      ```
      **Output:**
      ```
      Current queue: deque(['John', 'David', 'Alice'])
      Serving John
      John cart contains:
      egg: 1.0
      Total price: 1.0
      ...
      No more in queue
      ```

2. Create a script `main.py` that performs the following operations:
    - Add customers and their initial carts using `add_customer_cart()`.
    - Create a checkout queue using `checkout_queue()`.
    - Modify carts using `add_item()` and `remove_item()`.
    - Process checkout using `sale()`.

    Example operations:
    ```python
    from shopping import *
    
    # Add some customers with their initial carts
    add_customer_cart('David', apple=10.0, egg=1.0, sushi=11.8)
    add_customer_cart('John', banana=5.0, egg=1.0)
    add_customer_cart('Alice', orange=3.0, milk=2.5)
    
    # Create checkout queue
    line_up = checkout_queue('John', 'David', 'Alice')
    
    # Modify some carts
    add_item('David', 'candy', 2.5)
    remove_item('John', 'banana')
    add_item('Alice', 'bread')  # Free item
    
    # Process the sale
    sale(line_up)
    ```

Submission

Submit a zip file containing all the code files on Canvas.Naming Convention: CWID_LastName_Firstname.zipYour zipped folder should contain the following files:
                  | > shopping.py
                  | > main.py
                  | > test.py
                  | > test.sh (for UNIX-based systems)
                  | > win_test.bat (for Windows systems)

## Grading
1. All points add up to a total of 100 points possible as detailed below. Partial credit will be given where applicable.

| Points | Description |
| --- | --- |
|50|Environment setup and Lab Submission|
|20|All required files are submitted|
|30|All unit tests passed|
        