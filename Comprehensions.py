#  listA = []
#  for a in range(50):
#      if a%5==0:
#          listA.append(a)

# listA = [a for a in range(50) if i%5==0]

#  alpha = {alpha for alpha in ["a", "a", "b", "c", "d", "d"]}

# Normaldict = {
#   0 : "item0",
#   1 : "item1",
#   2 : "item2",
#   3 : "item3",
#   4 : "item4",
# }
# Compdict = {i:f"Item {i}" for i in range(5)}
# def gener(n):
#     for i in range(n):
#         yield i

# a = gener(5)
# print(a.__next__())
# gener = (i for i in range(n))
# a = gener(5)
# print(a.__next__())


# ls = []
# for i in range(100):
#     if i%3==0:
#         ls.append(i)

# ls = [i for i in range(100) if i%3==0]
#
# print(ls)


# dict1 = {i:f"item {i}" for i in range(1, 10001) if i%100==0}
# dict1 = {i:f"Item {i}" for i in range(5)}
#
# dict2 = {value:key for key,value in dict1.items()}
# print(dict1,"\n", dict2)

# dresses = [dress for dress in ["dress1", "dress2","dress1",
#                                "dress2","dress1", "dress2"]]
# print(type(dresses))

evens = (i for i in range(100) if i % 2 == 0)
# print(evens.__next__())

# for item in evens:
#     print(item)
