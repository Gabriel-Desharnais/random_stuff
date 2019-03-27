#! /usr/bin/python3

#This file contains the lru Last recently used module that manages the
# memory cache

class LRUModule:
    def __init__(self, cacheSize=5, host =None, ):
        # We are going to init the cache list with the right lenght
        # that way the module doesn't need to check the lenght of
        # list every time something is edited in the cache
        self.cacheLenght = cacheSize
        self.cacheKey = [None for a in range(self.cacheLenght)]
        self.OUEI = 0 # This index points to the oldest used element in cache

        # Using normal non ordered dict for acess speed reason
        self.cache = {}


        if host:
            # connect to host
            pass



    def __getitem__(self,key):
        # This function should return a keyError if the key is not cached
        value = self.cache[key]
        self.moveKeyToLRU(key) #It would be great to do that after return
        self.OUEI = (self.OUEI + 1) % self.cacheLenght #It would be great to do that after return
        return value
    def __setitem__(self,key, value):
        #This function add or changes the value of a key
        if key in self.cache:
            # Change the value
            self.cache[key] = value
            self.moveKeyToLRU(key)
            self.OUEI = (self.OUEI + 1) % self.cacheLenght
        else:
            # Add the value
            self.cache[key] = value
            oldKey = self.cacheKey[self.OUEI] # save old key for deletion later
            self.cacheKey[self.OUEI] = key
            self.OUEI = (self.OUEI + 1)%self.cacheLenght #It would be great to do that after return
            try:
                del self.cache[oldKey]
            except KeyError:
                pass

    def moveKeyToLRU(self, key):
        # Change order in cacheKey
        i = self.cacheKey.index(key)
        lui = (self.OUEI -1) % self.cacheLenght
        if lui < i:
            self.cacheKey.insert(self.OUEI, self.cacheKey.pop(i))
        else:
            self.cacheKey.insert(lui, self.cacheKey.pop(i))
    def accessDecorator(self, func):
        # apply this deco on your function used to read your non cached data
        def wrapper(key):
            # first check if the data is cached
            if key in self.cache:
                return self[key]
            else:
                r = self[key] = func(key)
                return r
        return wrapper
    def writeDecorator(self, func):
        # apply this deco on your function used to write your non cached data
        def wrapper(key, value):
            # first check if the data is cached
            self[key] = value
            func(key, value)
        return wrapper


if __name__ == "__main__":
    a = LRUModule()
    # fill the LRU
    a["1"] = 1
    a["2"] = 2
    a["3"] = 3
    a["4"] = 4
    a["5"] = 5
    a["6"] = 6
    print("Cache is the right size ?", len(a.cache) == 5)
    print("The oldest element has been removed from cache", not "1" in a.cache)
    print("The oldest element has been removed from keylist", not "1" in a.cacheKey )
    print("The oldest element in cache is '2'", a.cacheKey.index('2') == a.OUEI )
    # Read element "2"
    a["2"]
    print("The oldest element in cache should be 3", a.cacheKey.index('3') == a.OUEI )

    #Try read/write decorator
    a = LRUModule(cacheSize=2)
    nonCached = {1:1,2:2,3:3,4:4,5:5,6:6,7:7}

    @a.accessDecorator
    def get(key):
        return nonCached[key]

    @a.writeDecorator
    def write(key, value):
        nonCached[key] = value

    print("getting non cached data works", get(1)==1)
    print("data has been cached after read", 1 in a.cacheKey )

    write(8, "s")
    print("Data has been written in cache", 8 in a.cacheKey)
    print("Data has been written in noncache", nonCached[8] == "s")
