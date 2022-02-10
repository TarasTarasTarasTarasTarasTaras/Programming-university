class Observer:
    def __init__(self):
        self.__listeners = dict()
    
    def attach(self, key, function):
        self.__listeners[key] = function

    def detach(self, key):
        self.__listeners.pop(key)

    def get_listeners(self):
        return self.__listeners
