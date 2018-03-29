# -*- coding: utf-8 -*-

"""
在图论中，常常将树定义为一个无回路连通图。对于一个带权的无向连通图，其每个生成树所有边上的权值之和可能不同，
我们把所有边上权值之和最小的生成树称为图的最小生成树。求图的最小生成树有很多实际应用。例如，通讯线路铺设造价最优问题就是一个最小生成树问题。
常见的求最小生成树的方法有两种：克鲁斯卡尔(Kruskal)算法和普里姆（Prim）算法。
"""

INFINITY = 65535  # 代表无穷大


# 总共九个顶点
vexs = [[0, 10, INFINITY, INFINITY, INFINITY, 11, INFINITY, INFINITY, INFINITY],  # 邻接矩阵
        [10, 0, 18, INFINITY, INFINITY, INFINITY, 16, INFINITY, 12],
        [INFINITY, INFINITY, 0, 22, INFINITY, INFINITY, INFINITY, INFINITY, 8],
        [INFINITY, INFINITY, 22, 0, 20, INFINITY, INFINITY, 16, 21],
        [INFINITY, INFINITY, INFINITY, 20, 0, 26, INFINITY, 7, INFINITY],
        [11, INFINITY, INFINITY, INFINITY, 26, 0, 17, INFINITY, INFINITY],
        [INFINITY, 16, INFINITY, INFINITY, INFINITY, 17, 0, 19, INFINITY],
        [INFINITY, INFINITY, INFINITY, 16, 7, INFINITY, 19, 0, INFINITY],
        [INFINITY, 12, 8, 21, INFINITY, INFINITY, INFINITY, INFINITY, 0]]


# 加点法
# 设置一个已访问点列表，每次找已访问点列表和未访问点列表之间最短的边，找到后，把这条边一端的未访问列表加入访问列表，继续操作，
# 直到已访问列表中包含全部结点
def prim(vexs, node_index):
    nodes_num = len(vexs)

    # 已访问列表
    visited_index_nodes = [node_index]
    min_tree = []
    min_edge_node_index = None
    min_tree_node = None

    # 只需要nodes_num-1步就可以生成最小生成树
    for step in range(0, nodes_num - 1):
        min_distance = INFINITY

        # 遍历已访问列表
        for index in visited_index_nodes:
            # 遍历与已访问列表中的点的领结点
            for i, value in enumerate(vexs[index]):
                if i not in visited_index_nodes:
                    # 找出最小距离
                    if value < min_distance:
                        min_edge_node_index = i
                        min_distance = value
                        # 记录最小边
                        min_tree_node = (index, i, min_distance)

        visited_index_nodes.append(min_edge_node_index)
        min_tree.append(min_tree_node)

    print min_tree

#加边法
#找出最小边，若两个点不再一个集合中，就合并两个集合。最后到全部点进入一个集合中
def kruskal(vexs):
    nodes_num = len(vexs)
    edges = []
    min_tree = []
    temp_edge = None
    for step in range(0, nodes_num - 1):
        min_distance = INFINITY

        for i in range(0, nodes_num):
            for j in range(0, nodes_num):
                if i != j:
                    flag = True
                    for edge in edges:
                        if i in edge and j in edge:
                            flag = False

                    if flag:
                        if vexs[i][j] < min_distance:
                            min_distance = vexs[i][j]
                            temp_edge = (i, j, vexs[i][j])

        first_edge_index = -1
        second_edge_index = -1
        for index, edge in enumerate(edges):
            if temp_edge[0] in edge:
                first_edge_index = index
            if temp_edge[1] in edge:
                second_edge_index = index

        # print first_edge_index,second_edge_index

        if first_edge_index < 0 and second_edge_index < 0:
            edges.append([temp_edge[0], temp_edge[1]])
        elif first_edge_index > -1 and second_edge_index < 0:
            edges[first_edge_index].append(temp_edge[1])
        elif first_edge_index < 0 and second_edge_index > -1:
            edges[second_edge_index].append(temp_edge[0])
        else:
            edges[first_edge_index] += edges[second_edge_index]
            edges.remove(edges[second_edge_index])

        min_tree.append(temp_edge)
        # print edges

    print min_tree


if __name__ == '__main__':
    prim(vexs, 0)
    kruskal(vexs)
