# -*- coding:utf-8 -*-先序遍历计算左右子树的深度
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        if not pRoot:return True  #空树也是平衡二叉树
        return self.depth(pRoot)!=-1
        
    def depth(self,pRoot):
        if not pRoot: return 0
        left=self.depth(pRoot.left)
        if left==-1: return -1  #左子树不平衡直接退出
        right=self.depth(pRoot.right)
        if right==-1: return -1
        if abs(left-right)<=1: return max(left,right)+1   #当左右子树的深度之差不超过1，返回子树的深度
        else:return -1
        
        
        
        
        
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def __init__(self):
        self.isbalance=True
    def IsBalanced_Solution(self, pRoot):
        # write code here
        if not pRoot:return True
        self.depth(pRoot)
        return self.isbalance
    
    def depth(self,pRoot):
        if not pRoot : return 0
        left=self.depth(pRoot.left)
        right=self.depth(pRoot.right)
        if abs(left-right)>1: self.isbalance=False
        return max(left,right)+1
        
