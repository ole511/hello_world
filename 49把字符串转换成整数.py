#leetcode题目描述：假设环境中只能储存32位的有符号整数
#此题在剑指offer中的题目描述不到位，要看leetcode的题目描述

'''
其实这个假设对于 Python 不成立。
首先，Python 不存在 32 位的 int 类型。
其次，即使搜索到的字符串转32位整数可能导致溢出，我们也可以直接通过字符串判断是否存在溢出的情况
     （比如 try 函数 或 判断字符串长度 + 字符串比较）
'''

# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        # write code here
        if not s:return 0
        try: 
            if int(s)> 2**31-1 or int(s)< -2**31 :return 0
            return int(s)
        except:
            return 0
            
            
            
# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        # write code here
        s=s.strip()   #删除空格
        if not s :return 0
        numlist=[str(i) for i in range(10)]
        if s[0] not in numlist and s[0] not in ('+','-'):
            return 0
        sign=1    #正负数标志
        if s[0]=='+':s=s[1:]
        elif s[0]=='-':
            sign=-1
            s=s[1:]
        sum=0
        for i in s:
            if i not in numlist:
                return 0
            sum=sum*10+numlist.index(i)
        if sign>0 and sum>(1<<31)-1:return 0   #防止正数溢出  32位有符号整数中最大正数: (1<<31)-1 = 0x7fffffff = 2147483647
        if sign<0 and sum>(1<<31):return 0     #防止负数溢出                 最小负数：(1<<31) = 0x80000000 = -2147483648
        return sum*sign
        
        
        
        
        
# -*- coding:utf-8 -*-  正则表达式  最简洁、功能强大
#可以找出字符串中的数字以及其正负号。但是现在不能实现当字符串中也有字母时，该数字无效，结果返回0的情况。 想要实现这一功能，有待学习...
import re
class Solution:
    def StrToInt(self, s):
        # write code here
        s=s.lstrip()
        if not s:return 0
        return max(min(int(*re.findall('^[\+\-]?\d+',s)), (1<<31)-1), -(1<<31))
    
