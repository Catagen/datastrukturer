import unittest
from exercises.tree import BinarySearchTree

class TreeTests(unittest.TestCase):

    def setUp(self):
        self.tree = BinarySearchTree(50)

    def text_insert(self):
        self.tree.insert(40)
        self.tree.insert(30)
        self.tree.insert(60)
        self.tree.insert(70)
        assertEqual([self.tree.left.left, self.tree.left, self.tree, self.right, self.right.right], self.tree.tranverse())

    def test_lookup(self):
        self.assertEqual(self.tree, self.tree.lookup(50))
        self.tree.insert(40)
        self.tree.insert(60)
        self.assertEqual(self.tree.left, self.tree.lookup(40))
        self.assertEqual(self.tree.right, self.tree.lookup(60))
        self.assertEqual(None, self.tree.lookup(10))
