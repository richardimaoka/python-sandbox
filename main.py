import typing
from collections import namedtuple


class Item(typing.NamedTuple):
    user: str
    fish: str
    amount: int
    wasabi: bool


Item = namedtuple("Item", ["user", "fish", "amount", "wasabi"])


def add(a, b):
    return a + b


def f():
    return add(None, 0)


def add(a, b):
    c = a if a else 0
    return a + b
