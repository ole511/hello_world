# -*- coding:utf-8 -*- 二分法 查找第一个和最后一个k
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        if not data: return 0
        low,high=0,len(data)-1
        while low<high:   #注意各种边界，这里是< 不是<=
            mid=low+high>>1
            if data[mid]>=k: high=mid
            else: low=mid+1
        if data[low]!=k: return 0
        first=low
            
        low,high=0,len(data)-1
        while low<high:
            mid=low+high+1>>1
            if data[mid]<=k: low=mid
            else: high=mid-1
        if data[low]!=k: return 0
        last=low
        return last-first+1



# -*- coding:utf-8 -*- 二分法 寻找k-0.5和k+0.5的位置，不太方便记忆。记超超说的二分法模板就好
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        if not data:
            return 0
        l=self.getLocation(data,k-0.5)
        h=self.getLocation(data,k+0.5)
        return h-l
        
    def getLocation(self,data,k):
        low,high=0,len(data)-1
        while low<=high:
            mid=low+high>>1
            if data[mid]>k: high=mid-1
            elif data[mid]<k: low=mid+1
        return low
