# -*- coding:utf-8 -*- 两个队列实现分层存储
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root:
            return []
        curlist=[root]  #储存当前一层
        res=[]
        while curlist:
            nextlist=[]   #储存下一层
            for i in curlist:
                if i.left:
                    nextlist.append(i.left)
                if i.right:
                    nextlist.append(i.right)
                res.append(i.val)
            curlist=nextlist
        return res
        #25ms
        
        

# -*- coding:utf-8 -*- 一个队列即可实现
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root:
            return []
        curlist=[root]
        res=[]
        while curlist:
            node = curlist.pop(0)  #每次处理队列第0个
            if node.left:
                curlist.append(node.left)
            if node.right:
                curlist.append(node.right)
            res.append(node.val)
        return res
        #29ms
