class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        minL = float("inf")
        ans = ""

        t_dict = collections.defaultdict(int)
        for cha in t:
            t_dict[cha] += 1
        
        s_cur_dict = collections.defaultdict(int)
        left = 0
        for right in range(len(s)):
            s_cur_dict[s[right]] += 1

            if (right - left + 1) < len(t):
                continue
            
            
            contain = True

            #看是否包含t
            for let in t_dict:
                if s_cur_dict[let] < t_dict[let]:
                    contain = False
                    break
            
            #已经包含t在内,缩小窗口
            while contain:
                if (right - left + 1) < minL:
                    minL = right - left + 1
                    ans = s[left: right + 1] 
                    #保证不被ans的长度随minL而变, 而不是当前的长度
                
                s_cur_dict[s[left]] -= 1

                if s_cur_dict[s[left]] <= 0:
                    del s_cur_dict[s[left]]
                
                left += 1

                # 重新判断窗口是否仍然满足
                contain = True
                for let in t_dict:
                    if s_cur_dict[let] < t_dict[let]:
                        contain = False
                        break

        return ans
                        