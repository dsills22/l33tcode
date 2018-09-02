
#Given a string, find the length of the longest substring without repeating characters.

#Input: "pwwkew"
#Output: 3
#Explanation: The answer is "wke", with the length of 3. 
#             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
    	posn = {}
    	left = 0
    	right = 0
    	#bestLeft = 0
    	#bestRight = 0
    	longest = 0
    	l = len(s)
    	for right in range(0, l):
    		c = s[right]
    		if c in posn and posn[c] >= left:
    			#rally broken
    			left = posn[c] + 1 #prev posn + 1
    			posn[c] = right #set new posn
    		else:
    			posn[c] = right
    			currRally = right - left + 1
    			if currRally > longest:
    				longest = currRally
    				#bestLeft = left
    				#bestRight = right
    	#return s[bestLeft : bestRight+1]
    	return longest

sol = Solution()
print(sol.lengthOfLongestSubstring("pwwkew"))
print(sol.lengthOfLongestSubstring("abcabcbb"))
print(sol.lengthOfLongestSubstring("bbbbb"));
print(sol.lengthOfLongestSubstring("qwertyuioptasdfghjkly"))
print(sol.lengthOfLongestSubstring(""))
print(sol.lengthOfLongestSubstring("qwertyuiop"))
