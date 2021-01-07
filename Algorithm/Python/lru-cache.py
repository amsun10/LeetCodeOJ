# https://leetcode.com/problems/lru-cache/
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.LRU = []

    def update_lru(self, key: int):
        if key not in self.LRU:
            self.LRU.append(key)
        else:
            self.LRU.remove(key)
            self.LRU.append(key)

    def get(self, key: int) -> int:
        result = self.cache.get(key, -1)
        if result != -1:
            self.update_lru(key)
        return result

    def put(self, key: int, value: int) -> None:
        self.cache[key] = value
        self.update_lru(key)

        if len(self.cache) > self.capacity:
            self.cache.pop(self.LRU[0])
            self.LRU.pop(0)


if __name__ == '__main__':
    lRUCache = LRUCache(2)
    # print(lRUCache.put(2, 1))  # cache is {1=1}
    # print(lRUCache.put(1, 1))  # cache is {1=1, 2=2}
    # print(lRUCache.get(2))     # return 1
    # print(lRUCache.put(4, 1))  # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
    # print(lRUCache.get(1))     # return 3
    # print(lRUCache.get(2))      # return 4

    print(lRUCache.put(1, 1))  # cache is {1=1}
    print(lRUCache.put(2, 2))  # cache is {1=1, 2=2}
    print(lRUCache.get(1))     # return 1
    print(lRUCache.put(3, 3))  # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
    print(lRUCache.get(2))     # return 3
    print(lRUCache.put(4, 4))      # return 4
    print(lRUCache.get(1))     # return 3
    print(lRUCache.get(3))     # return 3
    print(lRUCache.get(4))     # return 3

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)