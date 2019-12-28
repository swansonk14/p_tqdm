import unittest

from p_tqdm import p_map, p_imap, p_umap, p_uimap, t_map, t_imap


def add_1(a):
    return a + 1


def add_2(a, b):
    return a + b


def add_3(a, b, c):
    return a + b + c


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
        result = self.func(add_3, array_1, single, array_2)
        if self.generator:
            result = list(result)

        correct_array = [16, 18, 20]
        if self.ordered:
            self.assertEqual(correct_array, result)
        else:
            self.assertEqual(sorted(correct_array), sorted(result))

    def test_one_list_and_two_singles(self):
        array = [1, 2, 3]
        single_1 = 5
        single_2 = -2
        result = self.func(add_3, single_1, array, single_2)
        if self.generator:
            result = list(result)

        correct_array = [4, 5, 6]
        if self.ordered:
            self.assertEqual(correct_array, result)
        else:
            self.assertEqual(sorted(correct_array), sorted(result))

    def test_one_single(self):
        single = 5
        result = self.func(add_1, single)
        if self.generator:
            result = list(result)

        correct_array = [6]
        if self.ordered:
            self.assertEqual(correct_array, result)
        else:
            self.assertEqual(sorted(correct_array), sorted(result))

    def test_one_single_with_num_iter(self):
        single = 5
        num_iter = 3
        result = self.func(add_1, single, num_iter=num_iter)
        if self.generator:
            result = list(result)

        correct_array = [6] * num_iter
        if self.ordered:
            self.assertEqual(correct_array, result)
        else:
            self.assertEqual(sorted(correct_array), sorted(result))

    def test_two_singles(self):
        single_1 = 5
        single_2 = -2
        result = self.func(add_2, single_1, single_2)
        if self.generator:
            result = list(result)

        correct_array = [3]
        if self.ordered:
            self.assertEqual(correct_array, result)
        else:
            self.assertEqual(sorted(correct_array), sorted(result))

    def test_two_singles_with_num_iter(self):
        single_1 = 5
        single_2 = -2
        num_iter = 3
        result = self.func(add_2, single_1, single_2, num_iter=num_iter)
        if self.generator:
            result = list(result)

        correct_array = [3] * num_iter
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
