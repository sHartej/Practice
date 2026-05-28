import math

shape = input("Which shape do you want to calculate (square/rectangle/triangle/circle)?: ")

if shape == 'square':
    num= float(input('Enter side lenght: '))
    num= num**2
    print(f'Area of your square is {num}')

elif shape == 'rectangle':
    l= float(input('Enter lenght: '))
    w= float(input('Enter width: '))
    num = l*w
    print(f'Area of your rectangle is {num}')

elif shape == 'triangle':
    h= float(input('Enter height: '))
    b= float(input('Enter base: '))
    num = (h*b)/2
    print(f'Area of your triangle is {num}')

elif shape == 'circle':
    r= float(input('Enter radius: '))
    num = math.pi * r**2
    print(f'Area of your circle is {num}')

else:
    print("Unknown shape. Please choose square, rectangle, triangle, or circle.")
