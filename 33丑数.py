# -*- coding:utf-8 -*- 来自超超的简单解法
'''
设置p2,p3,p5三个指针分别指向待乘的数i,j,q，找出i*2,j*3,q*5中最小的数，作为新加入数组的数字
如果i*2最小，那么i++
'''
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index<=0: return 0
        dp=[1]
        p2,p3,p5=0,0,0
        for i in range(1,index):
            temp=min(dp[p2]*2,dp[p3]*3,dp[p5]*5)
            dp.append(temp)
            if temp==dp[p2]*2:p2+=1
            if temp==dp[p3]*3:p3+=1
            if temp==dp[p5]*5:p5+=1
        return dp[index-1]
