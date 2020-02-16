# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if not s: return -1
        dic={}
        for i in s:
            dic.setdefault(i,0)
            dic[i]+=1
        for i in s:
            if dic[i]==1:
                return s.index(i)
        return -1







# -*- coding:utf-8 -*- 创建ASCII码作为索引的数组
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if not s: return -1
        ls=[0]*256
        for i in s:
            ls[ord(i)]+=1
        for i in s:
            if ls[ord(i)]==1:
                return s.index(i)
        return -1
