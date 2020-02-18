# -*- coding:utf-8 -*-  长链表先走到两个链表剩余结点数相同
'''
让其中一个长的链表 先走过两个链表长度之差的绝对值步数，
然后再用两个指针同时走，直到找到第一个相同的节点。
因为两个链表的第一个相同节点的后面都是一样的。
'''
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        if not pHead1 or not pHead2: return 
        len1,len2=0,0
        p1,p2=pHead1,pHead2
        # 计算两个链表的长度
        while p1:
            len1+=1
            p1=p1.next
        while p2:
            len2+=1
            p2=p2.next
        # 计算长度之差，让长链表先走几步
        p1,p2=pHead1,pHead2
        if (len1<len2):
            k=len2-len1
            while k>0:
                p2=p2.next
                k-=1
        else:
            k=len1-len2
            while k>0:
                p1=p1.next
                k-=1
        #一起走，判断是否相同
        while p1 is not p2:
          #这里如果改成：
          # while p1:
          #   if p1!=p2:
          # 会超过指定运算时间
            p1=p1.next
            p2=p2.next
        return p1
        
        
        
        
        
# -*- coding:utf-8 -*- 一个链表走完后走另一个链表
'''
  p1先走pHead1链表，再走pHead2
  p2先走pHead2链表，再走pHead1
  如此两个拼接后的链表长度相同，如果有公共部分，那么最后的部分相同
'''
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        if not pHead1 or not pHead2:return
        p1,p2=pHead1,pHead2
        while p1 is not p2:
            p1=p1.next
            p2=p2.next
            if p1 is not p2:
                if p1==None:p1=pHead2
                if p2==None:p2=pHead1
        return p1
