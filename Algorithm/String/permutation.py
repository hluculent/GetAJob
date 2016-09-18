# -*- coding:utf-8 -*-
"""
字符串的排列
输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,则打印出由字符a,b,c所能
排列出来的所有字符串abc,acb,bac,bca,cab和cba。 结果请按字母顺序输出。
"""
# -*- coding:utf-8 -*-
class Solution():
	def Permutation(self, ss):
		if ss=='' or len(ss)==1:
			return list(ss)
		ans = []
		tmp = ''
		Solution.subPermutation(self,ss,tmp,ans)
		ans.sort()
		return ans
	def subPermutation(self,string, tmp, ans):
		if string=='' and tmp!='':
			if tmp not in ans:
				ans.append(tmp)
			return
		for i in range(len(string)):
			Solution.subPermutation(self,string[:i]+string[i+1:],tmp+string[i],ans)
quiz = Solution()
print quiz.Permutation(ss='bac')
