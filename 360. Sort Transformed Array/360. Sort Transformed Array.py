class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        def quad_func(x):
            return a * (x**2) + b*x + c
        return sorted([quad_func(x) for x in nums])