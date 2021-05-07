import pickle
# py_dict = {'name': 'harry', 'salary': 9000, 'language': 'Hindi'}
# myfile = open('filename', 'wb')
# pickle.dump(py_dict, myfile)
# myfile.close()


# Pickling a python object
# cars = ["Audi", "BMW", "Maruti Suzuki", "Harryti Tuzuki"]
# file = "mycar.pkl"
# fileobj = open(file, 'wb')
# pickle.dump(cars, fileobj)
# fileobj.close()

file = "mycar.pkl"
fileobj = open(file, 'rb')
mycar = pickle.load(fileobj)
print(mycar)
print(type(mycar))


# pickle.loads = ?
