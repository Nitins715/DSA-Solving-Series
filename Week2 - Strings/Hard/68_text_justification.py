"""
Problem: Text Justification
LeetCode #68
Difficulty: Hard
Link: https://leetcode.com/problems/text-justification/

Problem Statement:
Given an array of strings words and a width maxWidth, format the text such that each line 
has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach — that is, pack as many words as you can 
in each line. Add extra spaces between words so that each line has exactly maxWidth characters.

If the number of spaces on a line does not divide evenly between words, 
the extra spaces should be distributed as evenly as possible from left to right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

Examples:
Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]

Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]

Approach:
- Use a greedy approach to build lines word by word.
- When adding the next word exceeds maxWidth, justify the current line.
- Distribute spaces evenly between words. If spaces don’t divide evenly, 
  extra spaces go to the leftmost gaps.
- The last line should be left-aligned and filled with spaces at the end.

Time Complexity: O(n), where n = number of words
Space Complexity: O(n)
"""

class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        res = []
        line = []
        line_length = 0

        for word in words:
            # Check if adding this word exceeds the maxWidth
            if line_length + len(word) + len(line) > maxWidth:
                # Distribute spaces
                total_spaces = maxWidth - line_length
                if len(line) == 1:
                    # If only one word, pad right with spaces
                    res.append(line[0] + ' ' * total_spaces)
                else:
                    # Evenly distribute spaces
                    spaces_between = total_spaces // (len(line) - 1)
                    extra_spaces = total_spaces % (len(line) - 1)

                    line_str = ""
                    for i in range(len(line) - 1):
                        line_str += line[i]
                        # Add an extra space to the first few gaps if needed
                        line_str += ' ' * (spaces_between + (1 if i < extra_spaces else 0))
                    line_str += line[-1]
                    res.append(line_str)

                # Start new line
                line = []
                line_length = 0

            line.append(word)
            line_length += len(word)

        # Handle the last line (left-justified)
        last_line = ' '.join(line)
        last_line += ' ' * (maxWidth - len(last_line))
        res.append(last_line)

        return res
