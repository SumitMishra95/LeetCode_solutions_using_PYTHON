class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        maxI = 2**31-1
        minI = -1 * 2**31
        
        if x<0:
            x = -x
            x = str(x)
            x = ''.join(reversed(x))
            y = -1*int(x)
                
        else:
            x = str(x)
            x = ''.join(reversed(x))
            y = int(x)
        
        if y > maxI or y < minI:
            return 0
