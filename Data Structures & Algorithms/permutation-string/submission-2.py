from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        pre_dict = defaultdict(int)
        for s in s1:
            pre_dict[s] += 1
        
        my_dict = defaultdict(int)
        l = 0
        for r in range(len(s2)):
            my_dict[s2[r]] += 1
            
            if (r-l+1) > len(s1):
                my_dict[s2[l]] -= 1
                
                if my_dict[s2[l]] == 0:
                    del my_dict[s2[l]] #删除这个无用的元素, 以清洁字典, 方便以后对照
                l += 1
            
            if (r-l+1) == len(s1): #及时比对
                if len(my_dict) == len(pre_dict):
                    match = True

                    for key in pre_dict:
                        if my_dict[key] != pre_dict[key]:
                            match = False
                            break
                    if match:
                        return True
        
        return False
