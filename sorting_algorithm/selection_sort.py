import math

from sorting import Sorter
class SelectionSorter(Sorter):
    def __init__(self):
        super().__init__()

    def sort(self):
        temp=self.data.copy()
        for i in range(len(temp)):
            min = math.inf
            min_index=-1
            for j in range(i,len(temp)):
                if temp[j]<min:
                    min_index=j
                    min=temp[j]
            temp[min_index]=temp[i]
            temp[i]=min
        self.data=temp

    def suggested(self):
        '''
        选择排序（Selection Sort）：
        选择排序是一种简单直观的排序算法。它的工作原理是每次从待排序的数据元素中选出最小（或最大）的一个元素，
        存放在序列的起始位置，然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序的序列末尾。
        以此类推，直到所有元素均排序完毕。
        '''
            # 获取列表长度
        n = len(self.data)
        # 遍历所有列表元素
        for i in range(n):
            # 将当前位置设为最小值位置
            min_index = i
            # 从i+1位置到列表末尾选择出最小数据
            for j in range(i + 1, n):
                if self.data[j] < self.data[min_index]:
                    min_index = j
            # 将找到的最小值与第i位置的值交换
            self.data[i], self.data[min_index] = self.data[min_index], self.data[i]


if __name__ == '__main__':
    SelectionSorter().run()
