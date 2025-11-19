class Solution(object):
    def letterCasePermutation(self, s):
        res = []

        def backtrack(path, i):
            if i == len(s):
                res.append(''.join(path))
                return

            if s[i].isalpha():
                # Branch for lowercase
                path.append(s[i].lower())
                backtrack(path, i + 1)
                path.pop()

                # Branch for uppercase
                path.append(s[i].upper())
                backtrack(path, i + 1)
                path.pop()
            else:
                # Digit, add directly
                path.append(s[i])
                backtrack(path, i + 1)
                path.pop()

        backtrack([], 0)
        return res