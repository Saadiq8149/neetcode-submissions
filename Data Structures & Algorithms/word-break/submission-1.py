class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def dp(s, wordDict, memo={}):
            if s in memo:
                return memo[s]
            
            if s == "":
                return True
            
            for w in wordDict:
                if s.startswith(w):
                    if dp(s[len(w):], wordDict, memo):
                        memo[s] = True
                        return True

            memo[s] = False
            return False

        return dp(s, wordDict)
