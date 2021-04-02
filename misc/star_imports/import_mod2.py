from module2 import *

foo()

try:
    _bar()
except Exception as err:
    print(err)

try:
    __foobar()
except Exception as err:
    print(err)
