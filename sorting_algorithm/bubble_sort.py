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
