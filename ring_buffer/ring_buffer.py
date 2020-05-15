class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.full = False

    def append(self, item):
        if len(self.data) < self.capacity:
            self.data.append(item)
        elif len(self.data) == self.capacity:
            if not self.full:
                self.current = 0
                self.full = True
            self.data[self.current] = item
            self.current = (self.current + 1) % self.capacity

    def get(self):
        return self.data

    # Should be:
    """
    if not self.full:
        return self.data
    return self.data[self.current:] + self.data[:self.current]

    Buffer should always go oldest to youngest...
    """


if __name__ == '__main__':
    buffer = RingBuffer(3)
    print(buffer.get())

    buffer.append('a')
    buffer.append('b')
    buffer.append('c')
    print(buffer.get())

    buffer.append('d')
    print(buffer.get())

    buffer.append('e')
    buffer.append('f')
    print(buffer.get())
