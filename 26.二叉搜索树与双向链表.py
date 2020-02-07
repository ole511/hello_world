# -*- coding:utf-8 -*- 递归·中序遍历
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        if not pRootOfTree:
            return None
        if not pRootOfTree.left and not pRootOfTree.right:
            return pRootOfTree
        # 递归处理左子树
        self.Convert(pRootOfTree.left)
        left = pRootOfTree.left
        # 将根节点左指针指向左子树最右孩子，左子树最右孩子的右指针指向根节点
        if left:
            while left.right:
                left = left.right
            pRootOfTree.left, left.right = left, pRootOfTree
        # 递归处理右子树
        self.Convert(pRootOfTree.right)
        right = pRootOfTree.right
        # 将根节点右指针指向右子树最左孩子，右子树最左孩子的左指针指向根节点
        if right:
            while right.left:
                right = right.left
            pRootOfTree.right, right.left = right, pRootOfTree
        while pRootOfTree.left:
            pRootOfTree = pRootOfTree.left
        return pRootOfTree



# -*- coding:utf-8 -*- 非递归·中序遍历
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        if not pRootOfTree:
            return
        stack=[]
        root=pRootOfTree
        pre=None
        while stack or pRootOfTree:   #中序遍历·递归到非递归的转换，套模板
            if pRootOfTree:
                stack.append(pRootOfTree)
                pRootOfTree=pRootOfTree.left
            else:
                cur=stack.pop()
                if pre:           # 递归要实现的内容
                    pre.right=cur # 递归要实现的内容
                    cur.left=pre  # 递归要实现的内容
                pre=cur           # 递归要实现的内容
                pRootOfTree = cur.right  #中序遍历·递归到非递归的转换，套模板
            while root.left:
                root=root.left
        return root
