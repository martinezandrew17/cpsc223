import shapes.circle as circle
import shapes.rectangle as rectangle
import shapes.triangle as triangle

def main():
    shape = input("Choose a shape (circle, rectangle, triangle): ").strip().lower()

    if shape == 'circle':
        radius = float(input("Enter the radius: "))
        print(f'Area: {circle.area(radius)}')
        print(f'Circumference: {circle.circumference(radius)}')
    elif shape == 'rectangle':
        length = float(input("Enter the length: "))
        width = float(input("Enter the width: "))
        print(f"Area: {rectangle.area(length, width)}")
        print(f'Circumference: {rectangle.perimeter(length, width)}')
    elif shape == 'triangle':
        base = float(input('Enter the base: '))
        height = float(input('Enter the height: '))
        side1 = float(input('Enter side 1: '))
        side2 = float(input('Enter side 2: '))
        side3 = float(input('Enter side 3: '))
        print(f"Area: {triangle.area(base, height)}")
        print(f'Perimeter: {triangle.perimeter(side1, side2, side3)}')
    else: 
        print("Invalid Shape. ")

if __name__ == "__main__":
    main()