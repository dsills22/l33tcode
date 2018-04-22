class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        ret = ""
        carry = "0"
        larger = ""
        smaller = ""
        
        if len(a) >= len(b):
            larger = a
            smaller = b
        else:
            larger = b
            smaller = a
        
        for i in range(1, len(larger) + 1):
            largerVal = larger[len(larger) - i]
            
            if i > len(smaller):
                smallerVal = "0"
            else:
                smallerVal = smaller[len(smaller) - i]
            
            if largerVal == "1" and smallerVal == "1":
                ret = carry + ret
                carry = "1"
            elif (largerVal == "0" and smallerVal == "1") or (largerVal == "1" and smallerVal == "0"):
                if carry == "1":
                    ret = "0" + ret
                else:
                    ret = "1" + ret
            else:
                ret = carry + ret
                carry = "0"
        if carry == "1":
            ret = carry + ret
        return ret
            
sol = Solution()       
print(sol.addBinary("110010010", "1011011"))
print("111101101")
