# 622. Design Circular Queue
# https://leetcode.com/problems/design-circular-queue/


class MyCircularQueue:

    _size = 0
    _arr = []
    _first_index = -1
    _last_index = -1

    def __init__(self, k: int):
        self._arr = [None] * k
        self._size = k

    def enQueue(self, value: int) -> bool:
        new_last_index = (self._last_index + 1) % self._size

        if new_last_index != self._first_index:
            if self.isEmpty():
                self._first_index = new_last_index

            self._arr[new_last_index] = value

            self._last_index = new_last_index

            return True
        else:
            return False

    def deQueue(self) -> bool:
        if (not self.isEmpty()):
            self._arr[self._first_index] = None

            self._first_index = (self._first_index + 1) % self._size

            if self.isEmpty():
                self._first_index = -1
                self._last_index = -1

            return True
        else:
            return False

    def Front(self) -> int:
        result = self._arr[self._first_index]
        return result if result is not None else -1

    def Rear(self) -> int:
        result = self._arr[self._last_index]
        return result if result is not None else -1

    def isEmpty(self) -> bool:
        # return self._last_index == self._first_index
        return self._arr.count(None) == self._size

    def isFull(self) -> bool:
        return self._first_index == (self._last_index + 1) % self._size


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


def test1():
    methods = ["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue",
               "Rear", "isFull", "deQueue", "enQueue", "Rear"]

    values = [[3], [1], [2], [3], [4],
              [], [], [], [4], []]

    expected = [None, True, True, True, False,
                3, True, True, True, 4]

    assert combo_test(MyCircularQueue,
                      methods,
                      values) == expected


def test2():
    methods = ["MyCircularQueue", "enQueue", "Rear", "Rear",
               "deQueue", "enQueue", "Rear", "deQueue",
               "Front", "deQueue", "deQueue", "deQueue"]

    values = [[6], [6], [], [],
              [], [5], [], [],
              [], [], [], []]

    expected = [None, True, 6, 6,
                True, True, 5, True,
                -1, False, False, False]

    assert combo_test(MyCircularQueue,
                      methods,
                      values) == expected
