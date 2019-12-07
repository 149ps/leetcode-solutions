class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [arr[0] for arr in collections.Counter(nums).most_common(k)]