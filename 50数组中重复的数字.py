'''
  1. 排序算法：时间O(nlogn) 空间O(1)
  2. 哈希表：时间O(n)  空间O(n)
  3. 本方法：时间O(n) 空间O(1)
'''

# -*- coding:utf-8 -*- 试图将每个数字归位，归为的过程中找到第一个重复的数字。
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        if not numbers:return False
        i=0
        while i < len(numbers):
            if i==numbers[i]:i+=1    #如果数组中索引为i的数字正好也是i,那么这个位置上的第一个数字已经归位，换下一个。
            else :
                if numbers[i]==numbers[numbers[i]]:    #在交换之前先判断，当前数字与要交换的数字是否重复，是的话就找到了，记下并返回即可
                    duplication[0]=numbers[i]
                    return True
                else: 
                    temp=numbers[i]       #如果当前数字与要交换的位置上的数字不相同，把当前数字归位。
                    numbers[i]=numbers[numbers[i]]
                    numbers[temp]=temp
        return False
