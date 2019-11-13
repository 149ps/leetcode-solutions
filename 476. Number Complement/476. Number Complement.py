class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        final_str = ''
        bin_num = "{0:b}".format(num)
        def flip(c):
            return '1' if c=='0' else '0'
        for char in str(bin_num):
            final_str += flip(char)
        return int(final_str,2)