__author__ = 'wangxiaoyang'
"""
12 排序（下）：如何用快排思想在O(n)内查找第K大元素？

归并排序和快速排序都用到了分治思想

归并排序（Merge Sort）
归并排序的核心思想还是蛮简单的。如果要排序一个数组，我们先把数组从中间分成前后两部分，然后对前后两部分分别排序，
再将排好序的两部分合并在一起，这样整个数组就都有序了

归并排序的性质
归并排序是一个稳定的排序算法
不管是最好情况、最坏情况，还是平均情况，时间复杂度都是 O(nlogn)
空间复杂度是 O(n)
归并排序不是原地排序算法。

快速排序的原理
如果要排序数组中下标从 p 到 r 之间的一组数据，我们选择 p 到 r 之间的任意一个数据作为 pivot（分区点）。
我们遍历 p 到 r 之间的数据，将小于 pivot 的放到左边，将大于 pivot 的放到右边，将 pivot 放到中间。
经过这一步骤之后，数组 p 到 r 之间的数据就被分成了三个部分，
前面 p 到 q-1 之间都是小于 pivot 的，中间是 pivot，后面的 q+1 到 r 之间是大于 pivot 的。
根据分治、递归的处理思想，我们可以用递归排序下标从 p 到 q-1 之间的数据和下标从 q+1 到 r 之间的数据，直到区间缩小为 1，
就说明所有的数据都有序了。

快排的时间复杂度也是 O(nlogn)，在极端情况下，才会退化到 O(n2)
快速排序并不是一个稳定的排序算法

"""
