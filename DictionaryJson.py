import json
import pickle

class example_class:
    data = {
        "user":{"name":"Luis",
            "Subject":"SoftwareDevelopment"
        }
    }

my_object = example_class()
                               ######### ATTENTION!, the follwoing is using pickle, not json###########
my_pickled_object = pickle.dumps(my_object)  # Pickling the object
print(f"This is my pickled object:\n{my_pickled_object}\n")
my_object.a_dict = None

my_unpickled_object = pickle.loads(my_pickled_object)  # Unpickling the object
print(
    f"This is a_dict of the unpickled object:\n{my_unpickled_object.data}\n")
