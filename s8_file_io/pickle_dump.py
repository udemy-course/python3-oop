
import pickle

data = {
    'name': 'somebody',
    'age': 30
}
f = open('pickle_test', 'wb')
pickle.dump(data, f)
f.close()

# s = pickle.dumps(data)