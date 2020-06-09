# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        if not pRoot or k==0: return
        stack=[]
        count=0
        node = pRoot
        while node or len(stack)>0:
            if node:
                stack.append(node)
                node = node.left
            else: 
                node = stack.pop()
                count+=1
                if count==k:
                    return node
                node = node.right
        return None
