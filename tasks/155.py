# 155. Min Stack
# https://leetcode.com/problems/min-stack/

class MinStack:

    _stack = []
    _count = 0
    _min_index = 0

    def __init__(self):
        self._stack = []
        self._count = 0
        self._min_index = 0

    def push(self, val: int) -> None:
        self._stack.append(val)
        self._count += 1
        if val < self._stack[self._min_index]:
            self._min_index = self._count - 1

    def pop(self) -> None:
        self._stack.pop()
        self._count -= 1

        if self._min_index <= self._count and self._count != 0:
            self._min_index = self._stack.index(min(self._stack))

    def top(self) -> int:
        return self._stack[self._count - 1]

    def getMin(self) -> int:
        return self._stack[self._min_index]


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


def test():
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    print(obj.getMin(), obj._stack)
    obj.pop()
    print(obj.top(), obj._stack)
    print(obj.getMin(), obj._stack)

    assert True


def test1():
    methods = ["MinStack", "push", "push", "push",
               "getMin", "pop", "top", "getMin"]

    values = [[], [-2], [0], [-3],
              [], [], [], []]

    expected = [None, None, None, None,
                -3, None, 0, -2]

    result = combo_test(MinStack,
                        methods,
                        values)

    # print(result)

    assert result == expected


def test2():
    methods = ["MinStack", "push", "push", "push",
               "top", "pop", "getMin", "pop",
               "getMin", "pop", "push", "top",
               "getMin", "push", "top", "getMin",
               "pop", "getMin"]

    values = [[], [2147483646], [2147483646], [2147483647],
              [], [], [], [],
              [], [], [2147483647], [],
              [], [-2147483648], [], [],
              [], []]

    expected = [None, None, None, None,
                2147483647, None, 2147483646, None,
                2147483646, None, None, 2147483647,
                2147483647, None, -2147483648, -2147483648,
                None, 2147483647]

    result = combo_test(MinStack,
                        methods,
                        values)

    # print(result)

    assert result == expected
