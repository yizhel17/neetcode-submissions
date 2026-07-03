class Solution:

    def encode(self, strs: List[str]) -> str:
        # #需要做好标识符, 标记好每一个字符串的结束.字符串需要被长度标记, 长度也需要被特殊符号标记.
        # encode = ""
        # for s in strs:
        #     encode += str(len(s)) + "#" + s
        
        # return encode

        parts = []

        for s in strs:
            parts.append(f"{len(s)}#{s}")
        return "".join(parts)

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0

        while i < len(s):
            
            j = i

            while s[j] != "#":
                j += 1
            
            leng = int(s[i:j])

            true_str = s[j+1: j+leng+1]

            ans.append(true_str)

            i = j + 1 + leng
        
        return ans
