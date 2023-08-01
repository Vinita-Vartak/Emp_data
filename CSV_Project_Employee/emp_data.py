from emp_classes import Employee
import random


def get_name():
    name = ""
    for i in range(random.randint(4, 8)):  # 8
        single_char = chr(64 + random.randint(1, 26))
        name += single_char
    return name.title()

def get_emp_objs(no):
    emp_list = []
    for i in range(1, no + 1):
        eid = 100 + i
        ename = get_name()
        esal = random.randint(25000, 80000)
        emp_obj = Employee(eid=eid, ename=ename, esalary=esal)
        emp_list.append(emp_obj)
    return emp_list

# print(get_emp_objs())