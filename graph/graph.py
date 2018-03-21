# -*- coding: utf-8 -*-

# 图的存储方式:
# 1 邻接矩阵
# 2 领结表
# 3 十字链表

class Queue:
    def __init__(self,max_size):
        self.max_size = int(max_size)
        self.queue = []

    def put(self,data):
        if self.max_size > 0:
            if self.full():
                raise ValueError('Queue is full!')
            else:
                self._put(data)

    def get(self):
        if self._queue_size() > 0:
            result = self._get()
            empty_flag = False
        else:
            result = None
            empty_flag = True
        return result

    def empty(self):
        if self._queue_size() == 0:
            return True
        else:
            return False

    def full(self):
        if self._queue_size() == self.max_size:
            return True
        else:
            return False

    def _put(self,data):
        self.queue.append(data)

    def _get(self):
        result = self.queue[0]
        self.queue.pop(0)
        return result

    def _queue_size(self):
        return len(self.queue)

# 图的深度遍历
# 利用 栈 和 一个已访问列表来 实现深度遍历的非递归
def dfs(self,first_node):
    stack_lsit = []
    visited = []
    stack_lsit.append(first_node)
    visited.append(first_node)
    while len(stack_lsit) > 0:
        x = stack_lsit[-1]
        for w in x.neighbor_list:
            if not w in visited:
                print(w.data)
                visited.append(w)
                stack_lsit.append(w)
                break

        stack_lsit.pop()

# 图的广度遍历
# 利用 栈 和 一个已访问列表来 实现深度遍历的非递归
def bsf(first_node):
    queue = Queue(100000)
    visited = []
    queue.put(first_node)
    visited.append(first_node)
    print first_node.data

    while not queue.empty():
        node =queue.get()
        neighbors = node.neighbor_list
        for neighbor in neighbors:
            if neighbor not in visited:
                print neighbor.data
                visited.append(neighbor)
                queue.put(neighbor)

"""
连通图：在无向图中，若任意两个顶点vi与vj都有路径相通，则称该无向图为连通图。
强连通图：在有向图中，若任意两个顶点vi与vj都有路径相通，则称该有向图为强连通图。
连通网：在连通图中，若图的边具有一定的意义，每一条边都对应着一个数，称为权；权代表着连接连个顶点的代价，称这种连通图叫做连通网。
生成树：一个连通图的生成树是指一个连通子图，它含有图中全部n个顶点，但只有足以构成一棵树的n-1条边。一颗有n个顶点的生成树有且仅有n-1条边，如果生成树中再添加一条边，则必定成环。
最小生成树：在连通网的所有生成树中，所有边的代价和最小的生成树，称为最小生成树。
"""



class GraphNode:
    def __init__(self,data):
        self.neighbor_list = []
        self.data = data

if __name__ == '__main__':
    node_a = GraphNode('a')
    node_b = GraphNode('b')
    node_c = GraphNode('c')
    node_d = GraphNode('d')
    node_e = GraphNode('e')
    node_f = GraphNode('f')

    node_a.neighbor_list = [node_b,node_c]
    node_b.neighbor_list = [node_a,node_c,node_e]
    node_c.neighbor_list = [node_a,node_b,node_d]
    node_d.neighbor_list = [node_c]
    node_e.neighbor_list = [node_b,node_f]
    node_f.neighbor_list = [node_e]

    bsf(node_a)


