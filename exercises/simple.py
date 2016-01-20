"""Övningar på de enklare ADTerna."""

from .exceptions import EmptyStack, EmptyQueue


class Stack():
    """Implementation av ADTn stack.
    """

    def __init__(self):
        """Initierar en tom stack.
        """
        self.items = []

    def push(self, item):
        """Lägg till `item` överst på stacken.
        """
        self.items.insert(0, item)

    def pop(self):
        """Plockar bort och returnerar översta värdet på stacken.
        """
        try:
            return self.items.pop(0)
        except IndexError:
            raise EmptyStack

    def peek(self):
        """Returnerar översta värdet på stacken.
        """
        try:
            return self.items[len(self.items) - 1]
        except IndexError:
            raise EmptyStack

    def is_empty(self):
        """Returnerar `True` om stacken är tom, annars `False`.
        """
        return self.items == []

    def size(self):
        """Returnerar antalet värden på stacken.
        """
        return len(self.items)


class Queue():
    """Implementation av ADTn kö (queue).
    """

    def __init__(self):
        """Initierar en tom kö.
        """
        self.data = []

    def enqueue(self, item):
        """Lägger till `ìtem` i slutuet på kön.
        """
        self.data.append(item)

    def dequeue(self):
        """Plockar bort det första värdet i kön och returnerar det.
        """
        try:
            return self.items.pop()
        except IndexError:
            raise EmptyStack

    def is_empty(self):
        """Returnerar `True` om kön är tom, annars `False`.
        """
        return self.items == []

    def size(self):
        """Returnerar antalet värden i kön.
        """
        return len(self.items)

if __name__ == '__main__':
    s = Stack()
    print(s.pop())
