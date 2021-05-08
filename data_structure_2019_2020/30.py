__author__ = 'wangxiaoyang'
"""
30 | 图的表示：如何存储微博、微信等社交网络中的好友关系？
一.What-图的概念：如下就是一个图(非线性表数据结构)
1.图的分类：无向图(微信-不允许单向关注)、有向图(微博-允许单向关注)、带权图(QQ-亲密度)

2.图相关概念：
①图中的元素叫作顶点
②一个顶点可以与任意其他顶点建立连接关系，这种建立的关系叫作边
③跟顶点相连接的边的条数叫做度
④有向图中把度分为入度(表示有多少条边指向这个顶点)和出度(表示有多少条边是以这个顶点为起点指向其他顶点)
⑤在带权图中每条边都有一个权重

二.图的存储
邻接矩阵
①邻接矩阵的底层依赖一个二维数组。
②对于无向图来说，如果顶点 i 与顶点 j 之间有边，我们就将 A[i][j] 和 A[j][i] 标记为 1；
③对于有向图来说，如果顶点 i 到顶点 j 之间，有一条箭头从顶点 i 指向顶点 j 的边，就将 A[i][j]
标记为 1。同理，如果有一条箭头从顶点 j 指向顶点 i 的边，就将 A[j][i] 标记为 1。
④对于带权图，数组中就存储相应的权重
⑤缺点：浪费存储空间
(1)无向图A[i][j] 等于 1，那 A[j][i] 也肯定等于 1，只需要存储一个
(2)稀疏图-顶点很多，但每个顶点的边并不多
⑥优点：
(1)存储方式简单、直接，因为基于数组，所以在获取两个顶点的关系时，就非常高效
(2)方便计算。这是因为，用邻接矩阵的方式存储图，可以将很多图的运算转换成矩阵之间的运算


邻接表
①每个顶点对应一条链表，链表中存储的是与这个顶点相连接的其他顶点
②有向图的邻接表存储方式，每个顶点对应的链表里面，存储的是指向的顶点
③无向图来说，每个顶点的链表中存储的，是跟这个顶点有边相连的顶点
④优点：存储节省空间
⑤缺点：查找比较耗时间(邻接表中链表的存储方式对缓存不友好，所以比起邻接矩阵，在邻接表中查询两个顶点之间的关系就没那么高效)
⑥可以将邻接表中的链表改成平衡二叉查找树(红黑树)等动态数据结构(跳表、散列表等)，这样就可以更加快速地查找两个顶点之间是否存在边了。
⑦可以将链表改成有序动态数组，可以通过二分查找的方法来快速定位两个顶点之间否是存在边

3.逆邻接表：每个顶点的链表中，存储的是指向这个顶点的顶点
"""
