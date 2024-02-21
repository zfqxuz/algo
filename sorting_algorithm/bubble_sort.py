from sorting import Sorter
class BubbleSorter(Sorter):
    def __init__(self):
        super().__init__()

    def sort(self):

        temp=self.data.copy()
        n=len(temp)-1
        while n>0:
            for i in range(n):
                if temp[i]>temp[i+1]:
                    temp[i],temp[i+1]=temp[i+1],temp[i]
            n-=1
        self.data=temp

    def suggested(self):
        '''
        冒泡排序（Bubble Sort）：
        冒泡排序是一种简单直观的排序算法。它重复地遍历待排序的数列，一次比较两个元素，如果它们的顺序错误就把它们交换过来。
        遍历数列的工作是重复进行直到没有再需要交换，即该数列已经排序完成。
        这个算法的名字由来是因为越小的元素会经由交换慢慢“浮”到数列的顶端。
        '''
        n = len(self.data)
        # 遍历所有数组元素
        for i in range(n):
            # Last i elements are already in place
            for j in range(0, n - i - 1):
                # 遍历列表从头到尾，对每个元素...
                # 如果当前元素大于下一个元素，则交换它们
                if self.data[j] > self.data[j + 1]:
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]


if __name__ == '__main__':
    BubbleSorter().run()
