# -*- coding:utf-8 -*- 将字符串转换成序列再调整的方法
class Solution:
    def ReverseSentence(self, s):
        # write code here
        if not s: return ""
        if s.isspace():return s
        temp=s.split()
        for i in range(len(temp)//2):
            temp[i],temp[-i-1]=temp[-i-1],temp[i]
        return ' '.join(temp)
    
'''
python不支持对源字符串直接进行修改。例如s[:3]="123"   s="123"+s[3:]都不能通过
所以我就没用先把字符串整体反转，再局部反转的方法。
'''
