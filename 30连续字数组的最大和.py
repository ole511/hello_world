# -*- coding:utf-8 -*-动态规划——用两个整数空间：sum和max_line记录状态
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if not array:
            return
        sum=array[0]     #不能是sum=0，因为有可能全是负数
        max_line=array[0]
        for i in array[1:]:  
            if sum<0:sum=0    #很关键，如果之前的和小于0，就都放弃，重新计算新的子序列的和
            sum+=i
            max_line=max(max_line,sum) #动态记录子序列最大的和
        return max_line




# -*- coding:utf-8 -*- 动态规划——用一个dp数组记录状态
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        dp=[array[0]]
        for i in array[1:]:
            if dp[-1]<0: dp.append(i)  #dp[i]为以array[i]为末尾的最大的子数组和
            else: dp.append(dp[-1]+i)
        return max(dp)
