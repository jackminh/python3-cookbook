#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

# 合并拼接字符串，如何你想将几个小的字符串合并为一个大的字符串
parts = ['Is', 'Chicago', 'Not', 'Chicago?']
print(''.join(parts), ' '.join(parts), ','.join(parts))
# 加号(+)操作符在作为一些复杂字符串格式化的替代方案的时候通常也工作的很好，比如：
a = 'Is Chicago'
b = 'Not Chicago'
print('{} {}'.format(a, b))
"""
字符串合并可能看上去并不需要用一整节来讨论。 但是不应该小看这个问题，程序员通常在字符串格式化的时候因为选择不当而给应用程序带来严重性能损失。
最重要的需要引起注意的是，当我们使用加号(+)操作符去连接大量的字符串的时候是非常低效率的，
因为加号连接会引起内存复制以及垃圾回收操作。 特别的，你永远都不应像下面这样写字符串连接代码：
s = ''
for p in parts:
    s += p
这种写法会比使用 join() 方法运行的要慢一些，因为每一次执行+=操作的时候会创建一个新的字符串对象。
你最好是先收集所有的字符串片段然后再将它们连接起来。
"""
data = ['ACME', 50, 91.1]
print(','.join(str(d) for d in data))
# 同样还得注意不必要的字符串连接操作。有时候程序员在没有必要做连接操作的时候仍然多此一举。比如在打印的时候：
print('a' + ':' + 'b' + ':' + 'c')  # Ugly
print(':'.join(['a', 'b', 'c']))  # Still ugly
print('a', 'b', 'c', sep=':')  # Better

"""
如果两个字符串很小，那么第一个版本性能会更好些，因为I/O系统调用天生就慢。
另外一方面，如果两个字符串很大，那么第二个版本可能会更加高效，
因为它避免了创建一个很大的临时结果并且要复制大量的内存块数据。
还是那句话，有时候是需要根据你的应用程序特点来决定应该使用哪种方案。
最后谈一下，如果你准备编写构建大量小字符串的输出代码，
你最好考虑下使用生成器函数，利用yield语句产生输出片段。比如：

def sample():
    yield 'Is'
    yield 'Chicago'
    yield 'Not'
    yield 'Chicago?'
这种方法一个有趣的方面是它并没有对输出片段到底要怎样组织做出假设。
例如，你可以简单的使用 join() 方法将这些片段合并起来：
text = ''.join(sample())
或者你也可以将字符串片段重定向到I/O：
for part in sample():
    f.write(part)
"""


def sample():
    yield 'Is'
    yield 'Chicago'
    yield 'Not'
    yield 'Chicago?'


def combine(source, maxsize):
    parts = []
    size = 0
    for part in source:
        parts.append(part)
        size += len(part)
        if size > maxsize:
            yield ''.join(parts)
            parts = []
            size = 0
        yield ''.join(parts)


# 结合文件操作
with open('filename.txt', 'w') as f:
    for part in combine(sample(), 10):
        f.write(part)
