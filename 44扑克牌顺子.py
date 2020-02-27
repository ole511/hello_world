# -*- coding:utf-8 -*- 比较聪明的做法
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if not numbers: return False
        king_cnt=0
        max,min=-1,14
        for i in numbers:   #找到大小王的个数，以及除零外的最大数、最小数
            if i>max:max=i
            if i<min and i!=0:min=i
            elif i==0:king_cnt+=1
        if king_cnt>0 and len(set(numbers))+king_cnt-1!=5:return False  #如果有除零外的对子，out
        if max-min>=5:return False  #如果除零外的最大最小数之差小于5，即可认为是顺子
        return True
        
        
        
        
# -*- coding:utf-8 -*- 简洁版  方法是一样的
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if len(numbers):
            while min(numbers)==0:
                numbers.remove(0)
            if len(numbers)==len(set(numbers)) and max(numbers)-min(numbers)<=4:
                return True
        return False
