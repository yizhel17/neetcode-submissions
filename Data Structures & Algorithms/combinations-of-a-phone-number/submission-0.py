class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        cur = []

        digitToChar = {

            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"

        }

        def bck(start):
            if len(cur) == len(digits):
                ans.append("".join(cur))
                return

            for char in digitToChar[digits[start]]:
                    cur.append(char)

                    bck(start + 1)

                    cur.pop()
        
        if digits:
            bck(0)

        return ans
