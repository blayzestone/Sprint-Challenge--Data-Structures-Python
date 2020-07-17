class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.oldest_index = 0

    def append(self, item):
        end_index = len(self.storage) - 1

        # if there is still room in the ring buffer, append the new item
        if len(self.storage) < self.capacity:
            self.storage.append(item)
        else:
            # otherwise overwrite the item at the oldest index
            self.storage[self.oldest_index] = item

            # Update the oldest index tracker to point to the next oldest item in the ring buffer
            if self.oldest_index < end_index:
                self.oldest_index += 1
            else:
                self.oldest_index = 0

    # create a copy of self.storage removing any Nontype values from it and return it
    def get(self):
        storage = [item for item in self.storage if item is not None]

        return storage
