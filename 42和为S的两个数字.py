# -*- coding:utf-8 -*- 双指针法
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        if len(array)<2 or tsum<1:return[]
        i,j=0,len(array)-1
        while i<j:
            if array[i]+array[j]==tsum:
                return [array[i],array[j]]
            elif array[i]+array[j]>=tsum: j-=1
            else :i+=1
        return []

    

# -*- coding:utf-8 -*- 只需要输出最外层的一对数字即可
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        if  len(array)<2 or tsum<1:return []
        for i in array:
            if tsum-i in array and tsum-i>i:
                return [i,(tsum-i)]
        return []
    
    
