# text = "Python tutorial for absolute beginners."
# t = text.split()
# print(t)


# class Date:
#     def __init__(self, year, month, day):
#         self.year = year
#         self.month = month
#         self.day = day


# @classmethod
# def from_dash(cls, string):
#     return cls(*string.split("-"))


# date1 = Date.from_dash("2008-12-5")
# print(date1.year)
# #Output: 2008


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

    @classmethod
    def from_dash(cls, string):
        # params = string.split("-")
        # print(params)
        # return cls(params[0], params[1], params[2])
        return cls(*string.split("-"))


harry = Employee("Harry", 255, "Instructor")
rohan = Employee("Rohan", 455, "Student")
karan = Employee.from_dash("Karan-480-Student")

print(karan.no_of_leaves)
# rohan.change_leaves(34)
#
# print(harry.no_of_leaves)
