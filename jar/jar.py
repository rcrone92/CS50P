# import external libraries needed

# define global variables

class Jar:
    def __init__(self, capacity=12):
        if capacity < 1:
            raise ValueError("Invalid capacity.")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, cookies):
        if (self.size + cookies) > self._capacity:
            raise ValueError("Exceeds jar capacity.")
        self._size = self.size + cookies

    def withdraw(self, cookies):
        if cookies > self.size:
            raise ValueError("Exceeds jar capacity.")
        self._size = self.size - cookies

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size > self._capacity:
            raise ValueError("Exceeds jar capacity.")
        self._size = size

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 1:
            raise ValueError("Invalid capacity")
        self._capacity = capacity
