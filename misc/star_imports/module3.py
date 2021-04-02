"""module3"""


def foo():
    print('CALLED: foo')


def foobar():
    print('CALLED: foobar')


def _bar():
    print('CALLED: _bar')


__all__ = [
    'foo',
    '_bar',
]
