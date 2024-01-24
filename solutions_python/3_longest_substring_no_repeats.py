"""
Given a string s, find the length of the longest 
substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""

def lengthOfLongestSubstring(s):
    """
    Let's do this in one iteration of the string...
    """
    dictOfCharacters = {}
    #
    workingSubstring = '';
    currentLongestSubstring = '';
    for char in s:
        # Use the try-catch block here for O(1) checking whether or not the key exists in the dictionary.
        # Is it hacky? Yes. Is it efficient and fast (which is what these DSA questions care about)? Also yes.
        try:
            if(dictOfCharacters[char]):
                # Mission failed: Duplicate character detected!
                # Set currentLongestSubstring to workingSubstring if it's longer
                if(len(workingSubstring) > len(currentLongestSubstring)):
                    currentLongestSubstring = workingSubstring
                # Reset out dict and workingSubstring at current place.
                workingSubstring = ''
                workingSubstring += char
                dictOfCharacters = {}
                dictOfCharacters[char] = True
        except KeyError:
            dictOfCharacters[char] = True
            workingSubstring += char

    # Final check
    if(len(workingSubstring) > len(currentLongestSubstring)):
        currentLongestSubstring = workingSubstring

    return f"{len(currentLongestSubstring)}, '{currentLongestSubstring}'"

if __name__ == '__main__':
    s1 = "abcabcbb"
    print(lengthOfLongestSubstring(s1)) # 3, 'abc'

    s2 = "bbbbb"
    print(lengthOfLongestSubstring(s2)) # 1, 'b'

    s3 = "pwwkew"
    print(lengthOfLongestSubstring(s3)) # 3, 'wke'

    s4 = "dvdf"
    print(lengthOfLongestSubstring(s4)) # 3, 'vdf'
