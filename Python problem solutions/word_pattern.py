'''
Link: https://leetcode.com/problems/word-pattern/

Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters that may be separated
by a single space.
'''

class Solution:
    def wordPattern(self, pattern, str):
        words_list = str.split(' ')
        if len(pattern) == len(words_list):
            di = {}
            factored_words = []
            for i in range(len(words_list)):
                if words_list[i] not in factored_words:
                    di[pattern[i]] = words_list[i]
                factored_words.append(words_list[i]) 
            final = ''
            for char in pattern:
                final += di[char] + ' ' if char in di else ''
            return str == final[:-1]
        else:
            return False

sol = Solution()
print(sol.wordPattern('abba', 'dog cat cat dog'))  # Output: True