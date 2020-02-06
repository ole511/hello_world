# -*- coding:utf-8 -*- 递归法
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if not pHead:return
        newnode=RandomListNode(pHead.label)
        newnode.random=pHead.random
        newnode.next=self.Clone(pHead.next)
        return newnode
        
        
# -*- coding:utf-8 -*- 哈希表：字典法
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        node_map = {}
        def loop(node):
            if not node:
                return None
            if not node_map.get(node):
                node_map[node] = RandomListNode(node.label)
            clone_node = node_map[node]
            if node.random:
                if not node_map.get(node.random):
                    node_map[node.random] = RandomListNode(node.random.label)
                clone_node.random = node_map[node.random]
            else:
                clone_node.random = None
            clone_node.next = loop(node.next)
            return clone_node
        return loop(pHead)
        

# -*- coding:utf-8 -*- 哈希表：多层序列代替字典
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        nodeList = []  # 存放各个节点
        randomList = []  # 存放各个节点指向的random节点。没有则为None
        labelList = []  # 存放各个节点的值
        #遍历整个链表
        while pHead:
            randomList.append(pHead.random)
            nodeList.append(pHead)
            labelList.append(pHead.label)
            pHead = pHead.next
        # random节点的索引，如果没有则为-1，返回的是节点的random指针指向的链表的位置
        #node节点对应的random节点的位置
        labelIndexList = map(lambda c: nodeList.index(c) if c else -1, randomList)
        #此处设定的是空的头节点
        dummy = RandomListNode(0)
        pre = dummy
        # 节点列表，只要把这些节点的random设置好，顺序串起来就ok了。
        #很简单的一个创建新链表的过程
        nodeList = map(lambda c: RandomListNode(c), labelList)
        # 把每个节点的random绑定好，根据对应的index来绑定
        for i in range(len(nodeList)):
            if labelIndexList[i] != -1:
                nodeList[i].random = nodeList[labelIndexList[i]]
        for i in nodeList:
            pre.next = i
            pre = pre.next
        #既改变了dummy所引导的链表，但是又没有改变链表头
        return dummy.next


        
        
# -*- coding:utf-8 -*- 剑指offer上的思想 兄弟节点插入&拖链法
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if not pHead:
            return None
        #step1 复制原链表节点，并插入其后
        tmp = pHead
        while tmp:
            clone = RandomListNode(tmp.label)
            clone.next = tmp.next
            tmp.next = clone
            tmp = clone.next
             
        #step2复制random指针
        tmp = pHead
        while tmp:
            clone = tmp.next
            clone.random = tmp.random.next if tmp.random else None
            tmp = clone.next
            
        #step3: 脱链
        #如果pHead只有一个节点,复制之后必有两个节点,因此不用担心pHead.next会为空
        clone = pHead.next
        cloneHead = clone
        while pHead:
            #还原原始链表节点.next
            pHead.next = clone.next
            #判断clone是否处于尾节点
            if pHead.next:
                clone.next = pHead.next.next
            else:
                clone.next = None
            pHead = pHead.next
            clone = clone.next
        return cloneHead
