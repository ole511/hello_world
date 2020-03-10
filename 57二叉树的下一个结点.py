'''
  给定一个二叉树其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
  注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
'''

# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def GetNext(self, pNode):
        # write code here
        if not pNode:return
        # 先找是否存在右子树，存在的话找右子树的最左结点
        # 注意这里有一个概念不要搞错，如果结点没有左子树，那么先遍历到的是根（该结点）而不是该结点的右子树的最左结点！！
        if pNode.right:
            pNode=pNode.right
            while pNode.left:
                pNode=pNode.left
            return pNode
        # 没有右子树，并且该结点是父结点的左子树，直接返回父结点
        if pNode.next and pNode==pNode.next.left:
            return pNode.next
        # 没有右子树，并且该结点是父节点的右子树，一直向上推，直到找到不是父节点的右节点的结点。返回该结点的父节点，画图理解。
        if pNode.next:
            while pNode.next and pNode==pNode.next.right:
                pNode=pNode.next
            return pNode.next
        return 
