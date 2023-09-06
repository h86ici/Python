import sys 
import os

sys.path.append(os.path.relpath("D:\\Github\\Python\\Code Examples\\Python_Class"))
import Class_example_Triangle_area as tri

a, b, c = 3, 4, 5
if tri.Triangle.is_valid(a, b, c):
    triangle1=tri.Triangle(a, b, c)
    print('The perimeter is %.3f' % triangle1.perimeter())
    print('The area is %.3f' % triangle1.area())