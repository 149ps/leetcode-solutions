class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        bin_n = bin(n).replace("0b","")
        count = 0 
        for char in str(bin_n):
            if char == '1':
                count += 1
        return count