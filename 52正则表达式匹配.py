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
            
            
            
            
'''
  动态规划问题：最优子结构：通过子问题的最优解，推导出问题的最优解。
  这里虽然不是求问题的最优解，但是可以通过求子问题的答案推导出整个问题的答案。即，通过判断s[i:]与pattern[j:]是否匹配，求解得到s与pattern是否匹配。
  
  假设：s=“abc”   pattern="a.*c*"
1. 首先建立一个dp表：s作为纵轴，i为s的索引；pattern为横轴，j为pattern的索引。
  dp表的行数为len(s)+1，列数为len(pattern)+1。因为需要保存当s为空、pattern为空时匹配的结果，并且要保存在最后（右下角），
  这样i、j就可以正常的表示在s、pattern  字符串中的索引，并与dp表正好对应。
  （也有一种方法是将【s为空、pattern为空】的结果保存在表格的左上方，但是这样的话i、j索引看起来比较乱，不易于理解。）
  
  dp[i][j]表示s[i:]与pattern[j:]是否匹配。
  
2. 初始化将dp[-1][-1]置为True。dp[-1][-1]表示当s为空、pattern为空时的结果。
                        pattern
          ————————————————————————————————————————————
       |  [[False, False, False, False, False, False], 
    S  |   [False, False, False, False, False, False], 
       |   [False, False, False, False, False, False], 
       |   [False, False, False, False, False, True]]
       
3. 构建二重循环，
  第一重：先将i置为s[len(s)+1],再从右往左依次后退。即i依次指向：空 c b a
  第二重：先将j置为pattern的最后一个字母，再从右往左后退。即j依次指向：* c * . a
          先将i指向空的原因是要先对最后一行初始化。
          动态来看，i在表格中从下往上、j在表格中从右往左的过程中，需要利用其下方、右方、右下方的答案，这也是本题使用动态规划方法的核心。
  在遇到‘*’的时候还要具体考虑。
  
   最终的dp表：
                         pattern
          ————————————————————————————————————————————
         |  [[True, True, False, False, False, False], 
   S     |   [False, True, False, False, False, False], 
         |   [False, True, False, True, False, False], 
         |   [False, True, False, True, False, True]]
         
          
'''
# -*- coding:utf-8 -*- 动态规划——自底向上
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here
        dp = [[False] * (len(pattern) + 1) for _ in range(len(s) + 1)]
        dp[-1][-1] = True
        for i in range(len(s), -1, -1):
            for j in range(len(pattern) - 1, -1, -1):
                first_match = i < len(s) and pattern[j] in {s[i], '.'}
                if j+1 < len(pattern) and pattern[j+1] == '*':
                    dp[i][j] = dp[i][j+2] or first_match and dp[i+1][j]
                else:
                    dp[i][j] = first_match and dp[i+1][j+1]
        return dp[0][0]
