from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, data):
        self.data = data
        self.i = 0

    def __next__(self):
        try:
            current = self.data[self.i]
            if current:
                self.i += 1

            return current

        except Exception:
            raise StopIteration
