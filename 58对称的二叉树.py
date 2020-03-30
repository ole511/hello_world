# -*- coding:utf-8 -*- 递归法
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        if not pRoot:
            return True
        return self.compare(pRoot.left,pRoot.right)
    
    def compare(self,root1,root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.val == root2.val:
            return self.compare(root1.left,root2.right) and self.compare(root1.right,root2.left)
        return False
        
        

# -*- coding:utf-8 -*- 非递归
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        if not pRoot:
            return True
        stack = [pRoot.left,pRoot.right]
        while stack:
            right=stack.pop()
            left=stack.pop()
            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            stack.append(left.left)
            stack.append(right.right)
            stack.append(left.right)
            stack.append(right.left)
        return True
        
