# f = open("nick.txt", "w")
# a = f.write("Harry bhai bahut achhe hain\n")
# print(a)
# f.close()

# f = open("nick.txt", "a")
# a = f.write("Harry bhai bahut achhe hain\n")
# print(a)
# f.close()


# Handle read and write both
f = open("nick.txt", "r+")
print(f.read())
f.write("thank you")
