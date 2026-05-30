class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_t={}
        dict_s={}
        for _ in t:
            if _ not in dict_t:
                dict_t[_]=1
            else:
                dict_t[_]+=1
        for _ in s:
            if _ not in dict_s:
                dict_s[_]=1
            else:
                dict_s[_]+=1
        if dict_t == dict_s:
            return True
        else:
            return False