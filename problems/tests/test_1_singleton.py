# -*- coding: utf-8 -*-

from problems.p01_singleton import (Singleton, GooHoo,
                                    singletonify,  singletonify2)


def test_new_magic_singleton():
    a, b = Singleton(), Singleton()
    assert a is b


def test_decorator_singleton():

    @singletonify2
    class HeBa:
        pass

    @singletonify
    class BaHe:
        pass

    a, b = HeBa(), HeBa()
    c, d = BaHe(), BaHe()
    assert a is b
    assert c is d


def test_metaclass_singleton():
    a, b = GooHoo(), GooHoo()
    assert a is b
