class Solution:

    def encode(self, strs: List[str]) -> str:
        sentence = ""
        for strings in strs:
            if strings == "":
                sentence = sentence + 'a' + strings
            else:
                sentence = sentence + chr(ord('a')+len(strings)+1) + strings
        return sentence
    def decode(self, s: str) -> List[str]:
        res = []
        cursor = int(0)
        step = int(0)
        i = int(0);
        
        while cursor < len(s):
            step = ord(s[cursor])-ord('a')
            if step == 0:
                res.append("")
                cursor += 1
            else:
                res.append(s[(cursor+1):(cursor+step)])
                cursor += step
        return res