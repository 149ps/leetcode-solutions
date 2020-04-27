"""
Design a max stack that supports push, pop, top, peekMax and popMax.

push(x) -- Push element x onto stack.
pop() -- Remove the element on top of the stack and return it.
top() -- Get the element on the top.
peekMax() -- Retrieve the maximum element in the stack.
popMax() -- Retrieve the maximum element in the stack, and remove it. If you find more than one maximum elements, only remove the top-most one.
Example 1:
MaxStack stack = new MaxStack();
stack.push(5); 
stack.push(1);
stack.push(5);
stack.top(); -> 5
stack.popMax(); -> 5
stack.top(); -> 1
stack.peekMax(); -> 5
stack.pop(); -> 1
stack.top(); -> 5
Note:
-1e7 <= x <= 1e7
Number of operations won't exceed 10000.
The last four operations won't be called when stack is empty.
"""
class MaxStack:
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        

    def push(self, x: int) -> None:
        if not self.stack:
            self.stack.append((x,x))
        else:
            if x > self.stack[-1][1]:
                self.stack.append((x,x))
            else:
                self.stack.append((x,self.stack[-1][1]))

    def pop(self) -> int:
        return self.stack.pop()[0] 

    def top(self) -> int:
        return self.stack[-1][0]

    def peekMax(self) -> int:
        return self.stack[-1][1]

    def popMax(self) -> int:
        value = self.stack[-1][1]
        if self.stack[-1][0] == value:
            return self.stack.pop()[0]
        i = len(self.stack) - 1
        temp_list = []
        while self.stack[i][0] != value:
            temp_list.append(self.stack.pop())
            i -= 1
        max_element = self.stack.pop()[0]
        while temp_list:
            if not self.stack:
                temp = temp_list.pop()[0]
                self.stack.append((temp,temp))
            else:
                if self.stack[-1][1] < temp_list[-1][0]:
                    temp = temp_list.pop()[0]
                    self.stack.append((temp,temp))
                else:
                    temp = temp_list.pop()[0]
                    self.stack.append((temp,self.stack[-1][1]))
        return max_element
        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()