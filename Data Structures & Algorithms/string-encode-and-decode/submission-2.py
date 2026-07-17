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
        res = []

        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            my_str = s[j+1:j+length+1]

            res.append(my_str)

            i = j + length + 1
        
        return res