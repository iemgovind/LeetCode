class MyHashMap:
    def __init__(self):
        """
        Initialize your hash map here.
        """
        self.size = 1000
        self.hash_map = [None] * self.size

    def put(self, key: int, value: int) -> None:
        """
        Inserts a (key, value) pair into the hash map. If the key already exists, update the value.
        """
        index = self._hash(key)
        if self.hash_map[index] is None:
            self.hash_map[index] = []
        for i, (k, v) in enumerate(self.hash_map[index]):
            if k == key:
                self.hash_map[index][i] = (key, value)
                return
        self.hash_map[index].append((key, value))

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
        """
        index = self._hash(key)
        if self.hash_map[index] is not None:
            for k, v in self.hash_map[index]:
                if k == key:
                    return v
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified key if it exists in the hash map.
        """
        index = self._hash(key)
        if self.hash_map[index] is not None:
            for i, (k, v) in enumerate(self.hash_map[index]):
                if k == key:
                    self.hash_map[index].pop(i)
                    return

    def _hash(self, key: int) -> int:
        """
        Internal hash function to convert key to an index in the hash map.
        """
        return key % self.size

# Create a new instance of MyHashMap
hash_map = MyHashMap()

# Test put() method
hash_map.put(1, 1)
hash_map.put(2, 2)
hash_map.put(3, 3)
print(hash_map.get(1))  # Expected output: 1
print(hash_map.get(2))  # Expected output: 2

# Test update value for an existing key using put() method
hash_map.put(1, 4)
print(hash_map.get(1))  # Expected output: 4

# Test remove() method
hash_map.remove(2)
print(hash_map.get(2))  # Expected output: -1
