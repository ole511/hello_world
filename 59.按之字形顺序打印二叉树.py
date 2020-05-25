# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Print(self, pRoot):
        # write code here
        if not pRoot: return []
        res=[]
        st=[pRoot]
        left = True
        while st:
            res_line=[]
            st2=[]
            for i in st:
                if left: res_line.append(i.val)
                else: res_line.insert(0,i.val)
                if i.left: st2.append(i.left)
                if i.right: st2.append(i.right)
            res.append(res_line)
            st = st2
            left = not left
        return res
