"""Map functions with tqdm progress bars for parallel and sequential processing.

p_map: Performs a parallel ordered map.
p_imap: Returns an iterator for a parallel ordered map.
p_umap: Performs a parallel unordered map.
p_uimap: Returns an iterator for a parallel unordered map.
t_map: Performs a sequential map.
t_imap: Returns an iterator for a sequential map.
"""

from pathos.helpers import cpu_count
from pathos.multiprocessing import ProcessingPool as Pool
from tqdm import tqdm

def _parallel(ordered, function, *arrays, **kwargs):
    """Returns an iterator for a parallel map with a progress bar.

    Arguments:
        ordered(bool): True for an ordered map, false for an unordered map.
        function(function): The function to apply to each element
            of the given arrays.
        arrays(tuple): One or more arrays of the same length
            containing the data to be mapped. If a non-list
            variable is passed, it will be repeated a number
            of times equal to the lengths of the list(s). If only
            non-list variables are passed, the function will be
            performed num_iter times.
        num_cpus(int): The number of cpus to use in parallel.
            If an int, uses that many cpus.
            If a float, uses that proportion of cpus.
            If None, uses all available cpus.
        num_iter(int): If only non-list variables are passed, the
            function will be performed num_iter times on
            these variables. Default: 1.
        **kwargs: extra arguments will be passes to tqdm

    Returns:
        An iterator which will apply the function
        to each element of the given arrays in
        parallel in order with a progress bar.
    """

    # Convert tuple to list
    arrays = list(arrays)

    # Extract kwargs
    num_cpus = kwargs.get('num_cpus', None)
    num_iter = kwargs.get('num_iter', 1)
    kwargs['num_cpus']=None
    kwargs['num_iter']=None

    # Determine num_cpus
    if num_cpus is None:
        num_cpus = cpu_count()
    elif type(num_cpus) == float:
        num_cpus = int(round(num_cpus * cpu_count()))

    # Determine num_iter when at least one list is present
    if any([type(array) == list for array in arrays]):
        num_iter = max([len(array) for array in arrays if type(array) == list])

    # Convert single variables to lists
    # and confirm lists are same length
    for i, array in enumerate(arrays):
        if type(array) != list:
            arrays[i] = [array for _ in range(num_iter)]
        else:
            assert len(array) == num_iter

    # Create parallel iterator
    map_type = 'imap' if ordered else 'uimap'
    iterator = tqdm(getattr(Pool(num_cpus), map_type)(function, *arrays),
                    total=num_iter, **kwargs)

    return iterator

def p_map(function, *arrays, **kwargs):
    """Performs a parallel ordered map with a progress bar."""

    ordered = True
    iterator = _parallel(ordered, function, *arrays, **kwargs)
    result = list(iterator)

    return result

def p_imap(function, *arrays, **kwargs):
    """Returns an iterator for a parallel ordered map with a progress bar."""

    ordered = True
    iterator = _parallel(ordered, function, *arrays, **kwargs)

    return iterator

def p_umap(function, *arrays, **kwargs):
    """Performs a parallel unordered map with a progress bar."""

    ordered = False
    iterator = _parallel(ordered, function, *arrays, **kwargs)
    result = list(iterator)

    return result

def p_uimap(function, *arrays, **kwargs):
    """Returns an iterator for a parallel unordered map with a progress bar."""

    ordered = False
    iterator = _parallel(ordered, function, *arrays, **kwargs)

    return iterator

def _sequential(function, *arrays, **kwargs):
    """Returns an iterator for a sequential map with a progress bar.

    Arguments:
        function(function): The function to apply to each element
            of the given arrays.
        arrays(tuple): One or more arrays of the same length
            containing the data to be mapped. If a non-list
            variable is passed, it will be repeated a number
            of times equal to the lengths of the list(s). If only
            non-list variables are passed, the function will be
            performed num_iter times.
        num_iter(int): If only non-list variables are passed, the
            function will be performed num_iter times on
            these variables. Default: 1.

    Returns:
        An iterator which will apply the function
        to each element of the given arrays sequentially
        in order with a progress bar.
    """

    # Convert tuple to list
    arrays = list(arrays)

    # Extract kwargs
    num_iter = kwargs.get('num_iter', 1)

    # Determine num_iter when at least one list is present
    if any([type(array) == list for array in arrays]):
        num_iter = max([len(array) for array in arrays if type(array) == list])

    # Convert single variables to lists
    # and confirm lists are same length
    for i, array in enumerate(arrays):
        if type(array) != list:
            arrays[i] = [array for _ in range(num_iter)]
        else:
            assert len(array) == num_iter

    # Create parallel iterator
    iterator = tqdm(map(function, *arrays),
                    total=num_iter)

    return iterator

def t_map(function, *arrays, **kwargs):
    """Performs a sequential map with a progress bar."""

    iterator = _sequential(function, *arrays, **kwargs)
    result = list(iterator)

    return result

def t_imap(function, *arrays, **kwargs):
    """Returns an iterator for a sequential map with a progress bar."""

    iterator = _sequential(function, *arrays, **kwargs)

    return iterator
