# -*- coding: utf-8 -*-
"""
    单例
    ~~~~~~~~~~~~~~~~~~
    0. __new__ 方法实现
    1. 装饰器实现
    2. metaclass 实现
    3. 简单函数实现
"""


# 0. __new__() magic method 实现
class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instanced'):
            cls._instanced = super().__new__(cls, *args, **kwargs)
        return cls._instanced
# ----------------------------------------------------------------


# 1. 装饰器实现
def singletonify(cls):
    instances = {}

    def _(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return _


def singletonify2(cls):
    def _(*args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = cls(*args, **kwargs)
        return cls._instance
    return _
# ----------------------------------------------------------------


# 2. metaclass 实现单例
class SingletonMeta(type):
    def __init__(self, *args, **kwargs):
        self.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super().__call__(*args, **kwargs)
        return self.__instance


class GooHoo(metaclass=SingletonMeta):
    def __init__(self):
        pass
# ----------------------------------------------------------------


# 3. 简单函数实现, From Peter Norvig http://norvig.com/python-iaq.html #
def singleton(instance):
    klass = instance.__class__
    if hasattr(klass, '__instanced'):
        msg = "{} is a Singleton class but is already instantiated"
        raise ValueError(msg.format(klass))
    klass.__instanced = True


class Test1:
    "A singleton class to do something ..."
    def __init__(self):
        singleton(self)
# ----------------------------------------------------------------  #


if __name__ == '__main__':
    a = GooHoo()
    b = GooHoo()
    print(a, b)
    assert a is b
