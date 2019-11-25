class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        bin_n = str('{:0b}'.format(n))
        for i in range(len(bin_n)-1):
            if bin_n[i] == bin_n[i+1]:
                return False
        return True