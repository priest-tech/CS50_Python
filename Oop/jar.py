class Jar:
    #__init__ should intialize a cookie jar with a 
    # given capacity, that represents the maximum number of cookies
    # If capacity is not a non-negative int, though, 
    # _init__ should instead raise a ValueError.
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a non-negative int")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        #should return a str with n 🍪, where n is the number of cookies
        #in the jar. For instance if there are 3 cookies in the jar,
        #it should return "🍪🍪🍪"
        return "🍪" * self._size
        

    def deposit(self, n):
        #should add n cookies to the jar. If adding n would
        #make the jar bigger than its capacity, the jar should
        #raise a valueerror
        if not isinstance(n, int) or n < 0:
            raise ValueError("n must be a non-negative int")
        if self._size + n > self._capacity:
            raise ValueError("Not enough capacity")
        self._size += n
        

    def withdraw(self, n):
        #should remove n cookies from the jar. If removing n
        if not isinstance(n, int) or n < 0:
            raise ValueError("n must be a non-negative int")
        if self._size - n < 0:
            raise ValueError("Not enough cookies in the jar")
        self._size -= n
        

    @property
    def capacity(self):
        #should return the capacity of the jar
        return self._capacity
        

    @property
    def size(self):
        #should return the number of cookies actually in the jar intially 0

        return self._size