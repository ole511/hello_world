# -*- coding:utf-8 -*-巧妙的左右遍历乘积法
'''
  从左往右遍历一次，在B数组中记录当前数字的左边的累积（不包括当前数字）。
  从右往左遍历一次，在B数组已有数字的基础上，乘以该数字右边的累乘的积。
  用left_product、right_product分别记录左边、右边累乘的积。这样就可以正好跳过当前数字啦~
  时间复杂度O(n) 空间复杂度O(1)
'''
class Solution:
    def multiply(self, A):
        # write code here
        b=[0]*len(A)
        left_product=1   #初始为1嗷
        right_product=1
        for i in range(len(A)):
            b[i]=left_product
            left_product*=A[i]
        for i in range(len(A)-1,-1,-1):
            b[i]*=right_product
            right_product*=A[i]
        return b
