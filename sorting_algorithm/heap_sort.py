import math

from sorting import Sorter
class HeapSorter(Sorter):
    def __init__(self):
        super(HeapSorter, self).__init__()

    class Heap:
        def __init__(self,data):
            self.data=data
            self.build_maxheap()

        def get_left(self,index):
            left_index=index*2+1
            if len(self.data)>left_index:
                return left_index,self.data[left_index]
            return None,None

        def get_right(self,index):
            right_index=index*2+2
            if len(self.data) >right_index:
                return right_index,self.data[right_index]
            return None,None

        def get_parent(self,index):
            parent_index=(index+1)//2-1
            if parent_index<0:
                return None,None
            return parent_index,self.data[parent_index]

        def max_heapify(self, index):
            largest = index
            left_index, left_value = self.get_left(index)
            right_index, right_value = self.get_right(index)

            # 如果左子节点大于父节点，则标记左子节点为最大
            if left_index is not None and left_value > self.data[largest]:
                largest = left_index

            # 如果右子节点是最大的，则更新最大值标记
            if right_index is not None and right_value > self.data[largest]:
                largest = right_index

            # 如果最大值不是当前考虑的父节点，则需要交换
            if largest != index:
                self.data[index], self.data[largest] = self.data[largest], self.data[index]
                # 递归地调整交换后的子树
                self.max_heapify(largest)

        def build_maxheap(self):
            for i in range(len(self.data) // 2 - 1, -1, -1):
                self.max_heapify(i)


    def sort(self):
        temp=self.data.copy()
        heap=self.Heap(temp)
        rst=[]
        while len(heap.data)>0:
            rst.append(heap.data[0])
            heap.data=heap.data[1:]
            heap.build_maxheap()
        self.data=rst


    def suggested(self):
        temp=self.data.copy()
        heap=self.Heap(temp)
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