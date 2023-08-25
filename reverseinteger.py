class Solution:
    def reverse(self, x: int) -> int:
        s = list(str(x))
        if '-' in s:
            s.remove('-')
            val = -int(''.join(reversed(s)))
            return val if val>-2**31 else 0
        val = int(''.join(reversed(s)))
        return val if val<2**31 -1 else 0
        
            
        
        
        