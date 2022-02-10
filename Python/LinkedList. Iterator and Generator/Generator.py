import random

def generator(size, *args, function = random.randint): 
    for i in range(size):
        yield function(*args)
