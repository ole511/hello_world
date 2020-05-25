# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if not pRoot:return []
        res=[]
        st=[pRoot]
        while st:
            st2=[]
            t=[]
            for i in st:
                t.append(i.val)
                if i.left:
                    st2.append(i.left)
                if i.right:
                    st2.append(i.right)
            res.append(t)
            st=st2
        return res




# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if not pRoot: return []
        res=[]
        st=[pRoot]
        while st:
            num=len(st)
            res2=[]
            for i in range(num):
                res2.append(st[0].val)
                if st[0].left:
                    st.append(st[0].left)
                if st[0].right:
                    st.append(st[0].right)
                del st[0]
            res.append(res2)
        return res
