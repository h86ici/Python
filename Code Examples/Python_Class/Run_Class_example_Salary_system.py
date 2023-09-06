import sys 
import os

sys.path.append(os.path.relpath("D:\\Github\\Python\\Code Examples\\Python_Class"))
import Class_example_Salary_system as salary

person = salary.Manager('劉一', 'Manager')
print('%s為 %s, 本月工資為: ￥%s元' % (person.name, person.title, person.get_salary()))