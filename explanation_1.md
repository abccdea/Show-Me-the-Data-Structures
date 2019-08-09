As I have to design a data structure for a Least Recently Used (LRU) cache with O(1) operations. It's the best option to go with dictionary in python which has constant time access of values with particular key. To keep track of the order of the values I have created a queue with the help of python deque, which allows constant time popleft().

Time efficiency- Getting, Inserting and removing the values from the cache takes O(1).

Space efficiency- Since the amount of memory used depends on size of cache, it would take O(n).