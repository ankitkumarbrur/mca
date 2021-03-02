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
        

class Queue:
    '''
    A circular queue(FIFO) implementation of fuxed size.

    Properties:
    ----------
    size: max size of the elements you can insert in the queue

    Methods:
    --------
    enqueue: to insert elements into the queue structure from the rear.
    dequeue: to delete elements from the queue structure from the front.
    __str__: to print the queue
    __len__: to get th length of the queue

    '''

    def __init__(self,size):
        '''
        Constructor for the Queue.

        Attributes:
        ----------
        size: size of the queue.
        '''
        self.__front = -1
        self.__rear = -1
        self.size = size
        self.__queue = list(range(size))

    def __len__(self):
        '''
        Defination of built-in function len() for our class Queue
        '''
        if self.__rear < self.__front:
            return self.size - self.__front + self.__rear + 1
        elif self.__rear == -1:
            return 0
        else:
            return self.__rear - self.__front + 1
    
    def __str__(self):
        '''
        Overridden defination of built-in function print() for our class Queue
        '''
        s = ""
        if self.__front != -1:
            if self.__front <= self.__rear:
                for i in range(self.__front,self.__rear+1):
                    s += str(self.__queue[i]) + " "
            else:
                for i in range(self.__front,self.size):
                    s += str(self.__queue[i]) + " "
                for i in range(0,self.__rear+1):
                    s += str(self.__queue[i]) + " "
        return s

    def isEmpty(self):
        if self.__front == -1:
            return True

    def isFull(self):
        if (self.__rear + 1) % self.size == self.__front:
            return True
    
    def enqueue(self,item):
        '''
        Inserts an element at the rear end of the Queue if it is not full.

        Attributes:
        ----------
        item: The item to be enqueued
        '''
        if (self.__rear + 1) % self.size == self.__front:
            raise Exception("__queue is full")

        if self.__front == -1: self.__front = 0

        self.__rear = (self.__rear + 1) % self.size
        self.__queue[self.__rear] = item

    def dequeue(self):
        '''
        Inserts an element at the rear end of the Queue if it is not full.

        Returns:
        -------
            The dequeued item from the front of the queue.
        '''
        if self.__front == -1:
            raise Exception("__queue is empty")

        item = self.__queue[self.__front]

        if self.__front == self.__rear:
            self.__front = self.__rear = -1

        else:
            self.__front = (self.__front + 1) % self.size

        return item