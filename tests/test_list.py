import unittest
from exercises.list import Node, UnorderedList
from exercises.exceptions import EmptyList

class NodeTests(unittest.TestCase):
    def test_node(self):
        n = Node('test', None)
        self.assertEqual(n.data, 'test')
        self.assertEqual(n.next, None)


class UnorderedListTests(unittest.TestCase):

    def setUp(self):
        self.ul = UnorderedList()

    def test_is_empty(self):
        self.assertTrue(self.ul.is_empty())
        self.ul.add('test')
        self.assertFalse(self.ul.is_empty())

    def test_add(self):
        self.ul.add('a')
        self.ul.add('b')
        self.assertEqual(self.ul.index('b'), 0)
        self.assertEqual(self.ul.size(), 2)

    def test_size(self):
        self.assertEqual(self.ul.size(), 0)
        self.ul.add('a')
        self.assertEqual(self.ul.size(), 1)
        self.ul.add('b')
        self.assertEqual(self.ul.size(), 2)

    def test_search(self):
        self.ul.add(1)
        self.assertTrue(self.ul.search(1))
        self.assertFalse(self.ul.search('1'))

    def test_remove(self):
        self.ul.remove('test')
        self.ul.add('a')
        self.ul.add('b')
        self.ul.add('c')
        self.ul.remove('test')
        self.ul.remove('b')
        self.assertEqual(self.ul.size(), 2)
        self.ul.add('b')
        self.ul.remove('a')
        self.assertEqual(self.ul.size(), 2)
        self.ul.remove('test')
        self.ul.remove('b')
        self.ul.remove('c')
        self.ul.remove('test')


    def test_append(self):
        self.ul.append('a')
        self.ul.add('b')
        self.ul.add('c')
        self.ul.append('d')
        self.assertEqual(self.ul.index('d'), 3)
        self.ul.append('e')
        self.assertEqual(self.ul.index('e'), 4)

    def test_insert(self):
        self.ul.insert(5, 'test')
        self.ul.insert(0, 'd')
        self.ul.add('b')
        self.ul.add('a')
        self.ul.insert(2, 'c')
        order = [self.ul.pop(), self.ul.pop(), self.ul.pop()]
        self.assertEqual(order, ['a', 'b', 'c'])

    def test_index(self):
        self.assertRaises(EmptyList, self.ul.index, 'test')
        self.ul.add('a')
        self.ul.add('b')
        self.ul.add('c')
        self.assertEqual(self.ul.index('c'), 0)
        self.assertEqual(self.ul.index('b'), 1)
        self.assertEqual(self.ul.index('a'), 2)

    def test_pop(self):
        self.assertRaises(EmptyList, self.ul.pop)
        self.assertRaises(EmptyList, self.ul.pop, 2)
        self.ul.add('test')
        self.assertRaises(IndexError, self.ul.pop, 2)
        self.ul.remove('test')
        self.ul.add('a')
        self.ul.add('b')
        self.ul.add('c')
        self.ul.add('d')
        self.assertEqual(self.ul.pop(), 'd')
        self.assertEqual(self.ul.pop(1), 'b')
