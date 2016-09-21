# -*- coding:utf-8 -*-
"""
正则表达式匹配
请实现一个函数用来匹配包括'.'和'*'的正则表达式。模式中的字符'.'表示任意一个字符，
而'*'表示它前面的字符可以出现任意次（包含0次）。 在本题中，匹配是指字符串的所有字符匹配整个模式。
例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配
"""
class Solution:
    #法2：动态规划
    def match(self, s, pattern):
        """设dp[i][j]表示s(0, i)与pattern(0, j)匹配
        如果pattern[j]=="." or s[i]==pattern[j]，dp[i][j] = dp[i-1][j-1]
        如果pattern[j]=="*"， 则dp[i][j] = dp[i][j-2] or dp[i][j-1] or (dp[i-1][j] and pattern[j]=="." or s[i]==pattern[j])
        """
        m, n = len(s), len(pattern)
        if m==0 and n==0:
            return True
        dp = [ [False]*(n+1) for _ in range(m+1)]
        #初始化
        dp[0][0] = True
        for j in range(1, n+1):
            if j>1 and pattern[j-1]=="*":
                dp[0][j] = dp[0][j-2]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if pattern[j-1]=="." or pattern[j-1]==s[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                elif pattern[j-1]=="*":
                    dp[i][j] = dp[i][j-2] or dp[i][j-1] or dp[i-1][j] and (s[i-1]==pattern[j-2] or pattern[j-2]==".")
        return dp[m][n]
