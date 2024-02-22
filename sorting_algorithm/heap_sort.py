import math
from  data_structure.Heap import Heap
from sorting import Sorter
class HeapSorter(Sorter):
    def __init__(self):
        super(HeapSorter, self).__init__()




    def sort(self):
        temp=self.data.copy()
        heap=Heap(temp)
        rst=[]
        while len(heap.data)>0:
            rst.append(heap.data[0])
            heap.data=heap.data[1:]
            heap.build_maxheap()
        self.data=rst


    def suggested(self):
        '''
        堆排序（Heap Sort）：
        堆排序是指利用堆这种数据结构所设计的一种排序算法。
        堆是一个近似完全二叉树的结构，并同时满足堆积的性质：即子节点的键值或索引总是小于（或者大于）它的父节点。
        '''

        temp=self.data.copy()
        heap=Heap(temp)
        rst=[]
        while len(heap.data)>0:
            rst.append(heap.data[0])
            heap.data[0]=heap.data[-1]
            heap.data=heap.data[:-1]
            heap.max_heapify(0)
            #不需要每次都调整已经排好序的部分
        self.data=rst


if __name__ == '__main__':
    HeapSorter().run()