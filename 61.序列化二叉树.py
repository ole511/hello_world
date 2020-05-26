# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Serialize(self, root):
        # write code here
        def dfs(node):
            if node:
                vals.append(node.val)
                dfs(node.left)
                dfs(node.right)
            else: vals.append('#')
        vals=[]
        dfs(root)
        return ','.join(str(i) for i in vals)
    def Deserialize(self, s):
        # write code here
        def dfs():
            v=next(vals)
            if v=='#':
                return None
            node = TreeNode(int(v))
            node.left = dfs()
            node.right = dfs()
            return node
        
        vals = iter(s.split(','))
        return dfs()
