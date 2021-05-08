__author__ = 'wangxiaoyang'
"""
52 算法实战（一）：剖析Redis常用数据类型对应的数据结构
列表（list）
两种实现方法，一种是压缩列表（ziplist），另一种是双向循环链表
列表中保存的单个数据（有可能是字符串类型的）小于 64 字节；列表中数据个数少于 512 个。用压缩列表
字典（hash）
两种实现方式。一种是我们刚刚讲到的压缩列表，另一种是散列表。
字典中保存的键和值的大小都要小于 64 字节；字典中键值对的个数要小于 512 个。用压缩列表
散列表的扩容与缩容，装载因子大于 1, 扩容 *2。当装载因子小于 0.1，缩容，缩小为字典中数据个数的大约 2 倍大小。
集合（set）
两种实现方法，一种是基于有序数组，另一种是基于散列表。
存储的数据都是整数，存储的数据元素个数不超过 512 个，用有序数组
有序集合（sortedset）
当数据量比较小的时候，Redis 会用压缩列表来实现有序集合，大的话用跳表实现
所有数据的大小都要小于 64 字节；元素个数要小于 128 个。用压缩列表实现
redis持久化
第一种是清除原有的存储结构，只将数据存储到磁盘中。当我们需要从磁盘还原数据到内存的时候，再重新将数据组织成原来的数据结构。
实际上，Redis 采用的就是这种持久化思路
"""