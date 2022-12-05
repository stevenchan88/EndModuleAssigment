import pickle
a_dictionary = {"a": 1, "b": 2}
file_to_write = open("dictionary.pickle", "wb")
pickle.dump(a_dictionary,file_to_write)
file_to_write.close()

file_to_read= open("dictionary.pickle","rb")
dictionary_2 = pickle.load(file_to_read)
print(dictionary_2)
