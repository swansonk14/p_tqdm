# p_tqdm

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/p-tqdm)](https://badge.fury.io/py/p-tqdm)
[![PyPI version](https://badge.fury.io/py/p-tqdm.svg)](https://badge.fury.io/py/p-tqdm)
[![Build Status](https://travis-ci.org/swansonk14/p_tqdm.svg?branch=master)](https://travis-ci.org/swansonk14/p_tqdm)

`p_tqdm` makes parallel processing with progress bars easy.

`p_tqdm` is a wrapper around [pathos.multiprocessing](https://github.com/uqfoundation/pathos/blob/master/pathos/multiprocessing.py) and [tqdm](https://github.com/tqdm/tqdm). Unlike Python's default multiprocessing library, pathos provides a more flexible parallel map which can apply almost any type of function --- including lambda functions, nested functions, and class methods --- and can easily handle functions with multiple arguments. tqdm is applied on top of pathos's parallel map and displays a progress bar including an estimated time to completion.

## Installation

```pip install p_tqdm```

## Example

Let's say you want to add two lists element by element. Without any parallelism, this can be done easily with a Python `map`.

```python
l1 = ['1', '2', '3']
l2 = ['a', 'b', 'c']

def add(a, b):
    return a + b
    
added = map(add, l1, l2)
# added == ['1a', '2b', '3c']
```

But if the lists are much larger or the computation is more intense, parallelism becomes a necessity. However, the syntax is often cumbersome. `p_tqdm` makes it easy and adds a progress bar too.

```python
from p_tqdm import p_map

added = p_map(add, l1, l2)
# added == ['1a', '2b', '3c']
```

```
  0%|                                    | 0/3 [00:00<?, ?it/s]
 33%|████████████                        | 1/3 [00:01<00:02, 1.00s/it]
 66%|████████████████████████            | 2/3 [00:02<00:01, 1.00s/it]
100%|████████████████████████████████████| 3/3 [00:03<00:00, 1.00s/it]
```

## p_tqdm functions

### Parallel maps

* [p_map](#p_map) - parallel ordered map
* [p_imap](#p_imap) - iterator for parallel ordered map
* [p_umap](#p_umap) - parallel unordered map
* [p_uimap](#p_uimap) - iterator for parallel unordered map

### Sequential maps
* [t_map](#t_map) - sequential ordered map
* [t_imap](#t_imap) - iterator for sequential ordered map

### p_map

Performs an ordered map in parallel.

```python
from p_tqdm import p_map

def add(a, b):
    return a + b

added = p_map(add, ['1', '2', '3'], ['a', 'b', 'c'])
# added = ['1a', '2b', '3c']
```

### p_imap

Returns an iterator for an ordered map in parallel.

```python
from p_tqdm import p_imap

def add(a, b):
    return a + b

iterator = p_imap(add, ['1', '2', '3'], ['a', 'b', 'c'])

for result in iterator:
    print(result) # prints '1a', '2b', '3c'
```

### p_umap

Performs an unordered map in parallel.

```python
from p_tqdm import p_umap

def add(a, b):
    return a + b

added = p_umap(add, ['1', '2', '3'], ['a', 'b', 'c'])
# added is an array with '1a', '2b', '3c' in any order
```

### p_uimap

Returns an iterator for an unordered map in parallel.

```python
from p_tqdm import p_uimap

def add(a, b):
    return a + b

iterator = p_uimap(add, ['1', '2', '3'], ['a', 'b', 'c'])

for result in iterator:
    print(result) # prints '1a', '2b', '3c' in any order
```

### t_map

Performs an ordered map sequentially.

```python
from p_tqdm import t_map

def add(a, b):
    return a + b

added = t_map(add, ['1', '2', '3'], ['a', 'b', 'c'])
# added == ['1a', '2b', '3c']
```

### t_imap

Returns an iterator for an ordered map to be performed sequentially.

```python
from p_tqdm import p_imap

def add(a, b):
    return a + b

iterator = t_imap(add, ['1', '2', '3'], ['a', 'b', 'c'])

for result in iterator:
    print(result) # prints '1a', '2b', '3c'
```

## Shared properties

### Arguments

All `p_tqdm` functions accept any number of iterables as input, as long as the number of iterables matches the number of arguments of the function.

To repeat a non-iterable argument along with the iterables, use Python's [partial](https://docs.python.org/3/library/functools.html#functools.partial) from the [functools](https://docs.python.org/3/library/functools.html) library. See the example below.

```python
from functools import partial

l1 = ['1', '2', '3']
l2 = ['a', 'b', 'c']

def add(a, b, c=''):
    return a + b + c

added = p_map(partial(add, c='!'), l1, l2)
# added == ['1a!', '2b!', '3c!']
```

### CPUs

All the parallel `p_tqdm` functions can be passed the keyword `num_cpus` to indicate how many CPUs to use. The default is all CPUs. `num_cpus` can either be an integer to indicate the exact number of CPUs to use or a float to indicate the proportion of CPUs to use.

Note that the parallel Pool objects used by `p_tqdm` are automatically closed when the map finishes processing.
