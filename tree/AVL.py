#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
AVL树是根据它的发明者G.M. Adelson-Velsky和E.M. Landis命名的。
它是最先发明的自平衡二叉查找树，也被称为高度平衡树。相比于"二叉查找树"，它的特点是：AVL树中任何节点的两个子树的高度最大差别为1

AVL树插入结点方法：
1.找到要插入的位置
2.加入新节点
3.沿着寻找结点的路线返回，
3.1检查路线上所有节点的两个子树的高度最大差别是否大于1，
    3.1a: 如果大于，就需要对该树进行旋转,更新进行旋转后的结点高度
    3.1b: 如果不大于，就仅更新结点的高度
"""


class TreeNode(object):
    def __init__(self, key, value, left=None, right=None, parent=None):
        self.key = key
        self.value = value
        self.leftChild = left
        self.rightChild = right
        self.parent = parent
        self.height = 0
        # print ('add ', self.key)


class AVL(object):
    def __init__(self):
        self.root = None
        self.size = 0

    def __setitem__(self, k, v):
        self.add(k, v)

    def show(self):
        root = self.root
        self.inOrder(root)

    def inOrder(self, node):
        if not node:
            return

        if node.leftChild:
            left = node.leftChild
            self.inOrder(left)

        print ('%s(%s l: %s r: %s p:%s)'
               % (str(node.key),
                  str(node.height),
                  str(node.leftChild.key) if node.leftChild else None,
                  str(node.rightChild.key) if node.rightChild else None,
                  str(node.parent.key) if node.parent else None)
               )

        if node.rightChild:
            right = node.rightChild
            self.inOrder(right)

    def add(self, key, value):
        if not self.root:
            self.root = TreeNode(key, value)
            self.size = self.size + 1
        else:
            self._add_new(key, value, self.root)

    def _add_new(self, key, value, node):
        """
        性质：当我们向avl树中插入一个新节点时，所有已经存在的结点的高度都已经被计算
        """
        if key < node.key:
            if node.leftChild:
                self._add_new(key, value, node.leftChild)

                print (
                    'node ', node.key, 'left:', self._height(node.leftChild), 'right:', self._height(node.rightChild))

                if self._height(node.leftChild) - self._height(node.rightChild) == 2:
                    self._balance(node, 'left') if key < node.leftChild.key else self._balance(node, 'left', 'right')

            else:
                node.leftChild = TreeNode(key, value, parent=node)
                self.size = self.size + 1

        elif key > node.key:
            if node.rightChild:
                self._add_new(key, value, node.rightChild)

                print (
                    'node ', node.key, 'right:', self._height(node.rightChild), 'left:', self._height(node.leftChild))

                if self._height(node.rightChild) - self._height(node.leftChild) == 2:
                    self._balance(node, 'right') if key > node.rightChild.key else self._balance(node, 'right', 'left')
            else:
                node.rightChild = TreeNode(key, value, parent=node)
                self.size = self.size + 1
        else:
            node.value = value

        self._renew_height(node)

    def _height(self, node):
        if not node:
            return -1
        else:
            return node.height

    def _renew_height(self, node):
        node.height = max(self._height(node.leftChild), self._height(node.rightChild)) + 1
        # print (node.key,' height: ' ,node.height)

    def _balance(self, node, direction_one, direction_two=''):
        if direction_one == 'left' and not direction_two:
            self._single_rotate_left(node)
        elif direction_one == 'right' and not direction_two:
            self._single_rotate_right(node)
        elif direction_one == 'left' and direction_two == 'right':
            self._rotate_left_right(node)
        elif direction_one == 'right' and direction_two == 'left':
            self._rotate_right_left(node)

    def _single_rotate_left(self, node):
        left = node.leftChild

        node.leftChild = left.rightChild
        if node.leftChild:
            node.leftChild.parent = node

        left.rightChild = node
        left.parent = node.parent

        if not node.parent:
            left.parent = None
            self.root = left
        else:
            if node.parent.leftChild == node:
                node.parent.leftChild = left
            else:
                node.parent.rightChild = left
        node.parent = left

        self._renew_height(node)
        self._renew_height(left)

    def _single_rotate_right(self, node):
        right = node.rightChild

        node.rightChild = right.leftChild
        if node.rightChild:
            node.rightChild.parent = node

        right.leftChild = node
        right.parent = node.parent

        if not node.parent:
            right.parent = None
            self.root = right
        else:
            if node.parent.leftChild == node:
                node.parent.leftChild = right
            else:
                node.parent.rightChild = right

        node.parent = right

        self._renew_height(node)
        self._renew_height(right)

    def _rotate_left_right(self, node):
        self._single_rotate_right(node.leftChild)
        self._single_rotate_left(node)

    def _rotate_right_left(self, node):
        self._single_rotate_left(node.rightChild)
        self._single_rotate_right(node)


if __name__ == '__main__':
    tree = AVL()
    # tree[3] = 5
    # tree[2] = 5
    # tree[1] = 5
    # tree[2.5] = 5
    # tree[0] = 5
    #
    # tree.show()
    # print (tree.root.key,tree.size)
    # for i in [3,2,1,4,5,6,7,16,15,14,13,12,11,10,8,9]:
    for i in [2, 1, 10, 5, 11, 7]:
        print ("add: ", i)
        tree[i] = ''
        tree.show()
        print ('root:', tree.root.key, 'size: ', tree.size)
        print ('-----')
