class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []

        charin = []
        for h in range(len(strs)):
            charin.append(sorted([char for char in strs[h]])) 

        set_list = []    
        for i in range(len(strs)):
            if i == 0:
                set_list.append([charin[i],[strs[i]]])
            else:
                need = False
                for j in range(len(set_list)):
                    if charin[i] == set_list[j][0]:
                        need = True
                        set_list[j][1].append(strs[i])
                        break
                else:
                    if need == False:
                        set_list.append([charin[i],[strs[i]]])
                
                
                      
        return [item[1] for item in set_list]