class Queue:
    """A simple class to implement the Queue operations and data attributes

    Attributes:
        front (int): Value of front end
        rear (int): Value of rear end
        size (int): Size of the Queue
        Q (List): Queue containing the elements.

    Methods:
        is_full: checks whether the queue is full or not.
        is_empty: checks whether the queue is empty or not.
        front_value: returns the front end value.
        rear_value: returns the rear end value.
        enqueue: inserts the element in the queue.
        dequeue: deletes the element from the queue.
    """

    # CONSTRUCTOR
    def __init__(self, size):
        self.front = -1
        self.rear = -1
        self.size = size
        self.Q = []

    def is_full(self) -> bool:
        if self.front == 0 and (self.rear == self.size - 1):
            return True
        else:
            return False

    def is_empty(self) -> bool:
        if self.rear == -1:
            return True
        else:
            return False

    def enqueue(self, x: int) -> None:
        if self.is_full() is True:
            print("OVERFLOW")
        else:
            if self.front == -1:
                self.front = 0

            self.rear += 1
            self.Q.insert(self.rear, x)

    def dequeue(self) -> None:
        if self.is_empty() is True:
            print("UNDERFLOW")
        else:
            print(f"Value to be deleted is {self.Q[self.rear]}")
            self.rear -= 1

    def rear_value(self) -> int:
        if self.is_empty() is not True:
            return self.Q[self.rear]

    def front_value(self) -> int:
        if self.is_empty() is not True:
            return self.Q[self.front]


# Main code
queue1 = Queue(5)
queue1.enqueue(20)
queue1.enqueue(30)
queue1.enqueue(40)
queue1.enqueue(50)
queue1.enqueue(60)

# This line will show overflow
queue1.enqueue(70)

# using DEQUEUE
queue1.dequeue()

print(queue1.front_value())
print(queue1.rear_value())
