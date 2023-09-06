import sys 
import os

sys.path.append(os.path.relpath("D:\\Github\\Python\\Code Examples\\Python_Class"))
from Class_example_Point_distance import *

main(1, 1, 1, 2, 2, 2)
print('Distance between P1 and P2: %.3f' % distance(1, 1, 3, 2, 2, 3))
