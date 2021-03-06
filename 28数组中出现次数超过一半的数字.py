# -*- coding:utf-8 -*- 排序+取中值（中位数是唯一有可能的值，再进行判断）
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if not numbers:
            return 0
        numbers.sort()
        mid=len(numbers)/2
        if numbers[numbers.index(numbers[mid-1])+mid] == numbers[mid-1]:
            return numbers[mid]
        else:
            return 0
            
            
# -*- coding:utf-8 -*- 字典
'''
每遇到一个新的数字就记录它出现过的次数。
'''
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if not numbers:
            return 0
        half=len(numbers)/2+1
        count={}
        for i in numbers:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
            if count[i]==half:
                return i
        return 0
        
        
# -*- coding:utf-8 -*- count--法
'''
初始设置值为number[0]为val,count=1，当为不同数字时count--，同一个数字时++。
当count=0时，换一个数字。最后留下来的数字为最终选手，判断它的次数是否超过数组的一半。
'''
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if not numbers:
            return 0
        count=0
        val=0
        for i in numbers:
            if count==0:
                val=i
            if val==i:
                count+=1
            elif val!=i:
                count-=1
        count=0
        if numbers.count(val)>len(numbers)/2:
            return val
        else: return 0
