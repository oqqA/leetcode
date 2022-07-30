# 146. LRU Cache
# https://leetcode.com/problems/lru-cache/

class LRUCache:
    _arr = {}
    _arr_age = {}
    _age = 0
    _capacity = 0

    def __init__(self, capacity: int):
        self._arr = {}
        self._arr_age = {}
        self._age = 0
        self._capacity = capacity

    def get(self, key: int) -> int:
        if self._arr.get(key) is not None:
            self._age += 1
            self._arr_age[key] = self._age

            return self._arr[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if self._arr.get(key) is None and len(self._arr) == self._capacity:
            min_key = 0
            min_val = float('inf')

            for k, v in self._arr_age.items():
                if v < min_val:
                    min_val = v
                    min_key = k

            del self._arr_age[min_key]
            del self._arr[min_key]

        self._age += 1
        self._arr_age[key] = self._age

        self._arr[key] = value


# tests

def combo_test(class_, methods, values):
    obj = None
    reuslt = []

    for index, method in enumerate(methods):
        if method == class_.__name__:
            obj = class_(*values[index])
            reuslt.append(None)
        else:
            geted_method = getattr(obj, method)
            res = geted_method(*values[index])
            reuslt.append(res)

    return reuslt


# def test():
#     obj = LRUCache(2)
#     obj.put(1, 6)
#     obj.put(2, 7)
#     print(obj.get(1))
#     print(obj._arr, obj._arr_age)
#     obj.put(3, 8)
#     print(obj._arr, obj._arr_age)
#     print(obj.get(2))
#     assert False


def test1():

    methods = ["LRUCache", "put", "put", "get", "put",
               "get", "put", "get", "get", "get"]

    values = [[2], [1, 1], [2, 2], [1], [3, 3],
              [2], [4, 4], [1], [3], [4]]

    expected = [None, None, None, 1, None,
                -1, None, -1, 3, 4]

    result = combo_test(LRUCache,
                        methods,
                        values)

    print(result)

    assert result == expected


def test2():

    methods = ["LRUCache", "put", "put", "get", "put",
               "get", "put", "get", "get", "get"]

    values = [[2], [1, 0], [2, 2], [1], [3, 3],
              [2], [4, 4], [1], [3], [4]]

    expected = [None, None, None, 0, None, -1, None, -1, 3, 4]

    result = combo_test(LRUCache,
                        methods,
                        values)

    print(result)

    assert result == expected
