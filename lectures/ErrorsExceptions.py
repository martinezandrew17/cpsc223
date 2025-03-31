# while True:
#     print("Hello")

# while True:
#     try:
#         x = int(input("Enter a number: "))
#         y = 10/x
#         break
#     except ValueError:
#         print("Not a valid number.")
#     except ZeroDivisionError:
#         print("No cannot be divided by zero. ")

# import sys

# for arg in sys.argv[1:]:
#     try: 
#         f = open(arg, 'r')
#     except IOError:
#         print("Cannot open",arg)

# try:
#     raise Exception("spam", "eggs")
# except Exception as inst:
#     # print(type(inst))
#     # print(type.args)
#     print(type.inst)
#     x,y = inst.args
#     print("X = ", x)
#     print("Y = ", y)

# def this_fails():
#     x = 1/0
# try:
#     this_fails()
# except ZeroDivisionError as err:
#     print("Handling Run-Time Error", err)

# try:
#     raise NameError("Hi there")
# # except NameError:
# #     print("Nam error")

# def func():
#     raise IOError
# try:
#     func()
# except IOError as err:
#     raise RuntimeError('Failed to connect to DB') from err

# try:
#     open('database.sqlite')
# except:
#     raise RuntimeError("Failed") from None

# try: 
#     raise ZeroDivisionError
# except ZeroDivisionError:
#     print("Zero")
# finally:
#     print("Shutting Down!")

# def bool_return():
#     try:
#         return True
#     finally:
#         return False
    
# print(bool_return())

def divide(x,y):
    try: 
        result = x/y
    except ZeroDivisionError:
        print("Zero Divison error")
    else:
        print("Result is: ", result)
    finally:
        print("Executed done successfully!")

divide(10,0)