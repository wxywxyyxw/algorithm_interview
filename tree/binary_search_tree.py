#!/usr/bin/python
# -*- coding: utf-8 -*-


class TreeNode(object):
    def __init__(self, key, value, left=None, right=None, parent=None):
        self.key = key
        self.value = value
        self.leftChild = left
        self.rightChild = right
        self.parent = parent


# 定义二叉搜索树(非平衡)
class BinarySearchTree(object):
    def __init__(self):
        self.root = None
        self.size = 0

    def __contains__(self, key):
        """
        __contains__():当使用in，not in 对象的时候 调用(not in 是在in完成后再取反,实际上还是in操作)
        """
        if self.find(key):
            return True
        else:
            return False

    def __setitem__(self, k, v):
        """
        def __setitem__(self, key, value): 相当于 dict_test = {’k’:’v’} dict_test[‘k’] = ‘a'
        """
        self.add(k, v)

    def __delitem__(self, key):
        self.remove(key)

    def add(self, key, value):
        if self.root:
            self._add_new(key, value, self.root)
        else:
            node = TreeNode(key, value)
            self.root = node
            self.size = self.size + 1

    def remove(self, key):
        if self.size > 1:
            self._remove_node(key)
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError('Error, key not in tree')

    def find(self, key):
        if self.root:
            node = self._find(key, self.root)

            return node.value if node else None

        else:
            return None

    def max(self):
        return self._find_max(self.root).key

    def min(self):
        return self._find_min(self.root).key

    def show(self):
        root = self.root
        self.inOrder(root)

    def inOrder(self, node):
        """
        中序遍历: 左中右
        先遍历左子树，在访问自己，在遍历右子树
        """

        if not node:
            return

        if node.leftChild:
            left = node.leftChild
            self.inOrder(left)

        print ('%s(%s)' % (str(node.key), str(node.value)))

        if node.rightChild:
            right = node.rightChild
            self.inOrder(right)

    @property
    def depth(self):

        return self._get_depth(self.root)


    def _add_new(self, key, value, node):
        if key < node.key:
            if node.leftChild:
                self._add_new(key, value, node.leftChild)
            else:
                node.leftChild = TreeNode(key, value, parent=node)
        elif key > node.key:
            if node.rightChild:
                self._add_new(key, value, node.rightChild)
            else:
                node.rightChild = TreeNode(key, value, parent=node)
        else:
            node.value = value

    def _find(self, key, node):
        if not node:
            return None
        elif key == node.key:
            return node
        elif key < node.key:
            return self._find(key, node.leftChild)
        else:
            return self._find(key, node.rightChild)

    def _remove_node(self, key):
        node = self._find(key, self.root)
        if node:
            # 如果没有左右子树，直接删除这个节点
            if not node.leftChild and not node.rightChild:
                parent_node = node.parent
                if parent_node.leftChild == node:
                    parent_node.leftChild = None
                else:
                    parent_node.rightChild = None

            # 如果只有左子树，则用左子树的根结点顶替它的位置
            elif node.leftChild and not node.rightChild:
                parent_node = node.parent if node.parent else self.root
                if parent_node.leftChild == node:
                    parent_node.leftChild = node.leftChild
                else:
                    parent_node.rightChild = node.leftChild
                node.leftChild.parent = parent_node

            # 如果只有右子树，则用右子树的根结点顶替它的位置
            elif node.rightChild and not node.leftChild:
                parent_node = node.parent if node.parent else self.root
                if parent_node.leftChild == node:
                    parent_node.leftChild = node.rightChild
                else:
                    parent_node.rightChild = node.rightChild
                node.rightChild.parent = parent_node

            # 如果左右子树都存在，则用删除节点的直接前驱(左子树的最大值替代它)
            else:
                max_left_node = self._find_max(node.leftChild)
                max_key, max_value = max_left_node.key, max_left_node.value

                # 进行替代
                node.key, node.value = max_key, max_value

                parent_node = max_left_node.parent

                if max_left_node.leftChild:
                    parent_node.rightChild = max_left_node.leftChild
                    max_left_node.leftChild.parent = parent_node
                else:
                    parent_node.rightChild = None

            self.size = self.size - 1

        else:
            raise KeyError('Error, key not in tree')

    def _find_max(self, root_node):
        node = root_node
        while node.rightChild:
            node = node.rightChild
        return node

    def _find_min(self, root_node):
        node = root_node
        while node.leftChild:
            node = node.leftChild
        return node

    def _get_depth(self,node):

        if not node:
            return 0

        left =  self._get_depth(node.leftChild)
        right =  self._get_depth(node.rightChild)

        return left + 1 if left > right else right + 1

if __name__ == '__main__':
    tree = BinarySearchTree()
    tree[2] = 5
    tree[1] = 5
    tree[1] = 8
    tree[3] = 5
    tree[100] = 3
    tree[34] = 0

    # tree.show()
    # del tree[2]
    # print ('----')
    # tree.show()
    # del tree[3]
    # print ('----')
    # tree.show()
    # del tree[1]
    # print ('----')
    tree.show()
    print (tree.max(), tree.min())
    print tree.depth
