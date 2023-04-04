class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        # Push the new element onto the first stack
        self.stack1.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        # If the second stack is empty, transfer all elements from the first stack
        # to the second stack in reverse order
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        # Pop the top element from the second stack, which will be the oldest element
        return self.stack2.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        # If the second stack is empty, transfer all elements from the first stack
        # to the second stack in reverse order
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        # Return the top element from the second stack, which will be the oldest element
        return self.stack2[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        # The queue is empty if both stacks are empty
        return not self.stack1 and not self.stack2


# Create a new queue
queue = MyQueue()

# Add elements to the queue
queue.push(1)
queue.push(2)
queue.push(3)

# Check the front element of the queue
print(queue.peek())    # Output: 1

# Remove the front element from the queue
print(queue.pop())     # Output: 1

# Check if the queue is empty
print(queue.empty())   # Output: False
