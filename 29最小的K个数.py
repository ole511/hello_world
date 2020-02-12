'''
输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4
'''

# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if not tinput:
            return []
        tinput.sort()
        if k>len(tinput):
            return []
        return tinput[:k]
        

        
        
# -*- coding:utf-8 -*- 快速排序法
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if not tinput or k>len(tinput) or k==0:
            return []
        
        def quicksort(left,right):    #这里调用一次函数只将tinput[left]放置到正确位置，其左右数字仍然是乱序
            if left>=right:    #如果左右索引为同一个，直接返回当前数字的索引
                return left
            i,j=left,right
            flag=tinput[left]  #哨兵
            while i!=j:
                while j>i and tinput[j]>flag:   #注意：如果是将left记为哨兵，那么就一定要从右边的j 开始启动
                    j-=1                        #  j往左移动，直到找到第一个小于flag的数字
                while j>i and tinput[i]<=flag:  #注意这里有=号，是为了让i跳过flag
                    i+=1                        #  i往右移动，直到找到第一个大于flag的数字
                if i<j:      #注意各种判断条件
                    tinput[i],tinput[j]=tinput[j],tinput[i]  #将比哨兵大的数字换到右边，比哨兵小的数字换到左边
            tinput[left],tinput[j]=tinput[j],tinput[left]    #当i=j时，将flag与tinput[i]互换，这里tinput[j]一定是小于flag的
            return j     #将j的值返回，为了和K作比较
        
        left,right=0,len(tinput)-1   #初始化
        while left<right:            #如果left=right，说明只有一个数字
            j=quicksort(left,right)  #找到第一个数字被换到的位置，与K比较
            if j==k-1:               #j是第K个数字，将前K个数字进行排序即可。leetcode上的题目无需排序，直接return即可
                break
            elif j<k-1:
                left=j+1
            else: right=j-1
        res=tinput[:k]
        res.sort()
        return res
    
    
