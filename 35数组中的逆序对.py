# -*- coding:utf-8 -*- 归并排序，在merge中计算逆序对
class Solution:
    def __init__(self):
        self.cnt=0  #在子类中直接访问超类的变量
    def InversePairs(self, data):
        # write code here
        if len(data)<2: return 0
        self.mergeSort(data)
        return self.cnt % 1000000007
        
    def mergeSort(self,data):
        if len(data)<2:
            return data
        mid=len(data)//2
        left=self.mergeSort(data[:mid])  #两个递归是写在前面的，
        right=self.mergeSort(data[mid:])
        i,j=0,0
        merged=[]
        while i<len(left) and j<len(right):
            if left[i]>right[j]:
                self.cnt += (len(left)-i)  
                #当left中当前值>right中当前值，由于left和right是分别有序的，那么left[i:]都大于right[j]。所以cnt+(len(left)i)
                merged.append(right[j])
                j+=1
            else: 
                merged.append(left[i])
                i+=1
        return merged + left[i:] + right[j:]
