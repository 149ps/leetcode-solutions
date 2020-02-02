"""
Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks. Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.

You need to return the least number of intervals the CPU will take to finish all the given tasks.

 

Example:

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
 

Note:

The number of tasks is in the range [1, 10000].
The integer n is in the range [0, 100].
"""
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hMap = collections.Counter(tasks)
        result = 0 
        maxHeap = [(-val,key) for key,val in hMap.items()]
        heapq.heapify(maxHeap)
        while maxHeap:
            stack,count = [],0
            for i in range(n+1):
                if maxHeap:
                    item = heapq.heappop(maxHeap)
                    count += 1
                    if item[0] < -1:
                        stack.append((item[0]+1,item[1]))
            for element in stack:
                heapq.heappush(maxHeap,element)
            if maxHeap:
                result += (n+1)
            else:
                result += count
        return result