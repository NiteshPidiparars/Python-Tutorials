# F strings
import math

me = "Nick"
a1 = 3
# a = "this is %s %s"%(me, a1)
# a = "This is {1} {0}"
# b = a.format(me, a1)
# print(b)
a = f"this is {me} {a1} {math.cos(65)}"  # f means formated string
# time
print(a)
