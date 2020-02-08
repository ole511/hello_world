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


