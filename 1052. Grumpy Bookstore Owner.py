class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        satisfied_c = max_c = temp = 0
        for i in range(len(customers)):
            if not grumpy[i]:
                satisfied_c += customers[i]
                customers[i] = 0
            else:
                temp += customers[i]
            if i >= X:
                temp -= customers[i-X]
            max_c = max(max_c,temp)
        return satisfied_c+max_c
        
