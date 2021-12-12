class Stack(object):
    """A class for creating Stack

    Attributes:
        top (int): will store the value of top of stack.
        size (int): will store the number of elements the stack can contain.

    Methods:
        push(x: int): will insert the given value `x` from the top of the stack if it is not full.
        pop(): will delete the element from the top of the stack.
        top_value(): it will return the value at the top of the stack.
        is_full(): will check if the stack is full or not.
        is_empty(): it will check if the stack is empty or not.
    """
    def __init__(self, size: int):
        self.top = -1
        self.size = size
        self.status = "empty"
        self.S = list([] * self.size)

    def is_full(self) -> str:
        if self.top == (self.size - 1):
            print("STACK is full")
            self.status = "full"
        else:
            self.status = ""

        return self.status

    def is_empty(self) -> str:
        if self.top == -1:
            print("STACK is empty")
            self.status = "empty"
        else:
            self.status = ""

        return self.status

    def push(self, x: int) -> None:
        """Insert the element in the STACK"""
        if self.is_full() == "full":
            print("OVERFLOW")
        else:
            print("PUSH operation is possible")
            self.top += 1
            self.S.insert(self.top, x)

    def pop(self) -> None:
        """Delete the element in the STACK"""
        if self.is_empty() == "empty":
            print("UNDERFLOW")
        else:
            print("POP operation is possible")
            print("Value to be deleted is {0}".format(self.S[self.top]))
            self.top -= 1

    def top_value(self) -> int:
        """Returns the top value"""
        if self.is_empty() == "empty":
            print("No element in the stack")
        else:
            return self.S[self.top]


# Main code
stack1 = Stack(5)
stack1.push(20)
stack1.push(30)
stack1.push(40)
stack1.push(50)

stack1.pop()
print(stack1.top_value())
stack1.push(60)
stack1.push(45)
stack1.push(23)
print(stack1.top_value())
stack1.pop()
