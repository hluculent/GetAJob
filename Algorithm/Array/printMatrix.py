# -*- coding:utf-8 -*-
"""
顺时针打印矩阵
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，例如，如果输入如下矩阵：
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
"""
class Solution:
	# matrix类型为二维列表，需要返回列表
	def printMatrix(self, matrix):
		# 四个指标 left right up down
		up, down = 0, len(matrix)
		left, right = 0, len(matrix[0])
		result = []
		# 循环一次走四边，循环终止的条件是result里面塞满元素
		while len(result) < len(matrix)*len(matrix[0]):
			result.extend(matrix[up][left:right])
			up += 1
			#result.extend(matrix[up:down][right]) # python 好像不支持这种矩阵表示方法
			result.extend([matrix[row][right-1] for row in range(up, down)])
			right -= 1
			if up != down:
				result.extend(matrix[down-1][col] for col in range(right-1, left-1,-1))
				down -= 1
			if right != left:
				result.extend(matrix[row][left] for row in range(down-1, up-1,-1))
				left += 1
		return result