#LENGTH OF LONGEST SUBSTRING
#(utilizes sliding window to assign the dictionary values of len of substring at each character)
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        cur, max_length, start = 0, 0, 0
        n = len(s)
        i = 0
        lookup = {}
        while i < n:
            if s[i] not in lookup:
                cur += 1
            else:
                start = max(start, lookup[s[i]])
                cur = i - start #eg 1-1=0 for a 
            lookup[s[i]] = i
            max_length = max(cur, max_length)
            i += 1
        return max_length

    def length_of_longest_substring(self, s):
        # Initialize variables
        start = 0  # Start index of the window
        max_length = 0  # Length of the longest substring
        char_index_map = {}  # Map to store the last index of each character
    
        # Iterate through the string
        for end in range(len(s)):
            # If the character is already in the map and its index is greater than or equal to the start index
            if s[end] in char_index_map and char_index_map[s[end]] >= start:
                # Move the start index to the right of the last occurrence of the current character
                start = char_index_map[s[end]] + 1
    
            # Update the last index of the character
            char_index_map[s[end]] = end
    
            # Update the maximum length if the current substring is longer
            max_length = max(max_length, end - start + 1)
    
        return max_length


# Test the Solution class
m = Solution()
print(m.lengthOfLongestSubstring('abcade'))
print(m.length_of_longest_substring('abcade'))
