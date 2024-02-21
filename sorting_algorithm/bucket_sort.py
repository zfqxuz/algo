from sorting import Sorter
from bubble_sort import BubbleSorter

class BucketSorter(Sorter):
    def __init__(self,data_len):
        super().__init__(data_len)
        self.nbuckets=10
        self.inbucket_sorter=BubbleSorter()


    def sort(self):
        buckets=[[] for _ in range(self.nbuckets)]
        rst=[]
        for num in self.data:
            buckets[num//10].append(num)
        print(buckets)
        for bucket in buckets:
            rst+=self.inbucket_sorter.sort_on_data(bucket)

        self.data=rst

    def suggested(self):
        '''
        桶排序（Bucket Sort）：
        桶排序是一种分布式排序算法，它将元素分布到几个称为“桶”的区间里。
        每个桶再个别排序（可能使用别的排序算法或是以递归方式继续使用桶排序进行排序），最后合并桶就得到了排序好的数组。
        '''
        def bucket_sort(data):
            if not data:
                return data

            # 确定最大值和最小值以计算桶的大小和数量
            min_value, max_value = min(data), max(data)
            bucket_range = (max_value - min_value) / len(data) + 1  # 避免除以0
            buckets = [[] for _ in range(int((max_value - min_value) / bucket_range) + 1)]

            # 将数据分配到各个桶中
            for num in data:
                index = int((num - min_value) / bucket_range)
                buckets[index].append(num)

            # 对每个桶进行排序，并收集排序后的数据
            sorted_data = []
            for bucket in buckets:
                sorted_data.extend(sorted(bucket))  # 使用Python内置排序

            return sorted_data

if __name__ == '__main__':
    BucketSorter(100).run()