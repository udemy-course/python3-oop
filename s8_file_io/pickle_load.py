
import pickle

# Restore from a file
f = open('pickle_test', 'rb')
data = pickle.load(f)
print(data)
f.close()


# Restore from a string
# data = pickle.loads(s)