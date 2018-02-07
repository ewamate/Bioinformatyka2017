import unittest
from dict_ops import merge_dicts
from dict_ops import dict_list_to_list

class TestDictOps(unittest.TestCase):

    def test_merge_dicts(self):
        dict1 = {'a': {'Full name': 1, 'Short name': 2, 'c': 3}, 'b': {'Full name': 1, 'Short name': 2, 'c': 3}, 'c': {'Full name': 1, 'Short name': 2, 'c': 3}}
        dict2 = {'a': {'a': 1, 'b': 2, 'c': 3}, 'b': {'a': 1, 'b': 2, 'c': 3}, 'c': {'a': 1, 'b': 2, 'c': 3}}
        merged = merge_dicts(dict1, dict2)
        self.assertEqual(len(merged.keys()), 3)
        self.assertEqual(len(merged['a'].keys()), 5)
        self.assertEqual(merged['a']['modomics.genesilico'], 'true')


        dict1 = {'a': {'Full name': 1, 'Short name': 2, 'c': 3}, 'b': {'Full name': 1, 'Short name': 2, 'c': 3}, 'c': {'Full name': 1, 'Short name': 2, 'c': 3}}
        dict2 = {'d': {'a': 1, 'b': 2, 'c': 3}, 'e': {'a': 1, 'b': 2, 'c': 3}, 'c': {'a': 1, 'b': 2, 'c': 3}}
        merged = merge_dicts(dict1, dict2)
        self.assertEqual(len(merged.keys()), 5)
        self.assertEqual(len(merged['a'].keys()), 2)
        self.assertEqual(merged['a']['modomics.genesilico'], 'true')


        dict1 = {'a': {'Full name': 1, 'Short name': 2, 'c': 3}, 'b': {'Full name': 1, 'Short name': 2, 'c': 3}, 'c': {'Full name': 1, 'Short name': 2, 'c': 3}}
        dict2 = {'c': {'a': 1, 'b': 2, 'c': 3}}
        merged = merge_dicts(dict1, dict2)
        self.assertEqual(len(merged.keys()), 3)
        self.assertEqual(len(merged['a'].keys()), 2)
        self.assertEqual(merged['a']['modomics.genesilico'], 'true')

    def test_dict_list_to_list(self):
        dct = {'a': {'a': 1, 'b': 2, 'c': 3}, 'b': {'a': 1, 'b': 2, 'c': 3}, 'c': {'a': 1, 'b': 2, 'c': 3}}
        lst = ['a','b','c']
        list = dict_list_to_list(dct, lst)
        self.assertEqual(len(list), 3)

        dct = {'a': 1, 'b': 2, 'c': 3}
        lst = ['a','b','c']
        list = dict_list_to_list(dct, lst)
        self.assertEqual(len(list), 3)

        dct = {'a': 1, 'b': 2, 'c': 3}
        lst = ['a']
        list = dict_list_to_list(dct, lst)
        self.assertEqual(len(list), 1)
        self.assertEqual(list[0], 1)


if __name__ == '__main__':
    unittest.main()
