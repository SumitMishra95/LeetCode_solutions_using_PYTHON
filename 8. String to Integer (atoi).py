class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        
        s = list(str.lstrip())
        if len(s) == 0:
            return 0
        
        if s[0] == "-":
            sign = -1
        else:
            sign = 1
            
        if s[0] in ['-', '+']:
            del s[0]
            
        ans, i = 0, 0
        while i < len(s) and s[i].isdigit():
            ans = ans*10 + int(s[i])
            i += 1
        
        return max(-2**31, min(sign*ans, 2**31-1))
