"""
Problem: Substring with Concatenation of All Words  
LeetCode #30  
Difficulty: Hard  
Link: https://leetcode.com/problems/substring-with-concatenation-of-all-words/  

Problem Statement:  
You are given a string s and an array of strings words.  
All the strings in words are of the same length.  
Return all starting indices of substring(s) in s that are a concatenation  
of each word in words exactly once and without any intervening characters.

Examples:  
Input: s = "barfoothefoobarman", words = ["foo","bar"]  
Output: [0,9]  

Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]  
Output: []  

Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]  
Output: [6,9,12]  

Approach (Sliding Window + Frequency Check):  
- Each word has the same length, say `word_len`.  
- The total window size to check is `total_len = word_len * len(words)`.  
- Build a frequency map of all words.  
- For each possible starting offset in range(word_len),  
  move a sliding window across the string in steps of word_len.  
- Maintain a temporary frequency map for the current window.  
- When the window exceeds total_len or contains an invalid word,  
  adjust the window to maintain valid counts.  
- When all counts match, record the start index.

Time Complexity: O(n * word_len)  
Space Complexity: O(m), where m is the number of unique words
"""

class Solution:
    def findSubstring(self, s, words):
        if not s or not words:
            return []

        word_len = len(words[0])
        total_len = word_len * len(words)
        word_count = {}

        # build frequency map for words
        for w in words:
            if w in word_count:
                word_count[w] += 1
            else:
                word_count[w] = 1

        res = []

        # check each possible start offset
        for i in range(word_len):
            left = i
            count = 0
            seen = {}

            for j in range(i, len(s) - word_len + 1, word_len):
                word = s[j:j + word_len]

                if word in word_count:
                    if word in seen:
                        seen[word] += 1
                    else:
                        seen[word] = 1
                    count += 1

                    # shrink window if word count exceeded
                    while seen[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        seen[left_word] -= 1
                        left += word_len
                        count -= 1

                    # valid window
                    if count == len(words):
                        res.append(left)

                        # move left forward
                        left_word = s[left:left + word_len]
                        seen[left_word] -= 1
                        left += word_len
                        count -= 1
                else:
                    # reset window
                    seen = {}
                    count = 0
                    left = j + word_len

        return res
