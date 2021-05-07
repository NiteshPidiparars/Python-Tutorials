# for c in a:
#       print (a)
# #Here a is an iterable.

# For Example:
# def getNum (x):
#     for i in range(x):
#         yield i

# seq = getNum (2)
# print(seq.__next__())
# print(seq.__next__())
# print(seq.__next__())


"""
Iterable - __iter__() or __getitem__()
Iterator - __next__()
Iteration -

"""


def gen(n):
    for i in range(n):
        yield i


g = gen(3)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())


# for i in g:
#     print(i)

h = 546546
ier = iter(h)
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
# for c in h:
#     print(c)
