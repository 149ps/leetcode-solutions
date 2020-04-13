"""
Design and implement a TwoSum class. It should support the following operations: add and find.

add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.

Example 1:

add(1); add(3); add(5);
find(4) -> true
find(7) -> false
Example 2:

add(3); add(1); add(2);
find(3) -> true
find(6) -> false
"""
class TwoSum:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hmap = {}

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.hmap[number] = self.hmap.get(number,0) + 1
        
        
        

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for num in self.hmap.keys():
            comple = value - num
            if num != comple:
                if comple in self.hmap:
                    return True
            elif self.hmap[num] > 1:
                return True
        
        return False    
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)