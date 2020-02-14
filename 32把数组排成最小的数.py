# -*- coding:utf-8 -*- 字符串拼接法
class Solution:
'''
比较两个字符串s1, s2大小的时候，先将它们拼接起来。
比较s1+s2和s2+s1哪个大，如果s1+s2大，那说明s2应该放前面
'''
    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers:
            return ''
        length=len(numbers)
        str_num=[str(i) for i in numbers]
        for i in range(length-1):
            for j in range(length-i-1):
                if int(str_num[j]+str_num[j+1]) > int(str_num[j+1]+str_num[j]):
                    str_num[j],str_num[j+1]=str_num[j+1],str_num[j]
        num = ''.join(i for i in str_num)
        return int(num)
        
        

# -*- coding:utf-8 -*-  lambda写法  上面解法的简洁版
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers: return ''
        numbers = list(map(str,numbers))
        numbers.sort(cmp=lambda x,y:cmp(x+y,y+x))
        return int(''.join(numbers))
