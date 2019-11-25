class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x_str = str('{:032b}'.format(x))
        y_str = str('{:032b}'.format(y))
        count = 0
        for i in range(len(x_str)):
            if not x_str[i] == y_str[i]:
                count+=1
        return count