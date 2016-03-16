"""Övningar på BinarySearchTree (BST).

Ett BST är ett rotat binärt träd där varje nod har en `key` och ett
eventuellt värde, `value`. Varje nod i trädet finns två träd,
`left` och `right`. En nods `key` måste vara större än alla noders `key`
i det vänstra trädet och mindre än alla noders `key` i det högra trädet.

Utseendet hos ett BST beror i väldigt hög grad på i vilken ordning noderna
lagts till. I värsta fall degenererar de fullständigt.

`Wikipedia <https://en.wikipedia.org/wiki/Binary_search_tree>`_
"""


class BinarySearchTree():
    """Implementation av BinarySearchTree (BST)."""

    def __init__(self, key, value=None):
        """Initiera det tomma trädet."""
        self.key = key
        self.left = None
        self.right = None
        self.value = value

    def insert(self, key, value=None):
        """Lägg till en nod i trädet."""

        if key < self.key:
            if self.left:
                self.left.insert(key, value)
            else:
                self.left = BinarySearchTree(key, value)

        elif key >= self.key:
            if self.right:
                self.right.insert(key, value)
            else:
                self.right = BinarySearchTree(key, value)


    def lookup(self, key):
        """Sök efter noden med matchande key.

        Returnerar matchande noden eller None.
        """

        current = self
        parent = None

        while current:
            if current.key == key:
                break

            parent = current
            if current.key > key:
                current = current.left
            else:
                current = current.right

        return current, parent


    def delete(self, key):
        #Radera noden med matchande key.

        node, parent = self.lookup(key)

        children_count = 0
        if node.left:
            children_count += 1
        if node.right:
            children_count += 1


        if children_count == 0:
            if parent is None:
                raise Exception(msg = "You may not delete the last node.")
            else:
                if parent.left is node:
                    parent.left = None
                else:
                    parent.right = None

        elif children_count == 1:
            if parent.left is node:
                if node.right is None:
                    parent.left = node.left
                else:
                    parent.left = node.right
            else:
                if node.right is None:
                    parent.right = node.left
                else:
                    parent.right = node.right

        else: # children_count == 2
            successor = node.right
            successor_parent = node

            while successor.left:
                successor_parent = successor
                successor = successor.left

            if parent:
                successor.left = node.left
                successor.right = node.right

                if parent.left is node:
                    parent.left = successor
                else:
                    parent.right = successor

            else: # no parent
                node.key = successor.key
                node.value = successor.value

            if successor_parent.left is successor:
                successor_parent.left = None
            else:
                successor_parent.right = None


    def traverse(self):
        """En in-order traversering av trädets noder.

        Implementera som en generator.
        """

        if self.left:
            for node in self.left.traverse():
                yield node

        yield self

        if self.right:
            for node in self.right.traverse():
                yield node


    def __eq__(self, other):
        if other is None:
            return False
        return self.key == other.key and self.left == other.left and self.right == other.right


    def __str__(self):
        """Utskrift av trädets alla noder (in-order)."""
        # Använd traverse...

        li = []

        for node in self.traverse():
            li.append(node.key)

        return str(li)
