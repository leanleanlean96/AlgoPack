class Stack:
    def __init__(self) -> None:
        self.__stack: list[int] = []
        self.__min_values: list[int] = []
    
    def push(self, value) -> None:
        if self.is_empty() or self.__min_values[-1] > value:
            self.__min_values.append(value)
        else:
            self.__min_values.append(self.__min_values[-1])
        self.__stack.append(value)
        
    def is_empty(self) -> bool:
        return len(self) == 0
    
    def __len__(self) -> int:
        return len(self.__stack)
    
    def pop(self) -> int:
        if self.is_empty():
            raise IndexError("The stack is empty")
        self.__min_values.pop()
        return self.__stack.pop()
    
    def peek(self) -> int:
        if self.is_empty():
            raise IndexError("The stack is empty")
        return self.__stack[-1]
    
    def min(self) -> int:
        if self.is_empty():
            raise IndexError("The stack is empty")
        return self.__min_values[-1]
