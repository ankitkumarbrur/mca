class Stack:
    '''
    Stack Class:

    Attributes:
    stack : list type object that will store stack items
    top : points to the top of the stack
    size : the size of the stack

    Methods:
    isEmpty : 
        Returns True if the stack is empty, False otherwise
    
    isFull : 
        Returns True if the stack is full, False otherwise

    clear :
        clears/empties the stack 

    push :
        pushes an item onto the stack 
    
    pop :
        pop an item off the stack 
    
    peek:
        returns the top of the stack without poppint it
    '''
    def __init__(self,size):
        '''
        Constructor for the Stack class:
        Attributes:
            size: size of the stack
        '''
        self.stack = []     # list to store stack items
        self.top = -1       # top pointer for stack
        self.size = size    # size of the current stack

    def __str__(self):
        '''
        __str__ function defination for Stack class
        Prints the stack items.
        '''
        return 'Stack('+', '.join(map(str,self.stack))+' <--Top)'

    def __len__(self):
        '''
        __len__ function defination for Stack class
        Returns the stack length/size.
        '''
        return self.size

    def isEmpty(self):
        '''
        returns True if stack is empty False otherwise
        '''
        return True if self.top == -1 else False

    def isFull(self):
        '''
        returns True if stack is Full False otherwise
        '''
        return True if self.top == self.size-1 else False

    def clear(self):
        '''
        empties the stack
        '''
        self.top = -1
        self.stack.clear()

    def push(self,item):
        '''
        Pushes an item on the stack if stack is not full
        Attributes:
            item: item to be pushed on the stack
        '''
        if self.isFull():
            raise Exception("OverflowError: The stack is full can't push")
        self.stack.append(item)
        self.top += 1

    def pop(self):
        '''
        Pops an item off the stack and returns it if stack is not empty
        '''
        if self.isEmpty():
            raise Exception("UndeflowError: The stack is empty can't pop")
        
        item = self.stack.pop()
        self.top -= 1
        return item

    def peek(self):
        '''
        returns the top of the stack element
        '''
        if self.isEmpty():
            raise Exception("UndeflowError: The stack is empty nothing on top")
        return self.stack[self.top]