class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        
        count = 0
        for w in words:
            if set(w).union(allowed) == allowed:
                count += 1

        return count
