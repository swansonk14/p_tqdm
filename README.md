# p_tqdm - parallel processing with progress bars

`p_tqdm` provides implementations of parallel and sequential map functions using [tqdm](https://github.com/tqdm/tqdm) progress bars.

Since `p_tqdm` uses [pathos.multiprocessing](https://github.com/uqfoundation/pathos/blob/master/pathos/multiprocessing.py) instead of the regular python [multiprocessing](https://docs.python.org/3/library/multiprocessing.html) module, its parallel maps can apply almost any type of function, including lambda functions, nested functions, and class methods.

## Installation

```pip install p_tqdm```

## p_map - parallel ordered map

```python
from p_tqdm import p_map

def func(a, b):
    return a + b

results = p_map(func, ['1', '2', '3'], ['a', 'b', 'c'])
```

```
  0%|                                    | 0/3 [00:00<?, ?it/s]
 33%|████████████                        | 1/3 [00:01<00:02, 1.00s/it]
 66%|████████████████████████            | 2/3 [00:02<00:01, 1.00s/it]
100%|████████████████████████████████████| 3/3 [00:03<00:00, 1.00s/it]
```

```python
results == ['1a', '2b', '3c'] # True
```

## p_imap - iterator for parallel ordered map

```python
from p_tqdm import p_imap

def func(a, b):
    return a + b

iterator = p_imap(func, ['1', '2', '3'], ['a', 'b', 'c'])

for result in iterator:
    print(result) # prints '1a', '2b', '3c'
```

## p_umap - parallel unordered map

```python
from p_tqdm import p_umap

def func(a, b):
    return a + b

results = p_umap(func, ['1', '2', '3'], ['a', 'b', 'c'])

results == ['2b', '1a', '3c'] # an array with '1a', '2b', and '3c' in any order
```

## p_uimap - iterator for parallel unordered map

```python
from p_tqdm import p_uimap

def func(a, b):
    return a + b

iterator = p_uimap(func, ['1', '2', '3'], ['a', 'b', 'c'])

for result in iterator:
    print(result) # prints '1a', '2b', '3c' in any order
```

## t_map - sequential map

```python
from p_tqdm import t_map

def func(a, b):
    return a + b

results = t_map(func, ['1', '2', '3'], ['a', 'b', 'c'])

results == ['1a', '2b', '3c'] # True
```

## t_imap - iterator for sequential map

```python
from p_tqdm import p_imap

def func(a, b):
    return a + b

iterator = t_imap(func, ['1', '2', '3'], ['a', 'b', 'c'])

for result in iterator:
    print(result) # prints '1a', '2b', '3c'
```
