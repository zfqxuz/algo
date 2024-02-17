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


