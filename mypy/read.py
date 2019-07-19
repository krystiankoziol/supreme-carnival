import pickle


def deserialize_pickle (pickle_file):
    with open(pickle_file,'rb') as f:
        iris = pickle.load(f)
    return iris


if __name__ == '__main__':
    iris = deserialize_pickle('iris.pickle')
    print (iris)
