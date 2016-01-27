import unittest
from exercises.simple import Stack, Queue
from exercises.exceptions import EmptyStack, EmptyQueue

class StackTests(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()

    def test_pop(self):
        self.assertRaises(EmptyStack, self.stack.pop)
        self.stack.push('test')
        self.stack.push('a')
        self.assertEqual(self.stack.pop(), 'a')
        self.assertEqual(self.stack.size(), 1)

    def test_peek(self):
        self.assertRaises(EmptyStack, self.stack.peek)
        self.stack.push('test')
        self.assertEqual(self.stack.peek(), 'test')
        self.assertEqual(self.stack.size(), 1)

    def test_is_empty(self):
        self.assertTrue(self.stack.is_empty())

    def test_size(self):
        self.stack.push('test')
        self.assertEqual(self.stack.size(), 1)


class QueueTests(unittest.TestCase):

    def setUp(self):
        self.que = Queue()

    def test_dequeue(self):
        self.assertRaises(EmptyQueue, self.que.dequeue)
        self.que.enqueue('a')
        self.que.enqueue('b')
        self.assertEqual(self.que.dequeue(), 'b')

    def test_is_empty(self):
        self.assertTrue(self.que.is_empty())
        self.que.enqueue('test')
        self.assertFalse(self.que.is_empty())

    def test_size(self):
        self.assertEqual(self.que.size(), 0)
        self.que.enqueue('test')
        self.assertEqual(self.que.size(), 1)
