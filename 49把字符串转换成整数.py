'''
leetcode题目描述：假设环境中只能储存32位的有符号整数  (此题在剑指offer中的题目描述不到位，要看leetcode的题目描述)

其实这个假设对于 Python 不成立。
首先，Python 不存在 32 位的 int 类型。
其次，即使搜索到的字符串转32位整数可能导致溢出，我们也可以直接通过字符串判断是否存在溢出的情况
     （比如 try 函数 或 判断字符串长度 + 字符串比较）
'''
               
            
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
         
        
------------------------------------------------------------------------------
        
# -*- coding:utf-8 -*-  正则表达式  最简洁、功能强大
'''
     ^：匹配字符串开头
     [\+\-]：代表一个+字符或-字符
     ?：匹配0个或1个由前面的正则表达式定义的片段，非贪婪方式
     \d：一个数字
     +：匹配前面一个字符的一个或多个
     \b:匹配一个单词边界，也就是指单词和空格间的位置。例如， 'er\b' 可以匹配"never" 中的 'er'，但不能匹配 "verb" 中的 'er'。
'''
import re   #首先要引入函数库
class Solution:
    def StrToInt(self, s):
        # write code here
        return max(min(int(*re.findall('^[\+\-]?\d+',s.lstrip())), (1<<31)-1), -(1<<31))   
        #可以找出字符串中的数字以及其正负号。但是现在不能实现当字符串中也有字母时，该数字无效，结果返回0的情况。
        #满足leetcode的题意，不满足剑指offer的
     
     
# -*- coding:utf-8 -*- 优化版本  在正则表达式中添加了'/b'以限制边界,在这里要写\\b，因为不是(r'正则表达式')
import re
class Solution:
    def StrToInt(self, s):
        # write code here
        s=s.lstrip()
        pattern=re.compile(r'[+-]?\d+\b')
        m=pattern.match(s)
        #上面使用的是findall方法，在字符串中找到所匹配的所有子串，并返回一个列表，还要通过*解压。
        #这里用的是match方法：尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。
        if not m : return 0
        m=int(m.group())  # group返回匹配成功的整个子串
        if m>(1<<31)-1 or m<-(1<<31):return 0  #判断溢出情况
        return m
     
---------------------------------------------------------------------------------     
     
# -*- coding:utf-8 -*-  用了int()的做法，不符合题意
class Solution:
    def StrToInt(self, s):
        # write code here
        if not s:return 0
        try: 
            if int(s)> 2**31-1 or int(s)< -2**31 :return 0
            return int(s)
        except:
            return 0
   
