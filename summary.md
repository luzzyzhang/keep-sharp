# 需要注意的细节问题总结

1. 函数默认值初始化问题

    ```python
    def foo(bar=[]):
        bar.append('baz')
        return '%s, %i' % (bar, id(bar))

    >>> foo()
    "['baz'], 4318961736"
    >>> foo()
    "['baz', 'baz'], 4318961736"
    >>> foo()
    "['baz', 'baz', 'baz'], 4318961736"
    # 每次调用 foo(), bar使用同一个 list 对象，修改如下
    def foo(bar=None):
        if bar is None:
            bar = []
        bar.append('baz')
        return bar
    >>> foo()
    ['baz']
    >>> foo()
    ['baz']
    ```

2. 类型属性查找问题

    ```python
    class A(object):
        x = 1

    class B(A):
        pass

    class C(A):
        pass

    print(A.x, B.x, C.x)  # what's the output?

    B.x = 2
    print(A.x, B.x, C.x)  # what's print now?

    A.x = 3
    print(A.x, B.x, C.x)  # And now what output?
    ```
3. 变量作用域问题

    ```python
    >>> x = 10
    >>> def foo():
    ...     x += 1
    ...     print(x)
    >>> foo()   # 执行结果是什么？

    # 使用 list 做局部变量
    >>> lst = [1, 2, 3]
    >>> def foo1():
    ...     lst.append(5)    # this is work
    ... foo1()
    >>> lst
    # lst 的结果是？

    >>> lst2 = [1, 2, 3]
    >>> def foo2():
    ...     lst += [5]   # bombs!!!
    >>> foo2()  # 运行结果是？
    ```

4. 迭代进行时修改列表

    ```python
    odd = lambda x: bool(x % 2)
    numbers = [n for n in range(10)]
    for i in range(len(numbers)):
        if odd(numbers[i]):
            del numbers[i]   # BAD: Deleting item from a list while iterating over it

    Traceback (most recent call last):
               File "<stdin>", line 2, in <module>
    IndexError: list index out of range

    如果要得到期望结果可以使用列表推导式
    numbers[:] = [n for n in numbers if not odd(n)]  # beauty
    ```
5. 闭包变量值的延迟绑定问题

    ```python
    def create_multipliers():
        return [lambda x: i * x for i in range(4)]
    r = [m(2) for m in create_multipliers()]
    # r 的结果是？
    # 如何避免闭包延迟绑定？
    ```

6. 运行结果
    ```python
        class C:
            name = 'foo'

        c1 = C()
        c2 = C()

        c2.name = 'bar'
        C.name = 'baz'

        print('{}, {}, {}'.format(c1.name, c2.name, C.name))
    ```

7. 以下表达式区别

    `[x * 2 for x in lst]`
    `(x * 2 for x in lst)`
    `{x * 2 for x in lst}`




## 参考列表
[Python面试问题](https://www.toptal.com/python#hiring-guide)

[Python常见错误](https://github.com/zlotus/doc_mac_from_zer0/blob/master/python/python_i_dont_know.md)
