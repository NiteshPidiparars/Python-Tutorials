# try:
#     #Run this code
# except Exception as error:
#     #Execute this code when there is an exception
# else:
#     #No Exception. Run this code

# def divide(a, b):
#     try:
#         print(f'{a}/{b} is {a / b}')
#     except ZeroDivisionError as e:
#         print(e)
#     else:
#         print("No Exception")
# divide(1, 2)

# try:
#     #Run this code
# except Exception as error:
#     #Execute this code when there is an exception
# else:
#    #No Exception. Run this code
# finally:
#    #Always run this code


f1 = open("nick.txt")

try:
    f = open("does2.txt")

except EOFError as e:
    print("Print eof error aa gaya hai", e)

except IOError as e:
    print("Print IO error aa gaya hai", e)

else:
    print("This will run only if except is not running")

finally:
    print("Run this anyway...")
    # f.close()
    f1.close()

print("Important stuff")
