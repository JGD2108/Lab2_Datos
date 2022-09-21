class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __iter__(self):
        return self.data

    def __repr__(self):
        return str(self.data)