import unittest
from functools import partial

from p_tqdm import p_map, p_imap, p_umap, p_uimap, t_map, t_imap


def add_1(a):
    return a + 1


def add_2(a, b):
    return a + b


def add_3(a, b, c=0):
    return a + 2 * b + 3 * c


class Test_p_map(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(Test_p_map, self).__init__(*args, **kwargs)
        self.func = p_map
        self.generator = False
        self.ordered = True

    def test_one_list(self):
        array = [1, 2, 3]
        result = self.func(add_1, array)
        if self.generator:
            result = list(result)

        correct_array = [2, 3, 4]
        if self.ordered:
            self.assertEqual(correct_array, result)
        else:
            self.assertEqual(sorted(correct_array), sorted(result))

    def test_two_lists(self):
        array_1 = [1, 2, 3]
        array_2 = [10, 11, 12]
        result = self.func(add_2, array_1, array_2)
        if self.generator:
            result = list(result)

        correct_array = [11, 13, 15]
        if self.ordered:
            self.assertEqual(correct_array, result)
        else:
            self.assertEqual(sorted(correct_array), sorted(result))

    def test_two_lists_and_one_single(self):
        array_1 = [1, 2, 3]
        array_2 = [10, 11, 12]
        single = 5
        result = self.func(partial(add_3, single), array_1, array_2)
        if self.generator:
            result = list(result)

        correct_array = [37, 42, 47]
        if self.ordered:
            self.assertEqual(correct_array, result)
        else:
            self.assertEqual(sorted(correct_array), sorted(result))

    def test_one_list_and_two_singles(self):
        array = [1, 2, 3]
        single_1 = 5
        single_2 = -2
        result = self.func(partial(add_3, single_1, c=single_2), array)
        if self.generator:
            result = list(result)

        correct_array = [1, 3, 5]
        if self.ordered:
            self.assertEqual(correct_array, result)
        else:
            self.assertEqual(sorted(correct_array), sorted(result))

    def test_list_and_generator_and_single_equal_length(self):
        array = [1, 2, 3]
        generator = range(3)
        single = -3
        result = self.func(partial(add_3, c=single), array, generator)
        if self.generator:
            result = list(result)

        correct_array = [-8, -5, -2]
        if self.ordered:
            self.assertEqual(correct_array, result)
        else:
            self.assertEqual(sorted(correct_array), sorted(result))

    def test_list_and_generator_and_single_unequal_length(self):
        array = [1, 2, 3, 4, 5, 6]
        generator = range(3)
        single = -3
        result = self.func(partial(add_3, c=single), array, generator)
        if self.generator:
            result = list(result)

        correct_array = [-8, -5, -2]
        if self.ordered:
            self.assertEqual(correct_array, result)
        else:
            self.assertEqual(sorted(correct_array), sorted(result))


class Test_p_imap(Test_p_map):
    def __init__(self, *args, **kwargs):
        super(Test_p_map, self).__init__(*args, **kwargs)
        self.func = p_imap
        self.generator = True
        self.ordered = True


class Test_p_umap(Test_p_map):
    def __init__(self, *args, **kwargs):
        super(Test_p_map, self).__init__(*args, **kwargs)
        self.func = p_umap
        self.generator = False
        self.ordered = False


class Test_p_uimap(Test_p_map):
    def __init__(self, *args, **kwargs):
        super(Test_p_map, self).__init__(*args, **kwargs)
        self.func = p_uimap
        self.generator = True
        self.ordered = False


class Test_t_map(Test_p_map):
    def __init__(self, *args, **kwargs):
        super(Test_p_map, self).__init__(*args, **kwargs)
        self.func = t_map
        self.generator = False
        self.ordered = True


class Test_t_imap(Test_p_map):
    def __init__(self, *args, **kwargs):
        super(Test_p_map, self).__init__(*args, **kwargs)
        self.func = t_imap
        self.generator = True
        self.ordered = True


if __name__ == '__main__':
    unittest.main()
