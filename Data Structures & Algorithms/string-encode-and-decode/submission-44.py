class Solution:

    def encode(self, strs: List[str]) -> str:
        sentence = ""
        for strings in strs:
            sentence = sentence + chr(ord('a')+len(strings)) + strings
        return sentence
    def decode(self, s: str) -> List[str]:
        res = []
        cursor = int(0)
        
        while cursor < len(s): 
            res.append(s[(cursor+1):(cursor+ord(s[cursor])-ord('a')+1)])
            cursor += ord(s[cursor])-ord('a')+1
        return res