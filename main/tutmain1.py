# tutmain1.py
print("__name__ in tutmain1.py is set to"+__name__)


def printhar(string):
    return f"Ye string harry ko de de thakur {string}"


def add(num1, num2):
    return num1 + num2 + 5


print("aand the name is", __name__)

if __name__ == '__main__':
    print(printhar("Harry1"))
    o = add(4, 6)
    print(o)
