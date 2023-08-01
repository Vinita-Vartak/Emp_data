class CommonMethod:
    def __str__(self):
        return f"\n{self.__dict__}"
    
    def __repr__(self):
        return str(self)
    

class Employee(CommonMethod):
    def __init__(self, eid, ename, esalary):
        self.EmpID = eid
        self.EmpName = ename
        self.EmpSalary = esalary
        


