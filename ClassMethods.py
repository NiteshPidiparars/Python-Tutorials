# class myClass:
#     @classmethod
#     def myfunc(cls, arg1, arg2, ...):
#         ....

class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves


harry = Employee("Harry", 255, "Instructor")
rohan = Employee("Rohan", 255, "Student")

rohan.change_leaves(34)
print(harry.no_of_leaves)
