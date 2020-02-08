# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        # write code here
        if not ss:
            return []
        s=list(ss)
        s.sort()
        l=len(s)
        strlist=[ss]
        while True:
            for i in range(l-2,-1,-1):
                if s[i]<s[i+1]:
                    break
            for j in range(l-1,-1,-1):
                if s[j]>s[i]:
                    break
            if i==0 and j==0:
                break
            s[i],s[j]=s[j],s[i]
            s[i+1:]=reversed(s[i+1:])
            strlist.append(''.join(s))
        return strlist








# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        # write code here
        if not ss:
            return []
        s=list(ss)
        s.sort()
        end=len(s)
        res=[ss]
        res.append(self.permu(s,0,end))
        return res
    
    def permu(self,s,position,end):
        if position==end:
            return '',join(s)
        else:
            for i in range(position,end):
                if i == position or s[i]!=s[position]:
                    s[i],s[position]=s[position],s[i]
                    self.permu(s,position+1,end)
                    s[i],s[position]=s[position],s[i]
