# -*- coding:utf-8 -*- 字典序排序法
class Solution:
    def Permutation(self, ss):
        # write code here
        if ss=='':
            return []
        s=list(ss)
        s.sort()
        l=len(s)
        strlist=[ss]
        k,j=0,0  #为什么要初始化才能过？？！
        while True:
            for k in range(l-2,-1,-1):
                if s[k]<s[k+1]:
                    break
            for j in range(l-1,-1,-1):
                if s[j]>s[k]:
                    break
            if k==0 and j==0:
                break
            s[k],s[j]=s[j],s[k]
            s[k+1:]=reversed(s[k+1:])
            strlist.append(''.join(s))
        strlist=sorted(strlist)
        return strlist
    
    
    
    
    # -*- coding:utf-8 -*- python高效递归
class Solution:
    def Permutation(self, ss):
        # write code here
        if not ss:
            return []
        if len(ss)==1:
            return [ss]
        res=[]
        for i in range(len(ss)):
            for j in self.Permutation(ss[:i]+ss[i+1:]):
                res.append(ss[i]+j)
        return sorted(set(res))








# -*- coding:utf-8 -*-  两两交换法
class Solution:
    def Permutation(self, ss):
        # write code here
        if ss=='':
            return []
        s=list(ss)
        s.sort()
        end=len(s)
        res=[]
        self.permu(s,0,end,res)
        # res=list(set(res))  用来删除序列中重复的元素
        res=sorted(res)
        return res
    
    def permu(self,s,position,end,res):
        if position==end:
            res.append(''.join(s))
        else:
            for i in range(position,end):
                if i == position or s[i]!=s[position]:
                    s[i],s[position]=s[position],s[i]
                    self.permu(s,position+1,end,res)
                    s[i],s[position]=s[position],s[i]
