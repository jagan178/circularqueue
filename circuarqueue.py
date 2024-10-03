class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size  # Create a list with a fixed size
        self.front = -1
        self.rear = -1

    def is_full(self):
        # Queue is full when the next position of rear is front
        return (self.rear + 1) % self.size == self.front

    def is_empty(self):
        # Queue is empty when front and rear are both -1
        return self.front == -1

    def enqueue(self, data):
        if self.is_full():
            print("Queue is full")
            return

        if self.is_empty():
            self.front = 0  # Set front to 0 if the queue was empty

        # Move rear pointer and insert data
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = data

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None

        data = self.queue[self.front]
        self.queue[self.front] = None  # Optional: Clear the dequeued element

        if self.front == self.rear:
            # Queue is now empty
            self.front = self.rear = -1
        else:
            # Move front pointer forward
            self.front = (self.front + 1) % self.size

        return data

    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.queue[self.front]

    def display(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print("Queue elements are:", end=" ")
            i = self.front
            while True:
                print(self.queue[i], end=" ")
                if i == self.rear:
                    break
                i = (i + 1) % self.size
            print()

# Example usage
cq = CircularQueue(5)
cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
cq.enqueue(4)
cq.enqueue(5)
cq.display()  # Displays the queue

print("Dequeued:", cq.dequeue())
cq.display()

cq.enqueue(6)
cq.display()
