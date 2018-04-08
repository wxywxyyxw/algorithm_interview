# -*- coding: utf-8 -*-

def adjust_heap(lists, i, size):
    lchild = 2 * i + 1
    rchild = 2 * i + 2
    max = i
    if i < size / 2:
        if lchild < size and lists[lchild] > lists[max]:
            max = lchild
        if rchild < size and lists[rchild] > lists[max]:
            max = rchild
        if max != i:
            lists[max], lists[i] = lists[i], lists[max]
            adjust_heap(lists, max, size)

#从初始状态开始构建大根堆
def build_heap(lists, size):
    #从非叶子结点开始
    for i in range(0, (size/2))[::-1]:
        print i
        adjust_heap(lists, i, size)

#堆排序
def heap_sort(lists):
    size = len(lists)
    build_heap(lists, size)
    for i in range(0, size)[::-1]:
        lists[0], lists[i] = lists[i], lists[0] #交换根结点和最后一个元素(把最大的元素放到队列的最后)
        adjust_heap(lists, 0, i)


if __name__ == '__main__':
    list1 = [4,6,7,3,5,0,9]
    heap_sort(list1)
    print (list1)

    #build_heap(list1,len(list1))