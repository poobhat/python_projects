"""Linear Queue"""

class MyQueue:
    def __init__(self, data=None, p_start=0):
        data = [] if data is None else data
        self.data = data # Dynamic list to store elements
        self.p_start = p_start # A pointer to indicate the start position

    # Insert an element into the queue. Return true if the operation is successful. */
    def enQueue(self, node):
        self.data.append(node)
        return True

    # Delete an element from the queue. Return true if the operation is successful.
    def deQueue(self):
        if self.isEmpty():
            return False
        self.p_start += 1
        return True

    # Get the front item from the queue.
    def Front(self):
        return self.data.get(self.p_start)

    # Checks whether the queue is empty or not
    def isEmpty(self):
        return self.p_start >= len(self.data)

