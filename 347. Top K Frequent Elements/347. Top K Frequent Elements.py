class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = collections.Counter(nums).most_common(k)
        return [arr[0] for arr in hmap]