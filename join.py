# The syntax of the join() method is:
#     string.join(iterable)

# join() with lists
numList = ['1', '2', '3', '4']
separator = ', '
print(separator.join(numList))

myDictionary = {"name": "Jack", "country": "America"}
separator = "_separator_"
print(separator.join(myDictionary))

# it shows --> Traceback (most recent call last): File "./prog.py", line 3, in TypeError: sequence item 1: expected str instance, int found
# inputlist = ["Test1", 13, "Test2", 24, "Test3", 100, "Test4"]
# sep = '_'
# out = sep.join(inputlist)
# print(out)

lis = ["John", "cena", "Randy", "orton",
       "Sheamus", "khali", "jinder mahal"]

# for item in lis:
#     print(item, "and", end=" ")

a = ", ".join(lis)
print(a, "other wwe superstars")
