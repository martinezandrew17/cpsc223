import unittest
from collections import deque
from shopping import (
    today_sale,
    get_total_item,
    check_out_queue,
    add_customer_cart,
    look_up_customer_cart,
    sale,
    remove_item,
    add_item,
    apply_discount
)

class TestSaleFunctions(unittest.TestCase):
    def setUp(self):
        today_sale.clear()

    def test_get_total_item(self):
        cart = {'apple': 10.0, 'egg': 1.0, 'sushi': 11.8}
        self.assertEqual(get_total_item(cart), 22.8)

    def test_get_total_item_empty(self):
        cart = {}
        self.assertEqual(get_total_item(cart), 0)

    def test_check_out_queue(self):
        queue = check_out_queue('John', 'David')
        self.assertIsInstance(queue, deque)
        self.assertEqual(list(queue), ['John', 'David'])

    def test_check_out_queue_empty(self):
        queue = check_out_queue()
        self.assertIsInstance(queue, deque)
        self.assertEqual(len(queue), 0)

    def test_add_customer_cart(self):
        add_customer_cart('David', apple=10.0, egg=1.0, sushi=11.8)
        self.assertIn('David', today_sale)
        self.assertEqual(today_sale['David'], {'apple': 10.0, 'egg': 1.0, 'sushi': 11.8})

    def test_add_customer_cart_no_items(self):
        add_customer_cart('Alice')
        self.assertIn('Alice', today_sale)
        self.assertEqual(today_sale['Alice'], {})

    def test_look_up_customer_cart(self):
        add_customer_cart('David', apple=10.0, egg=1.0, sushi=11.8)
        cart = today_sale['David']
        self.assertDictEqual(cart, {'apple': 10.0, 'egg': 1.0, 'sushi': 11.8})

    def test_look_up_customer_cart_not_exist(self):
        with self.assertRaises(KeyError):
            look_up_customer_cart('NonExistent')

    def test_sale(self):
        add_customer_cart('David', apple=10.0, egg=1.0, sushi=11.8)
        add_customer_cart('John', banana=5.0, egg=1.0)
        queue = check_out_queue('John', 'David')
        sale(queue)
        self.assertEqual(len(queue), 0)

    def test_sale_empty_queue(self):
        queue = check_out_queue()
        sale(queue)
        self.assertEqual(len(queue), 0)

    def test_remove_item_success(self):
        add_customer_cart('David', apple=10.0, egg=1.0)
        remove_item('David', 'apple')
        self.assertNotIn('apple', today_sale['David'])

    def test_remove_item_not_in_cart(self):
        add_customer_cart('David', apple=10.0)
        remove_item('David', 'banana')
        self.assertEqual(today_sale['David'], {'apple': 10.0})

    def test_remove_item_customer_not_exist(self):
        remove_item('NonExistent', 'apple')
        self.assertNotIn('NonExistent', today_sale)

    def test_add_item_with_price(self):
        add_customer_cart('David')
        add_item('David', 'apple', 10.0)
        self.assertEqual(today_sale['David']['apple'], 10.0)

    def test_add_item_without_price(self):
        add_customer_cart('David')
        add_item('David', 'apple')
        self.assertEqual(today_sale['David']['apple'], 0)

    def test_add_item_customer_not_exist(self):
        add_item('NonExistent', 'apple', 10.0)
        self.assertNotIn('NonExistent', today_sale)

    def test_apply_discount_name_length_divisible_by_3(self):
        discount = apply_discount('Bob')  # length = 3
        self.assertEqual(discount, 10)

    def test_apply_discount_starts_with_vowel(self):
        discount = apply_discount('Emma')  # starts with 'E'
        self.assertEqual(discount, 10)

    def test_apply_discount_multiple_conditions(self):
        discount = apply_discount('Alicia')  # starts with 'A' and length=5
        self.assertEqual(discount, 20)

    def test_apply_discount_no_discount(self):
        name = "Glyn"  # Does not meet any discount conditions
        discount = apply_discount(name)
        self.assertEqual(discount, 0)  # Expecting no discount


    def test_multiple_operations_sequence(self):
        # Add customers
        add_customer_cart('David', apple=10.0, egg=1.0)
        add_customer_cart('John', banana=5.0)
        
        # Modify carts
        add_item('David', 'sushi', 11.8)
        remove_item('John', 'banana')
        
        # Check final state
        self.assertEqual(today_sale['David'], 
                        {'apple': 10.0, 'egg': 1.0, 'sushi': 11.8})
        self.assertEqual(today_sale['John'], {})

    def test_queue_processing_order(self):
        add_customer_cart('Alice', apple=1.0)
        add_customer_cart('Bob', banana=2.0)
        add_customer_cart('Charlie', orange=3.0)
        
        queue = check_out_queue('Alice', 'Bob', 'Charlie')
        self.assertEqual(list(queue), ['Alice', 'Bob', 'Charlie'])
        
        # Process first customer
        name = queue.popleft()
        self.assertEqual(name, 'Alice')
        self.assertEqual(len(queue), 2)

if __name__ == '__main__':
    unittest.main()