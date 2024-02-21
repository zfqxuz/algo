from sorting import Sorter

class QuickSorter(Sorter):
    def __init__(self):
        super().__init__()

    def sort(self):

        self.quick_sort(0,self.data_length-1)

    def quick_sort(self,left,right):

        if left>=right:
            return

        partition_index=left
        pivot_element=self.data[right]
        for i in range(left,right):
            if self.data[i]<pivot_element:
                self.swap(partition_index, i)
                partition_index+=1


        self.swap(partition_index,right)

        self.quick_sort(left,partition_index-1)
        self.quick_sort(partition_index+1,right)


    def swap(self,i,j):
        self.data[i],self.data[j]=self.data[j],self.data[i]

    def suggested(self):
        '''
        快速排序（Quick Sort）：
        快速排序是一种分治排序算法。它将一个数组分成两个子数组，将两部分独立地排序。
        快速排序以递归方式将数据分为两部分，一部分包括小于等于基准点的数据，另一部分包括大于基准点的数据，
        然后再通过递归的方式，将两部分数据分别进行快速排序，整个排序过程可以递归进行，以达到整个数据变成有序序列。
        '''
        def sort(self):
            # 调用快速排序的辅助函数，传入初始的左右边界索引
            self.quick_sort(0, len(self.data) - 1)

        def quick_sort(self, left, right):
            if left < right:
                # 执行分区操作，并获取分区索引
                partition_index = self.partition(left, right)
                # 递归地对左侧部分进行快速排序
                self.quick_sort(left, partition_index - 1)
                # 递归地对右侧部分进行快速排序
                self.quick_sort(partition_index + 1, right)

        def partition(self, left, right):
            # 选择最右侧的元素作为基准值
            pivot = self.data[right]
            partition_index = left
            for i in range(left, right):
                if self.data[i] < pivot:
                    self.swap(i, partition_index)
                    partition_index += 1
            # 将基准值移动到正确的位置
            self.swap(partition_index, right)
            return partition_index

        def swap(self, i, j):
            # 交换两个元素的位置
            self.data[i], self.data[j] = self.data[j], self.data[i]

if __name__ == '__main__':
    QuickSorter().run()