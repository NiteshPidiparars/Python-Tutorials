# Typecasting in Python :
abc = 5
abc2 = '45'
abc3 = 55.95
xyz = 5.0

abc4 = int(abc2)

print(abc+abc4)  # Output : 50
print(abc+int(abc2))  # Output : 50

print(float(abc)+xyz)  # It will add 5.0 + 5.0 and will return 10.0

# It will give an error as abc has been changed into string.
print(str(abc)+45)
