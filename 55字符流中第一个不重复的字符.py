# -*- coding:utf-8 -*-  用了内置函数count
class Solution:
    # 返回对应char
    def __init__(self):
        self.s=""
    def FirstAppearingOnce(self):
        # write code here
        res=filter(lambda c:self.s.count(c)==1,self.s)
        return res[0] if res else '#'
    def Insert(self, char):
        # write code here
        self.s+=char
        
        
        
# -*- coding:utf-8 -*- 字典
class Solution:
    # 返回对应char
    def __init__(self):
        self.s=""
    def FirstAppearingOnce(self):
        # write code here
        dic={}
        -----------------------------
        # 建立字典的不同方法
        for i in self.s:
            if i in dic: dic[i]+=1  #建立有序字典,常规的字典是无序存储的.从开始访问s中的元素,依次加入有序字典中
            else: dic[i]=1
        
        for i in self.s:
            dic[i]=dic.get(i,0)+1  #无序字典,所以字典中字符的顺序不是我们输入时的顺序
        
        for i in self.s:
            dic.setdefault(i,0)
            dic[i]+=1
        -----------------------------
        # 得到键的不同方法
        for i in self.s:
            if dic[i]==1:return i
            
        for key,value in dic.items():  # 只可用于在有序字典中查找
            if value==1: return key
        ------------------------------
        return '#'
    def Insert(self, char):
        # write code here
        self.s+=char
        
        
     
