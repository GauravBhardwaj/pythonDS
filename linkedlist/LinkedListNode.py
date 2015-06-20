class Node(object):
    def __init__(self, init_data, next=None):
        self.data = init_data
        self.next = next

    def get_data(self):
        return self.data

    def set_data(self, new_data):
        self.data = new_data

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next
