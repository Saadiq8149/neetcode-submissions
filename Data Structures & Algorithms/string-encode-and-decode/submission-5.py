class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += f"__join__{len(s)}__{s}"
        return encoded 

    def decode(self, s: str) -> List[str]:
        return [x.split("__")[-1] for x in s.split("__join__")[1:]]