class Solution:
    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "__empty__"
        return "_._".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "__empty__":
            return []
        return s.split("_._")