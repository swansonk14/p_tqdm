import types
import unittest

import p_tqdm
import tqdm

def add_1(a):
    return a + 1

def add_2(a, b):
    return a + b

def add_3(a, b, c):
    return a + b + c

def _test_one_list(self):
    array = [1, 2, 3]
    result = self.func(add_1, array)
    if self.generator:
        result = list(result)

    correct_array = [2, 3, 4]
    if self.ordered:
        self.assertListEqual(correct_array, result)
    else:
        self.assertListEqual(sorted(correct_array), sorted(result))

def _test_two_lists(self):
    array_1 = [1, 2, 3]
    array_2 = [10, 11, 12]
    result = self.func(add_2, array_1, array_2)
    if self.generator:
        result = list(result)

    correct_array = [11, 13, 15]
    if self.ordered:
        self.assertListEqual(correct_array, result)
    else:
        self.assertListEqual(sorted(correct_array), sorted(result))

def _test_two_lists_and_one_single(self):
    array_1 = [1, 2, 3]
    array_2 = [10, 11, 12]
    single = 5
    result = self.func(add_3, array_1, single, array_2)
    if self.generator:
        result = list(result)

    correct_array = [16, 18, 20]
    if self.ordered:
        self.assertListEqual(correct_array, result)
    else:
        self.assertListEqual(sorted(correct_array), sorted(result))

def _test_one_list_and_two_singles(self):
    array = [1, 2, 3]
    single_1 = 5
    single_2 = -2
    result = self.func(add_3, single_1, array, single_2)
    if self.generator:
        result = list(result)

    correct_array = [4, 5, 6]
    if self.ordered:
        self.assertListEqual(correct_array, result)
    else:
        self.assertListEqual(sorted(correct_array), sorted(result))

def _test_one_single(self):
    single = 5
    result = self.func(add_1, single)
    if self.generator:
        result = list(result)

    correct_array = [6]
    if self.ordered:
        self.assertListEqual(correct_array, result)
    else:
        self.assertListEqual(sorted(correct_array), sorted(result))

def _test_one_single_with_num_iter(self):
    single = 5
    num_iter = 3
    result = self.func(add_1, single, num_iter=num_iter)
    if self.generator:
        result = list(result)

    correct_array = [6]*num_iter
    if self.ordered:
        self.assertListEqual(correct_array, result)
    else:
        self.assertListEqual(sorted(correct_array), sorted(result))

def _test_two_singles(self):
    single_1 = 5
    single_2 = -2
    result = self.func(add_2, single_1, single_2)
    if self.generator:
        result = list(result)

    correct_array = [3]
    if self.ordered:
        self.assertListEqual(correct_array, result)
    else:
        self.assertListEqual(sorted(correct_array), sorted(result))

def _test_two_singles_with_num_iter(self):
    single_1 = 5
    single_2 = -2
    num_iter = 3
    result = self.func(add_2, single_1, single_2, num_iter=num_iter)
    if self.generator:
        result = list(result)

    correct_array = [3]*num_iter
    if self.ordered:
        self.assertListEqual(correct_array, result)
    else:
        self.assertListEqual(sorted(correct_array), sorted(result))

class Testp_imap(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(Testp_imap, self).__init__(*args, **kwargs)
        self.func = p_tqdm.p_imap
        self.generator = True
        self.ordered = True

    def test_one_list(self):
        _test_one_list(self)

    def test_two_lists(self):
        _test_two_lists(self)

    def test_two_lists_and_one_single(self):
        _test_two_lists_and_one_single(self)

    def test_one_list_and_two_singles(self):
        _test_one_list_and_two_singles(self)

    def test_one_single(self):
        _test_one_single(self)

    def test_one_single_with_num_iter(self):
        _test_one_single_with_num_iter(self)

    def test_two_singles(self):
        _test_two_singles(self)

    def test_two_singles_with_num_iter(self):
        _test_two_singles_with_num_iter(self)

class Testp_map(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(Testp_map, self).__init__(*args, **kwargs)
        self.func = p_tqdm.p_map
        self.generator = False
        self.ordered = True

    def test_one_list(self):
        _test_one_list(self)

    def test_two_lists(self):
        _test_two_lists(self)

    def test_two_lists_and_one_single(self):
        _test_two_lists_and_one_single(self)

    def test_one_list_and_two_singles(self):
        _test_one_list_and_two_singles(self)

    def test_one_single(self):
        _test_one_single(self)

    def test_one_single_with_num_iter(self):
        _test_one_single_with_num_iter(self)

    def test_two_singles(self):
        _test_two_singles(self)

    def test_two_singles_with_num_iter(self):
        _test_two_singles_with_num_iter(self)

class Testp_uimap(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(Testp_uimap, self).__init__(*args, **kwargs)
        self.func = p_tqdm.p_uimap
        self.generator = True
        self.ordered = False

    def test_one_list(self):
        _test_one_list(self)

    def test_two_lists(self):
        _test_two_lists(self)

    def test_two_lists_and_one_single(self):
        _test_two_lists_and_one_single(self)

    def test_one_list_and_two_singles(self):
        _test_one_list_and_two_singles(self)

    def test_one_single(self):
        _test_one_single(self)

    def test_one_single_with_num_iter(self):
        _test_one_single_with_num_iter(self)

    def test_two_singles(self):
        _test_two_singles(self)

    def test_two_singles_with_num_iter(self):
        _test_two_singles_with_num_iter(self)

class Testp_umap(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(Testp_umap, self).__init__(*args, **kwargs)
        self.func = p_tqdm.p_umap
        self.generator = False
        self.ordered = False

    def test_one_list(self):
        _test_one_list(self)

    def test_two_lists(self):
        _test_two_lists(self)

    def test_two_lists_and_one_single(self):
        _test_two_lists_and_one_single(self)

    def test_one_list_and_two_singles(self):
        _test_one_list_and_two_singles(self)

    def test_one_single(self):
        _test_one_single(self)

    def test_one_single_with_num_iter(self):
        _test_one_single_with_num_iter(self)

    def test_two_singles(self):
        _test_two_singles(self)

    def test_two_singles_with_num_iter(self):
        _test_two_singles_with_num_iter(self)

class Testt_imap(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(Testt_imap, self).__init__(*args, **kwargs)
        self.func = p_tqdm.t_imap
        self.generator = True
        self.ordered = True

    def test_one_list(self):
        _test_one_list(self)

    def test_two_lists(self):
        _test_two_lists(self)

    def test_two_lists_and_one_single(self):
        _test_two_lists_and_one_single(self)

    def test_one_list_and_two_singles(self):
        _test_one_list_and_two_singles(self)

    def test_one_single(self):
        _test_one_single(self)

    def test_one_single_with_num_iter(self):
        _test_one_single_with_num_iter(self)

    def test_two_singles(self):
        _test_two_singles(self)

    def test_two_singles_with_num_iter(self):
        _test_two_singles_with_num_iter(self)

class Testt_map(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(Testt_map, self).__init__(*args, **kwargs)
        self.func = p_tqdm.t_map
        self.generator = False
        self.ordered = True

    def test_one_list(self):
        _test_one_list(self)

    def test_two_lists(self):
        _test_two_lists(self)

    def test_two_lists_and_one_single(self):
        _test_two_lists_and_one_single(self)

    def test_one_list_and_two_singles(self):
        _test_one_list_and_two_singles(self)

    def test_one_single(self):
        _test_one_single(self)

    def test_one_single_with_num_iter(self):
        _test_one_single_with_num_iter(self)

    def test_two_singles(self):
        _test_two_singles(self)

    def test_two_singles_with_num_iter(self):
        _test_two_singles_with_num_iter(self)

if __name__ == '__main__':
    unittest.main()
