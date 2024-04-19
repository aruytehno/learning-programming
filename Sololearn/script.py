import pytest

def test_example():
    list = ["one", "two"]
    dict = {1: 1, 2: 1, 3: 2, 4: 3}
    words = ("spam", "eggs", "sausages")

    print(type(list))
    print(type(dict))
    print(type(words))

def test_example2():
    tuple = (1, (1, 2, 3))
    print(tuple[1])