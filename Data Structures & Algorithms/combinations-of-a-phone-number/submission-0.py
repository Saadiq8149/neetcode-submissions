class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        combinations, current = [], ""

        if digits == "":
            return []

        self.mapping = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        } 

        def helper(combinations, current, digits, i):
            if i == len(digits):
                combinations.append(current)
                return

            digit = digits[i]
            for c in self.mapping[digit]:
                helper(combinations, current+c, digits, i+1)
                


        helper(combinations, current, digits, 0)
        return combinations
