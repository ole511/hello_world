'''
题目： 实现一个函数用来匹配包括'.'和'*'的正则表达式。
模式中的字符'.'表示任意一个字符（不包括空字符！），而'*'表示它前面的字符可以出现任意次（包含0次）。 
在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配
'''

'''
首先，考虑特殊情况：         
1>当s和pattern都为空时，返回true         
2>当s非空，而pattern空了，返回false
3>当s空了,pattern非空，还是可能匹配成功的。比如 s="acd" pattern="..*d*"
  这里主要判断patternd的[0]、[1]的是否为“x*”，不是的话就返回False，是的话就继续判断
之后就开始匹配第一个字符，这里有两种可能：匹配成功或匹配失败。
    难点是要考虑pattern下一个字符可能是‘*’的情况。
    【当pattern中的第二个字符是“*”时】
      如果s第一个字符跟pattern第一个字符不匹配，则pattern后移2个字符，继续匹配。
      如果s第一个字符跟pattern第一个字符匹配，可以有2种匹配方式：
        1) s后移1字符，pattern后移2字符，相当于x*匹配一位；
        2) s后移1字符，pattern不变，即继续匹配字符下一位，相当于x*匹配多位；

    【当pattern中的第二个字符不是“*”时】
    如果s第一个字符和pattern中的第一个字符相匹配（s[0]==pattern[0]或者pattern[0]=='.'），那么s和pattern都后移一个字符，然后匹配剩余的部分。
    如果s第一个字符和pattern中的第一个字符不匹配，直接返回False。

'''

# -*- coding:utf-8 -*- 递归方式
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here
        if not s and not pattern: return True
        if s and not pattern: return False
        if not s and pattern:
            if len(pattern)>=2 and pattern[1]=='*':
                return self.match(s,pattern[2:])
            else: return False
        if len(pattern)>=2 and pattern[1]=='*':
            if s[0]==pattern[0] or pattern[0]=='.': 
                return self.match(s[1:],pattern) or self.match(s,pattern[2:])
            else : return self.match(s,pattern[2:])
        else:
            if s[0]==pattern[0] or pattern[0]=='.' :return self.match(s[1:],pattern[1:])
            else: return False
            
            
            
            
            
