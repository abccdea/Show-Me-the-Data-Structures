from collections import deque

class LRU_Cache(object):

    def __init__(self, capacity):
       # Initialize class variables
       self.cache_cap = capacity
       self.cache_val = {}
       self.cache_order = deque()

    def get(self, key):
        # Retrieve item from provided key. Return -1 if non existant.
        if key is None:
            return -1

        return self.cache_val.get(key, -1)

    def set(self, key, value):
        if (self.cache_cap==0):
            print("Cannot add. Cache has empty capacity")
            return
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if len(self.cache_order) >= self.cache_cap:
            del self.cache_val[self.cache_order.popleft()]
        self.cache_order.append(key)
        self.cache_val[key] = value
'''
For testing
'''
print("Test case 1:")
our_cache = LRU_Cache(2)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 2)
print(our_cache.cache_val)
print(our_cache.get(1))       # returns -1
print(our_cache.get(2))       # returns 2
print(our_cache.get(None))    # return -1      
print("Test case 2:")
empty_cache = LRU_Cache(0)
empty_cache.set(1, 1)    # returns Cannot add. Cache has empty capacity
empty_cache.get(1)
print("Test case 3:")
update_cache = LRU_Cache(2)
update_cache.set(1, 1)
update_cache.set(2, 2)
update_cache.set(1, 11)
print(update_cache.get(1))       # returns 11
print(update_cache.get(2))       # returns 2