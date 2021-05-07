# Dictionary is nothing but key value pairs
# d1 = {}
# print(type(d1))
# d2 = {"Harry": "Burger",
#       "Rohan": "Fish",
#       "SkillF": "Roti",
#       "Shubham": {"B": "maggie", "L": "roti", "D": "Chicken"}}
# d2["Ankit"] = "Junk Food"
# d2[420] = "Kebabs"
# print(d2)
# del d2[420]
# print(d2["Shubham"])
# d3 = d2.copy()
# del d3["Harry"]
# d2.update({"Leena":"Toffee"})
# print(d2.keys())
# print(d2.items())

d2 = {"programming": "the process of writing computer programs",
      "Java": "Java is a Object Oriented Programming langauge.",
      "Hibernate": "Hibernate is a ORM tool.",
      "Python": "it is an easy to write and better understanding programming language."}
key = input("Enter Dictionary key:")
if key in d2:
    print("Values is: " + d2[key])
else:
    print("invalid key!!")
