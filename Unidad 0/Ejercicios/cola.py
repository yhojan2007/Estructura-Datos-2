""" 
Cola (queue) implementation in Python
Cola FIFO (First In First Out) 
"""

class Cola:

    def __init__(self) -> None:
        """ Initializes an empty queue."""
        self.items: list[any] = []


    def is_empty(self) -> bool:
        """ 
        Checks if the queue is empty.

        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return len(self.items) == 0


    def enqueue(self, item: any) -> None:
        """
        Adds an item to the end of the queue.

        Args:
            item (any): The item to be added to the queue.
        """
        self.items.append(item)


    def dequeue(self) -> any:
        """ 
        Removes and returns the first item in the queue.

        Returns:
            any: The first item in the queue.

        Raises:
            IndexError: If the queue is empty.
        """
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("dequeue from empty queue")


    def peek(self) -> any:
        """ 
        Returns the first item in the queue without removing it.

        Returns:
            any: The first item in the queue.

        Raises:
            IndexError: If the queue is empty.
        """
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("peek from empty queue")


    def size(self) -> int:
        """ 
        Returns the number of items in the queue.

        Returns:
            int: The number of items in the queue.
        """
        return len(self.items)


    def __str__(self) -> str:
        """ 
        Returns a string representation of the queue.

        Returns:
            str: A string representation of the queue.
        """
        return str(self.items)


# Example usage
if __name__ == "__main__":
    # Create a queue and perform some operations
    queue = Cola()

    # Enqueue items
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.enqueue(40)

    # Display the queue and its properties
    print("Queue:", queue)  # Output: Queue: [10, 20, 30, 40]
    print("Front item:", queue.peek())  # Output: Front item: 10
    print("Queue size:", queue.size())  # Output: Queue size: 4

    # Dequeue an item
    print("Dequeued item:", queue.dequeue())  # Output: Dequeued item: 10
    print("Queue after dequeue:", queue)  # Output: Queue after dequeue: [20, 30, 40]
    print("Queue size after dequeue:", queue.size())  # Output: Queue size after dequeue: 3