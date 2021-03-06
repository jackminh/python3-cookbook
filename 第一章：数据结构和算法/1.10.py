#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

# 删除序列相同元素并保持顺序
# 如果序列上的值都是 hashable 类型，那么可以很简单的利用集合或者生成器来解决这个问题


def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


a = [1, 5, 2, 1, 9, 1, 5, 10]
print(list(dedupe(a)))


# 这个方法仅仅在序列中元素为 hashable 的时候才管用。 如果你想消除元素不可哈希(比如 dict 类型)的序列中重复元素的话，你需要将上述代码稍微改变一下，就像这样：
def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


# 这里的key参数指定了一个函数，将序列元素转换成 hashable 类型。
a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
a1 = list(dedupe(a, key=lambda d: (d['x'], d['y'])))
print(a1)
a2 = list(dedupe(a, key=lambda d: d['x']))
print(a2)
a3 = list(dedupe(a, key=lambda d: d['x']))
print(a3)
# 如果你仅仅是想消除重复元素，通常可以简单的构建一个集合。
a = [1, 24, 5, 55, 5, 454, 1, 5, 6]
a1 = set(a)
print(a1)
"""
然而，这种方法不能维护元素的顺序，生成的结果中的元素位置被打乱。而上面的方法可以避免这种情况。
"""
