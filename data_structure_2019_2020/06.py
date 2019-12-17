__author__ = 'wangxiaoyang'
"""
链表
并不需要一块连续的内存空间，它通过“指针”将一组零散的内存块串联起来使用
三种最常见的链表结构，它们分别是：单链表、双向链表和循环链表
针对链表的插入和删除操作，我们只需要考虑相邻结点的指针改变，所以对应的时间复杂度是 O(1)

和单链表相比，循环链表的优点是从链尾到链头比较方便

单向链表只有一个方向，结点只有一个后继指针 next 指向后面的结点。而双向链表，顾名思义，它支持两个方向，
每个结点不止有一个后继指针 next 指向后面的结点，还有一个前驱指针 prev 指向前面的结点
双向链表可以支持 O(1) 时间复杂度的情况下找到前驱结点

单链表LRU实现思路:
定义单链表越靠近链表尾部的结点是越早之前访问的。当有一个新的数据被访问时，我们从链表头开始顺序遍历链表。
1. 如果此数据之前已经被缓存在链表中了，我们遍历得到这个数据对应的结点，并将其从原来的位置删除，然后再插入到链表的头部。
2. 如果此数据没有在缓存链表中，又可以分为两种情况：
    如果此时缓存未满，则将此结点直接插入到链表的头部；
    如果此时缓存已满，则链表尾结点删除，将新的数据结点插入链表的头部
"""