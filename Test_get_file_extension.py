import sys 
import os

sys.path.append(os.path.relpath("D:\\Github\\Python\\Code Examples"))
from Get_file_extension import get_file_extension

print(get_file_extension('test.txt', False))