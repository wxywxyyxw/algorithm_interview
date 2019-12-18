__author__ = 'wangxiaoyang'
"""
10 递归：如何用三行代码找到“最终推荐人”？
递归需要满足的三个条件
1. 一个问题的解可以分解为几个子问题的解
2. 这个问题与分解之后的子问题，除了数据规模不同，求解思路完全一样
3. 存在递归终止条件
写递归代码最关键的是写出递推公式，找到终止条件
写递归代码的关键就是找到如何将大问题分解为小问题的规律，并且基于此写出递推公式，然后再推敲终止条件，最后将递推公式和终止条件翻译成代码
递归代码要警惕堆栈溢出
递归代码要警惕重复计算
"""
