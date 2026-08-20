"""
Pila (Stack) implementation in Python
Pila LIFO (Last In First Out)  
"""

class Pila:

    def __init__(self) -> None:
        """ Initializes an empty stack."""
        self.items: list[any] = []


    def is_empty(self) -> bool:
        """
        Checks if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return len(self.items) == 0


    def push(self, item: any) -> None:
        """
        Adds an item to the top of the stack.

        Args:
            item (any): The item to be added to the stack.
        """
        self.items.append(item)


    def pop(self) -> any:
        """
        Removes and returns the top item in the stack.

        Returns:
            any: The top item in the stack.

        Raises:
            IndexError: If the stack is empty.
        """
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from empty stack")


    def peek(self) -> any:
        """
        Returns the top item in the stack without removing it.

        Returns:
            any: The top item in the stack.

        Raises:
            IndexError: If the stack is empty.
        """
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from empty stack")


    def size(self) -> int:
        """
        Returns the number of items in the stack.

        Returns:
            int: The number of items in the stack.
        """
        return len(self.items)


    def __str__(self) -> str:
        """
        Returns a string representation of the stack.

        Returns:
            str: A string representation of the stack.
        """
        return str(self.items)


# Example usage
if __name__ == "__main__":

    # Create a stack and perform some operations
    stack = Pila()

    # add items to the stack
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)

    # print the stack and its properties
    print("Stack:", stack)  # Output: Stack: [10, 20, 30, 40]
    print("Top item:", stack.peek())  # Output: Top item: 40
    print("Stack size:", stack.size())  # Output: Stack size: 4

    # remove the top item from the stack
    print("Popped item:", stack.pop())  # Output: Popped item: 40
    print("Stack after pop:", stack)  # Output: Stack after pop: [10, 20, 30]
    print("stack size after pop:", stack.size())  # Output: Stack size after pop: 3