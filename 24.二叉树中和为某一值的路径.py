# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
二叉树递归实现前序遍历，用一个list保存路径上的值，遇到叶子节点求list里的和
如果和等于期望值，把结果保存下来，最终输出所有结果
注意：list为可变变量，每次保存的时候用切片实现拷贝
'''
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return []
        path=[]
        res=[]
        def find(root):
            #if sum(path) > expectNumber:  有可能是负数所以不能判断大于小于
            #    return 
            path.append(root.val)
            if not root.left and not root.right:
                if sum(path) == expectNumber:
                    res.append(path[:])
                path.pop()

            else:
                if root.left:
                    find(root.left)
                if root.right:
                    find(root.right)
                path.pop()
            
        find(root)
        return res
