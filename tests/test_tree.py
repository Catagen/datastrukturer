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
        self.assertEqual(self.tree, self.tree.lookup(50)[0])
        self.tree.insert(40)
        self.tree.insert(60)
        self.assertEqual(self.tree.left, self.tree.lookup(40)[0])
        self.assertEqual(self.tree.right, self.tree.lookup(60)[0])
        self.assertEqual(None, self.tree.lookup(10)[0])

    def test_traverse(self):
        self.tree.insert(40)
        self.tree.insert(60)
        self.tree.insert(45)
        self.tree.insert(55)
        self.tree.insert(65)

        result = []
        for node in self.tree.traverse():
            result.append(node.key)

        self.assertEqual([40,45,50,55,60,65], result)

    def test_delete(self):
        self.tree.insert(25)
        self.tree.insert(30)
        self.tree.insert(20)
        self.tree.insert(27)
        self.tree.insert(23)
        self.tree.insert(24)
        self.tree.insert(19)

        self.tree.insert(75)
        self.tree.insert(70)
        self.tree.insert(80)
        self.tree.insert(72)
        self.tree.insert(77)


        self.tree2 = BinarySearchTree(50)
        self.tree2.insert(27)
        self.tree2.insert(30)
        self.tree2.insert(20)
        self.tree2.insert(23)
        self.tree2.insert(24)
        self.tree2.insert(19)

        self.tree2.insert(75)
        self.tree2.insert(80)
        self.tree2.insert(72)

        self.tree.delete(25)
        self.tree.delete(77)
        self.tree.delete(70)
        self.assertTrue(self.tree == self.tree2)


    def test_str(self):
        self.tree.insert(25)
        self.tree.insert(30)
        self.tree.insert(20)
        self.tree.insert(27)
        self.tree.insert(23)
        self.tree.insert(24)
        self.tree.insert(19)

        self.tree.insert(75)
        self.tree.insert(70)
        self.tree.insert(80)
        self.tree.insert(72)
        self.tree.insert(77)

        self.assertEqual(str(self.tree), str([19,20,23,24,25,27,30,50,70,72,75,77,80]))
