# -*- coding:utf-8 -*- 先序递归
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if not pRoot: return 0
        left=self.TreeDepth(pRoot.left)
        right=self.TreeDepth(pRoot.right)
        return max(left,right)+1
        
        
        
        
# -*- coding:utf-8 -*- 层次遍历
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if not pRoot:return 0
        ls=[pRoot]
        cnt=0
        while ls:
            cnt+=1
            length=len(ls)  #记录同层节点个数
            for i in range(length):
                a=ls.pop(0)
                if a.left: ls.append(a.left)
                if a.right: ls.append(a.right)
        return cnt
