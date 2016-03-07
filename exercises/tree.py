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


    def lookup(self, key, parent=None, rp=False):
        """Sök efter noden med matchande key.

        Returnerar matchande noden eller None.
        """

        if key == self.key:
            return parent if rp else self
        elif key < self.key and self.left:
            return self.left.lookup(key, parent=self, rp=rp)
        elif key > self.key and self.right:
            return self.right.lookup(key, parent=self, rp=rp)

        return None

    def delete(self, key):
        """Radera noden med matchande key."""

        bovpappa = self.lookup(key, rp=True)
        bov = self.lookup(key)

        nybovpappa = None
        nybov = None

        if bov:

            if bov.left:
                current = bov.left

                while current:

                    if not current.right.right:
                        nybovpappa = current
                        nybov = current.right

                    current = current.right

                nybovpappa.right = nybov.left

            elif bov.right:
                current = bov.right

                while current:
                    if not current.left.left:
                        nybovpappa = current
                        nybov = current.left

                nybovpappa.left = nybov.right

            else:
                if bovpappa:
                    if bov == bovpappa.left:
                        bovpappa.left = None
                    elif bov == bovpappa.right:
                        bovpappa.right = None
                else:
                    del self

                return

            nybov.left, nybov.right = bov.left, bov.right

            if bovpappa:
                if bov == bovpappa.left:
                    bovpappa.left = nybov
                elif bov == bovpappa.right:
                    bovpappa.right = nybov
            else:
                self.key = nybov.key
                self.left = nybov.left
                self.right = nybov.right

        else:
            raise ValueError

        return

    def traverse(self, this=None):
        """En in-order traversering av trädets noder.

        Implementera som en generator.
        """

        if not this: this = self

        if this.left:
            for node in self.traverse(this.left):
                yield node

        yield this

        if this.right:
            for node in self.traverse(this.right):
                yield node


    def __str__(self):
        """Utskrift av trädets alla noder (in-order)."""
        # Använd traverse...

        li = []

        for node in self.traverse():
            li.append(node.key)

        return str(li)

if __name__ == "__main__":

    b = BinarySearchTree(12)
    b.insert(3)
    b.insert(10)
    b.insert(1)
    b.insert(0)
    b.insert(3)
    b.insert(5)
    b.insert(20)
    b.insert(18)
    b.insert(21)
    print(b)
