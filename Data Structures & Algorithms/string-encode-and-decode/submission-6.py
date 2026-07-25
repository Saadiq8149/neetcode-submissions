class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += f"__join__{s}"
        return encoded 

    def decode(self, s: str) -> List[str]:
        return s.split("__join__")[1:]