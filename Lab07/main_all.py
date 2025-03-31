from shapes import circle
from shapes import rectangle
from shapes import triangle

def main():
    radius = 5 
    print(f'Circle Area: {circle.area(radius)}')
    print(f'Circle Circumference: {circle.circumference(radius)}')

    length, width = 4, 6
    print(f"Rectangle Area: {rectangle.area(length, width)}")
    print(f'Rectangle Perimeter: {rectangle.perimeter(length, width)} ')

    try: 
        print(triangle.area(3, 4))
    except NameError:
        print("Triangle module is not imported due to __all__ restriction.")
    
if __name__ == "__main__":
    main()