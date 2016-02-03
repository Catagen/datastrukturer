"""Övningar på ADTn unordered list."""

from .exceptions import EmptyList


class Node():
    """Implementation av nod för `UnorderedList`."""

    def __init__(self, data, next):

        """Initiera noden med attributen `self.data` och `self.next`.
        """
        self.data = data
        self.next = next


class UnorderedList():
    """Implementation av ADTn oordnad lista (unordered list).

    Listans första element har index 0.
    """

    def __init__(self):

        """Initiera den tomma listan.
        """
        self.head = None

    def is_empty(self):
        """Returnerar `True` om listan är tom, annars `False`.
        """
        return self.head is None

    def add(self, item):
        """Lägg till `item` i början av listan.
        """
        self.head = Node(item, self.head)

    def size(self):
        """Returnerar antalet värden i listan.
        """
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next

        return count

    def search(self, item):
        """Returnerar `True` om `item` finns i listan, annars `False`.
        """
        current = self.head
        while current:
            if item == current.data:
                return True
            current = current.next

        return False

    def remove(self, item):
        """Raderar första förekomsten av `item` från listan.
        """

        current = self.head

        while current:
            if current.next and current.next.data == item:
                current.next = current.next.next
                return
            elif not current.next:
                return
            current = current.next

        return

    def append(self, item):
        """Lägg till `item` i slutet av listan.
        """
        current = self.head

        while current:
            if not current.next:
                current.next = Node(item, None)
                return
            current = current.next

        self.add(item)
        return

    def insert(self, position, item):
        """Lägg till `item` på index `position`.
        """

        current = self.head
        count = 1

        while current:
            if count == position:
                current.next = Node(item, current.next)
                return
            count += 1
            current = current.next

        if position == 0:
            self.add(item)

        return

    def index(self, item):
        """Returnerar index i listan för första förekomsten av `item`.
        """
        current = self.head
        count = 0

        while current:
            if current.data == item:
                return count
            count += 1
            current = current.next

        raise EmptyList

    def pop(self, position=None):
        """Plockar bort och returnerar värdet på index `position`.

        Om inget värde anges för `position` tolkas det som sista värdet.
        """

        current = self.head
        count = 0
        retval = None

        if not position:
            try:
                retval = self.head.data
                self.head = self.head.next
                return retval
            except:
                raise EmptyList

        else:
            if current:
                while current:
                    if count == int(position):
                        retval = current.data
                        self.remove(current.data)
                        return retval
                    count += 1
                    current = current.next
            else:
                raise EmptyList

        raise IndexError
