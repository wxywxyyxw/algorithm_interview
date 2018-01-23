#!/usr/bin/python
# -*- coding: utf-8 -*-
import Queue


class TreeNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


'''
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
'''


def rebuild_tree_from_per_and_in_order(per_order, in_order):
    """
    per_order: list
    in_order: list
    """
    # print (per_order,in_order)
    if not per_order or not in_order or len(per_order) != len(in_order):
        return None

    if len(per_order) == 1:
        return TreeNode(per_order[0])

    root_index = in_order.index(per_order[0])

    root = TreeNode(per_order[0])

    if len(per_order) > 1:
        root.left = rebuild_tree_from_per_and_in_order(per_order[1:root_index + 1], in_order[:root_index])
        root.right = rebuild_tree_from_per_and_in_order(per_order[root_index + 1:], in_order[root_index + 1:])

    return root


def inOrder(tree):
    if tree.left:
        inOrder(tree.left)
    print (tree.value)
    if tree.right:
        inOrder(tree.right)


def preOrder(tree):
    print (tree.value)
    if tree.left:
        preOrder(tree.left)
    if tree.right:
        preOrder(tree.right)


# 按层序遍历输出树中某一层的值
def print_one_level(tree, level):
    if not tree or level < 0:
        return 0
    if level == 0:
        print(tree.value)
        return 1
    print_one_level(tree.left, level - 1)
    print_one_level(tree.right, level - 1)


# 已知树的深度按层遍历输出树的值
def print_tree_by_level(tree, depth):
    for level in range(depth):
        print_one_level(tree, level)


# 树的层次遍历
def level_order(tree):
    node_queue = []
    node_queue.append(tree)

    while node_queue:
        node = node_queue[0]
        node_queue = node_queue[1:]
        if node.left:
            node_queue.append(node.left)
        if node.right:
            node_queue.append(node.right)
        print (node.value)


# 找出树的哪一层结点最多，输出这一层的结点数目
def max_leaf_node(tree):
    """
    在非递归后序遍历的基础上，修改栈存储{node,node depth}，添加一个字典来记录每层的结点数.

    """
    node = tree
    node_stack = []
    depth_left_nodes = {}
    pre = None
    depth = 0
    node_stack.append((node, depth))
    while len(node_stack) > 0:
        cur, cur_depth = node_stack[-1]

        # 叶子结点或者 子节点已被访问
        if (not cur.left and not cur.right) \
                or (pre and (pre in [cur.right, cur.left])):
            # print (cur.value)

            num = depth_left_nodes.get(cur_depth, 0)
            depth_left_nodes[cur_depth] = num + 1

            pre, _ = node_stack.pop()
        else:
            if cur.right:
                node_stack.append((cur.right, cur_depth + 1))
            if cur.left:
                node_stack.append((cur.left, cur_depth + 1))

    print (depth_left_nodes)

    return max(depth_left_nodes.values())


if __name__ == '__main__':
    pre_order = [4, 2, 1, 3, 10, 6, 5, 7, 8]
    in_order = [1, 2, 10, 3, 4, 5, 6, 7, 8]
    tree = rebuild_tree_from_per_and_in_order(pre_order, in_order)
    inOrder(tree)
    # preOrder(tree)

    # print_tree_by_level(tree, 3)
    # level_order(tree)
    print ('-----')
    max_leaf_node(tree)
