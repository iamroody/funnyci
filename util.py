import pickle

class util:
    @staticmethod
    def getDictionaryFromFile(path):
        try:
            f = open(path, 'r')
            version = pickle.load(f)
            f.close()
            return version
        except EOFError:
            return {}

    @staticmethod
    def writeDictionaryToFile(dictionary, path):
        f = open(path, 'wb')
        pickle.dump(dictionary, f)
        f.close()
    