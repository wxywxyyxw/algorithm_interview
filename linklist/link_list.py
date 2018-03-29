# -*- coding: utf-8 -*-


# 链表结点
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def print_linked_list(linked_list):
    node = linked_list
    while node:
        print node.val
        node = node.next

"""
链表反转的解决方法
node1->node2->node3


一次操作:
1 tmp = node1->next        找出我的下一个
2 node1->next = pre(None)  每次我都去隔壁当排头
3 pre =node1               然后给我一个排头的头衔
4 node1 = tmp              从下一个开始循环


"""

class Solution:
    """
    @param head: The first node of the linked list.
    @return: You should return the head of the reversed linked list.
                  Reverse it in-place.
    """
    @classmethod
    def reverse(self, head):
        # write your code here
        if head is None: return None
        p = head
        cur = None
        pre = None
        while p is not None:
            cur = p.next
            p.next = pre
            pre = p
            p = cur
        return pre


def test_reverse():
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    print_linked_list(node1)
    print ('----after reverse----')
    print print_linked_list(Solution.reverse(node1))


if __name__ == '__main__':
    test_reverse()
