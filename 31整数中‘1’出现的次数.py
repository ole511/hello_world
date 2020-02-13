# -*- coding:utf-8 -*- 找规律
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
'''
如果x > 1的话，则第i位数上包含的1的数目为：(高位数字 + 1）* 10 ^ (i-1) (其中高位数字是从i+1位一直到最高位数构成的数字)
如果x < 1的话，则第i位数上包含的1的数目为：(高位数字 ）* 10 ^ (i-1)
如果x == 1的话，则第i位数上包含1的数目为：(高位数字) * 10 ^ (i-1) +(低位数字+1) (其中低位数字时从第i - 1位数一直到第1位数构成的数字)
'''
        # write code here
        a,sum=1,0
        while n//a:
            div,mod=divmod(n,a*10)
            curNum,curMod=divmod(mod,a)
            if curNum>1:  
                sum=sum+div*a+a
            elif curNum==1:
                sum=sum+div*a+curMod+1
            else:sum=sum+div*a
            a=a*10
        return sum




# -*- coding:utf-8 -*- 上面解法的精简版
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        if n==0: return 0
        if n<=9: return 1
        a,cnt=1,0
        while a<=n:
            div,mod=divmod(n,a)
            cnt+=(div+8)//10*a+(div%10==1)*(mod+1)  #关键理解+8的作用！！
            a=a*10
        return cnt
        
        
        
# -*- coding:utf-8 -*-暴力解法，耗时很长很长
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        cnt=0
        for i in range(n+1):
            cnt += self.haveOne(i)
        return cnt
    def haveOne(self,i):
        cnt,div=0,i
        while div:
            div,mod=divmod(div,10)
            cnt+=(mod==1)
        return cnt
