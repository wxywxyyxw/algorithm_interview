#!/usr/bin/python
# -*- coding: utf-8 -*-

# 定义基本二叉树
class BinaryTree(object):
    def __init__(self, value):
        self.value = value
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, value):
        """
        插入左子树
        分两种情况
        1: 如果该节点没有左子树，直接插入左子树
        2: 如果该节点有左子树，则将该节点的左子树变为新加入结点的左子树，新加入结点变为该节点的左子树
        """
        if not self.leftChild:
            self.leftChild = BinaryTree(value)
        else:
            newNode = BinaryTree(value)
            newNode.leftChild = self.leftChild
            self.leftChild = newNode

        return self.leftChild

    def insertRight(self, value):
        """
        插入右子树
        分两种情况
        1: 如果该节点没有右子树，直接插入右子树
        2: 如果该节点有右子树，则将该节点的左子树变为新加入结点的右子树，新加入结点变为该节点的右子树
        """
        if not self.rightChild:
            self.rightChild = BinaryTree(value)
        else:
            newNode = BinaryTree(value)
            newNode.rightChild = self.rightChild
            self.rightChild = newNode

        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return self.rightChild

    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value

    def preOrder(self):
        """
        前序遍历: 中左右
        先遍历自己，在遍历左子树，在遍历右子树
        """
        print (self.value)
        if self.leftChild:
            left = self.leftChild
            left.preOrder()
        if self.rightChild:
            right = self.rightChild
            right.preOrder()

    def inOrder(self):
        """
        中序遍历: 左中右
        先遍历左子树，在访问自己，在遍历右子树
        """

        if self.leftChild:
            left = self.leftChild
            left.inOrder()

        print (self.value)

        if self.rightChild:
            right = self.rightChild
            right.inOrder()

    def postOrder(self):
        """
        后序遍历: 左右中
        先遍历左子树，在遍历右子树，在访问自己，
        """

        if self.leftChild:
            left = self.leftChild
            left.postOrder()

        if self.rightChild:
            right = self.rightChild
            right.postOrder()

        print (self.value)

    def pre_order_no_recursion(self):
        """
        非递归前序遍历
        建立一个栈,保存遍历的结点
        """
        node = self
        tree_stack = []
        while node or len(tree_stack) > 0:

            while node:
                print (node.value)
                tree_stack.append(node)
                node = node.leftChild
            if len(tree_stack) > 0:
                node = tree_stack.pop()
                node = node.rightChild

    def in_order_no_recursion(self):
        """
        非递归中序遍历
        建立一个栈,保存遍历的结点,和前序遍历类似，只是输出的位置是在出栈后
        """

        node = self
        tree_stack = []
        while node or len(tree_stack) > 0:

            while node:
                tree_stack.append(node)
                node = node.leftChild
            if len(tree_stack) > 0:
                node = tree_stack.pop()
                print (node.value)
                node = node.rightChild

    def post_order_no_recursion(self):
        """
        非递归后序遍历
        利用一个栈 和 一个flag 来后序遍历
        """
        node = self
        node_stack = []
        pre = None
        node_stack.append(node)
        while len(node_stack) > 0:
            cur = node_stack[-1]

            # 叶子结点或者 子节点已被访问
            if (not cur.leftChild and not cur.rightChild) \
                    or (pre and (pre in [cur.rightChild, cur.leftChild])):
                print (cur.value)
                pre = node_stack.pop()
            else:
                if cur.rightChild:
                    node_stack.append(cur.rightChild)
                if cur.leftChild:
                    node_stack.append(cur.leftChild)


if __name__ == '__main__':
    """
    建立一个二叉树
          1
      2     3
    4  5  6  7
    """

    root = BinaryTree(1)

    left = root.insertLeft(2)
    right = root.insertRight(3)

    left.insertLeft(4)
    left.insertRight(5)

    right.insertLeft(6)
    right.insertRight(7)

    # root.preOrder()

    # root.inOrder()

    # root.postOrder()

    # print ('-----')

    # root.pre_order_no_recursion()

    # root.in_order_no_recursion()

    # root.post_order_no_recursion()
