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


# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        # write code here
        if not ss:
            return []
        s=list(ss)
        s.sort()
        res=[]
        l=len(s)
        visited=[False]*l
        res_str=[]
        def dfs(s,res,res_str,visited):
            if len(res_str)==l:
                res.append(''.join(res_str))
                return
            for i in range(l):
                if visited[i]:
                    continue
                if i!=0 and not visited[i-1] and s[i]==s[i-1]:
                    continue
                visited[i]=True
                res_str.append[i]
                dfs(s,res,res_str,visited)
                res_str.pop()
                visited[i]=False
        return res
