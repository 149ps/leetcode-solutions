class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        def count_ones(n):
            bin_n = bin(n).replace("0b","")
            count = 0 
            for char in str(bin_n):
                if char == '1':
                    count += 1
            return count
        final_arr = []
        for i in range(num+1):
            final_arr.append(count_ones(i))
        return final_arr