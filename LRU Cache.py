class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.empty = capacity
        self.keys = dict()
        self.cache = []

    def get(self, key: int) -> int:
        if self.keys.get(key) is not None:
            if key in self.cache:
                self.cache.remove(key)
            self.cache.insert(0, key)
            return self.keys[key]

        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.keys:
            self.keys[key] = value
            self.cache.remove(key)
            self.cache.insert(0, key)
        else:
            if self.empty != 0:
                self.keys[key] = value
                self.empty -= 1
                self.cache.insert(0, key)
            else:
                self.keys.pop(self.cache[-1])
                self.cache.pop()
                self.keys[key] = value
                self.cache.insert(0, key)   