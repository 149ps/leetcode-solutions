class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        def count_ones(n):
            return bin(n).replace("0b","").count('1')
        final_arr = []
        for i in range(num+1):
            final_arr.append(count_ones(i))
        return final_arr