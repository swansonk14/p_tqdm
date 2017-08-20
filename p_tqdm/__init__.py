"""Map functions with tqdm progress bars for parallel and sequential processing.

p_imap: Returns an iterator for a parallel ordered map.
p_map: Performs a parallel ordered map.
p_uimap: Returns an iterator for a parallel unordered map.
p_umap: Performs a parallel unordered map.
t_imap: Returns an iterator for a sequential map.
t_map: Performs a sequential map.
"""

from pathos.helpers import cpu_count
from pathos.multiprocessing import ProcessingPool as Pool
from tqdm import tqdm

def p_imap(function, *arrays, num_cpus=None):
    """Returns an iterator for a parallel ordered map with a progress bar.

    Args:
        function: The function to apply to each element
            of the given arrays.
        arrays: One or more arrays of the same length
            containing the data to be mapped.
        num_cpus: The number of cpus to use in parallel.
            If an int, uses that many cpus.
            If a float, uses that proportion of cpus.
            If None, uses all available cpus.
    Returns:
        An iterator which will apply the function
        to each element of the given arrays in
        parallel in order with a progress bar.
    """

    if num_cpus is None:
        num_cpus = cpu_count()
    elif type(num_cpus) == float:
        num_cpus = int(round(num_cpus * cpu_count()))

    iterator = tqdm(Pool(num_cpus).imap(function, *arrays),
                         total=len(arrays[0]))

    return iterator

def p_map(function, *arrays, num_cpus=None):
    """Performs a parallel ordered map with a progress bar.

    Example:
    p_map(f, [1, 2, 3], ['a', 'b', 'c']) --> [f(1, 'a'), f(2, 'b'), f(3, 'c')]

    Args:
        function: The function to apply to each element
            of the given arrays.
        arrays: One or more arrays of the same length
            containing the data to be mapped.
        num_cpus: The number of cpus to use in parallel.
            If an int, uses that many cpus.
            If a float, uses that proportion of cpus.
            If None, uses all available cpus.
    Returns:
        An array with the result of applying the function
        to each element of the given arrays in order.
    """

    new_data = list(p_imap(function, *arrays, num_cpus=num_cpus))

    return new_data

def p_uimap(function, *arrays, num_cpus=None):
    """Returns an iterator for a parallel unordered map with a progress bar.

    Args:
        function: The function to apply to each element
            of the given arrays.
        arrays: One or more arrays of the same length
            containing the data to be mapped.
        num_cpus: The number of cpus to use in parallel.
            If an int, uses that many cpus.
            If a float, uses that proportion of cpus.
            If None, uses all available cpus.
    Returns:
        An iterator which will apply the function
        to each element of the given arrays in
        parallel with a progress bar. The results
        may be in any order.
    """

    if num_cpus is None:
        num_cpus = cpu_count()
    elif type(num_cpus) == float:
        num_cpus = int(round(num_cpus * cpu_count()))

    iterator = tqdm(Pool(num_cpus).uimap(function, *arrays),
                         total=len(arrays[0]))

    return iterator

def p_umap(function, *arrays, num_cpus=None):
    """Performs a parallel unordered map with a progress bar.

    Example:
    p_umap(f, [1, 2, 3], ['a', 'b', 'c']) --> [f(2, 'b'), f(1, 'a'), f(3, 'c')]
    Note: The resulting array may be in any order.

    Args:
        function: The function to apply to each element
            of the given arrays.
        arrays: One or more arrays of the same length
            containing the data to be mapped.
        num_cpus: The number of cpus to use in parallel.
            If an int, uses that many cpus.
            If a float, uses that proportion of cpus.
            If None, uses all available cpus.
    Returns:
        An array with the result of applying the function
        to each element of the given arrays. This array
        may be in any order.
    """

    new_data = list(p_uimap(function, *arrays, num_cpus=num_cpus))

    return new_data

def t_imap(function, *arrays):
    """Returns an iterator for a sequential map with a progress bar.

    Args:
        function: The function to apply to each element
            of the given arrays.
        arrays: One or more arrays of the same length
            containing the data to be mapped.
    Returns:
        An iterator which will apply the function
        to each element of the given arrays sequentially
        in order with a progress bar.
    """

    iterator = tqdm(map(function, *arrays),
                         total=len(arrays[0]))

    return iterator

def t_map(function, *arrays):
    """Performs a sequential map with a progress bar.

    Example:
    t_map(f, [1, 2, 3], ['a', 'b', 'c']) --> [f(1, 'a'), f(2, 'b'), f(3, 'c')]

    Args:
        function: The function to apply to each element
            of the given arrays.
        arrays: One or more arrays of the same length
            containing the data to be mapped.
    Returns:
        An array with the result of applying the function
        to each element of the given arrays in order.
    """

    new_data = list(t_imap(function, *arrays))

    return new_data
