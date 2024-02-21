from  sorting import Sorter
class InsertionSorter(Sorter):
    def __init__(self):
        super().__init__()

    def sort(self):
        temp=self.data.copy()
        j=0
        while j<len(temp):
            i=j
            while (i>0) and (temp[i]<temp[i-1]):

                temp[i],temp[i-1]=temp[i-1],temp[i]
                i-=1
            j+=1
        self.data=temp

    def suggested(self):
        '''
        插入排序（Insertion Sort）：
        插入排序是一种简单直观的排序算法。它的工作方式是通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。
        插入排序在实现上，通常采用in-place排序（即只需用到O(1)的额外空间的排序）。
        '''
        # 遍历从1到数组的长度
        for i in range(1, len(self.data)):
            key = self.data[i]
            j = i - 1
            # 将选中的元素与它前面的元素比较，如果选中的元素（key）小于前面的元素，则前面的元素后移
            while j >= 0 and key < self.data[j]:
                self.data[j + 1] = self.data[j]
                j -= 1
            # 将选中的元素插入到正确的位置
            self.data[j + 1] = key


if __name__ == '__main__':
    InsertionSorter().run()


