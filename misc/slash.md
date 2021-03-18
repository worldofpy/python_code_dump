# Uses of `/` and `\` in python

---

## 1. division operator

```python
>>> 5 / 2
2.5
```

## 2. floor division operator

```python
>>> 5 // 2
2
```

## 3. positional only function arguments

```python
def bar(a, b, /, c, d):
    print(f'{a = }, {b = }, {c = }, {d = }')
```

```python
>>> bar(1, 2, 3, 4)
a = 1, b = 2, c = 3, d = 4
```

```python
>>> bar(1, 2, c=3, d=4)
a = 1, b = 2, c = 3, d = 4
```

```python
>>> bar(a=1, b=2, c=3, d=4)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: bar() got some positional-only arguments passed as keyword arguments: 'a, b'
```

---

## escape sequences

```bash
>>> print('this is a line \n and another line')
this is a line
 and another line
```

```bash
>>> print(r'this is a line \n and another line')  # r'' makes it a raw string
this is a line \n and another line
```
