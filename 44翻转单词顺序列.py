# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        if not s: return ""
        if s.isspace():return s
        temp=s.split()
        for i in range(len(temp)//2):
            temp[i],temp[-i-1]=temp[-i-1],temp[i]
        return ' '.join(temp)
    



