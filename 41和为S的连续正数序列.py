# -*- coding:utf-8 -*- 双指针法
'''
  i和j分别指向答案序列的头和尾，判断i到j的和是否为tsum。
  i从1到tsum+1//2，j从2开始，但是不用回退，j++即可。因为在i增加的过程中，j也是单调增加的。
'''
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        if tsum<3: return []
        j,sum=2,3
        res=[]    #注意这里可以是res=[],而不是res=[[]]。否则答案会出现：[[],[7,8]]  (第一个序列为空)
        for i in range(1,tsum+1//2):
            while sum<tsum:
                j+=1
                sum+=j
            line=[]
            if sum==tsum and j-i>0:
                for k in range(i,j+1):
                    line.append(k)
                res.append(line)
            sum-=i
        return res
        
        
        
        
        
# -*- coding:utf-8 -*-  以商为中心找答案
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        if tsum<3: return []
        k=tsum+1//2   #k作为除数，递减
        res=[]
        while k>=2:
            line=[]
            div,mod=divmod(tsum,k)
            if k%2==0:    #除数为偶数时
                if mod+mod==k and (div+1-mod)>0:   #当商为xx.5，并且答案序列都为正数时
                    for i in range(div-mod+1,div+mod+1):   #答案序列为以xx.5为中位数的对称数组
                        line.append(i)
                    res.append(line)
            else:   #除数为奇数时
                if mod==0 and (div-k//2)>0:   #tsum能被整除，并且列答案序列都为正数时
                    for i in range(div-k//2,div+k//2+1):   #答案序列为以商为中位数的对称数组
                        line.append(i)
                    res.append(line)
            k-=1
        return res
        
        
        
        
        
        
