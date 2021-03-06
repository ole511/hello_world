'''
用inerst函数实现数据加入序列，用GetMedian实现取出数据流的中位数。
本题牛客网的python有误，提示GetMedian() takes exactly 1 argument (2 given)。
需要将def GetMedian(self)写成def GetMedian(self,data)，但实际上data并无作用。

本题有两种解法，都是将数据流拆成前后两段。
一、前半段升序，后半段降序。分别以奇数和偶数两种状态处理新的数字：
    奇数时，将num与前半段的最大值比较。中位数是后半段的最小值。
    偶数时，将num与后半段的最小值比较。中位数是（前半段的最大值+后半段的最小值）/2.0

二、前半段大顶堆，后半段小顶堆。
    但是python没有直接可以调用的大顶堆，要自己写，有点麻烦。

三、利用内置的bisect函数实现二分插入。简单高效。

'''

# -*- coding:utf-8 -*- bisect函数实现二分查找插入num
# 插入时间复杂度O(logn), 获取中位数时间复杂度O(1)
import bisect
class Solution:
    def __init__(self):
        self.data=[]
        self.sum=[]
    def Insert(self, num):
        # write code here
        bisect.insort(self.data,num)
        self.sum+=1
        #index = bisect_left(self.data,num)
        #self.data.insert(index,num)
    def GetMedian(self,o):
        # write code here
        if sum % 2:
            return self.data[sum/2]
        return (self.data[sum/2]+self.data[(sum/2)-1])/2.0

# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.count=0
        self.small=[]
        self.big=[]
    def Insert(self, num):
        # write code here
        self.count+=1
        if self.count%2:
            if self.small:
                if num<self.small[-1]:
                    self.big.append(self.small.pop())
                    self.small.append(num)
                    self.small.sort()
                else:
                    self.big.append(num)
                    self.big.sort(reverse=True)
            else:
                self.big.append(num)
                self.big.sort(reverse=True)
        else:
            if num>self.big[-1]:
                self.small.append(self.big.pop())
                self.big.append(num)
                self.big.sort(reverse=True)
            else:
                self.small.append(num)
                self.small.sort()
    def GetMedian(self,data):
        # write code here
        if self.count%2:
            return self.big[-1]
        return (self.small[-1]+self.big[-1])/2.0
