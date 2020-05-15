class RingBuffer:
    def __init__(self, capacity):
        self.capacity=capacity
        self.storage = []
        self.c_position = 0

    def append(self, item):
        self.item = item
        if len(self.storage) < self.capacity:
            self.storage.append(self.item)
        else:
            self.storage[self.c_position]=self.item
        self.c_position += 1
        if self.c_position == self.capacity:
            self.c_position = 0 


    def get(self):
        return self.storage