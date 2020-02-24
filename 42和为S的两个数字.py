# -*- coding:utf-8 -*-  不知道为什么错了，vscode上可以正常运行
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        if len(array)<2 or tsum<1:return
        i,j=0,len(array)-1
        min_product=array[-1]*array[-1]
        while i<j:
            if array[i]+array[j]==tsum:
                min_product=min(min_product,array[i]*array[j])
                i+=1
                j-=1
            elif array[i]+array[j]>tsum:
                j-=1
            else: i+=1
        return min_product    #因为要输出数组而不是乘积，大傻子！
'''
用例:   [1,2,4,7,11,15],15
对应输出应该为:
[4,11]
你的输出为:
[object of type 'int' has no len()
'''



# -*- coding:utf-8 -*- 只需要输出最外层的一对数字即可
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        if  len(array)<2 or tsum<1:return []
        for i in array:
            if tsum-i in array and tsum-i>i:
                return [i,(tsum-i)]
        return []
