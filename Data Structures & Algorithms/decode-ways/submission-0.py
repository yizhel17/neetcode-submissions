class Solution:
    def numDecodings(self, s: str) -> int:
        #此题就是因为要 判断 解码的字符串是否有以0开头的情况
        if not s or s[0] == "0":
            return 0
        
        n = len(s)
        dp = [0] * (n + 1) #包含了dp[0], dp数组: 前i个字符的解码总方法数.

        dp[0] = 1 #辅助i-2时的累加
        dp[1] = 1 #长度为1的字符串的解码总方法数, 辅助i-1的累加

        for i in range(2, n + 1):
            #单字符串解码
            one_digit = int(s[i - 1]) #"123", i = 2, s[i-1] = "2"
            if 1 <= one_digit <= 9:
                dp[i] += dp[i - 1]
            
            two_digit = int(s[i - 2: i])
            if 10 <= two_digit <= 26:
                dp[i] += dp[i - 2]
        
        return dp[-1]
