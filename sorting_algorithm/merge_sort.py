from sorting import Sorter
class MergeSorter(Sorter):
    def __init__(self):
        super().__init__()

    def sort(self):
        temp=self.data.copy()
        self.data=self.split(temp)


    def split(self,data):
        if len(data)==1:
            return data
        elif len(data)==2:
            return [min(data),max(data)]
        else:
            mid_index=len(data)//2
            left=data[:mid_index]
            right=data[mid_index:]
            return self.merge(left,right)

    def merge(self,left,right):
        merged=[]
        left=self.split(left)
        right=self.split(right)
        left_index=right_index=0
        while (left_index<len(left)) and (right_index<len(right)):
            if left[left_index]<right[right_index]:
                merged.append(left[left_index])
                left_index+=1
            else:
                merged.append(right[right_index])
                right_index+=1
        if left_index<len(left):
            merged+=left[left_index:]
        else:
            merged+=right[right_index:]
        return merged

    def suggested(self):
        '''
        归并排序（Merge Sort）：
        归并排序是建立在归并操作上的一种有效的排序算法，该算法是采用分治法（Divide and Conquer）的一个非常典型的应用。
        归并排序先递归地分解数列，再将它们合并。每次合并操作是将两个排序好的序列合并成一个序列。
        '''
        def merge_sort(self):
            self.data = self.merge_sort_rec(self.data)

        def merge_sort_rec(self, array):
            if len(array) > 1:
                mid = len(array) // 2
                left_half = array[:mid]
                right_half = array[mid:]

                self.merge_sort_rec(left_half)
                self.merge_sort_rec(right_half)

                i = j = k = 0

                # 将数据合并回array中
                while i < len(left_half) and j < len(right_half):
                    if left_half[i] < right_half[j]:
                        array[k] = left_half[i]
                        i += 1
                    else:
                        array[k] = right_half[j]
                        j += 1
                    k += 1

                # 检查是否有剩余的元素
                while i < len(left_half):
                    array[k] = left_half[i]
                    i += 1
                    k += 1

                while j < len(right_half):
                    array[k] = right_half[j]
                    j += 1
                    k += 1

            return array

    @Sorter.sample_usage("小和")

    def small_sum(self):
        '''
        定义元素s小和为s的左侧小于等于s的数字的和
        定义数组小和为数组S中所有元素小和的和
        归并排序求给定数组小和，核心想法是merge时候左组和右组相对位置是不变的。
        [1,4][2,3]和[4,1][3,2]在”4在2和3前面“这一点上是等价的
        '''
        data=[1,3,4,2,5]

        def split_small_sum(data):
            if len(data)==1:
                return 0,data
            elif len(data)==2:
                return min(data),[min(data),max(data)]
            else:
                mid_index=len(data)//2
                left=data[:mid_index]
                right=data[mid_index:]
                small_sum,temp =merge_small_sum(left, right)
                return small_sum,temp

        def merge_small_sum(left,right):
            merged = []
            counter=0
            leftsum,left = split_small_sum(left)
            rightsum,right = split_small_sum(right)
            left_index = right_index = 0
            while (left_index < len(left)) and (right_index < len(right)):
                if left[left_index] < right[right_index]:
                    merged.append(left[left_index])
                    counter+=left[left_index]*(len(right)-right_index)
                    left_index += 1
                else:
                    merged.append(right[right_index])
                    right_index += 1
            if left_index < len(left):
                merged += left[left_index:]
            else:
                merged += right[right_index:]
            return counter+leftsum+rightsum,merged

        rst, sorted =split_small_sum(data)
        print(rst,sorted)

    @Sorter.sample_usage("逆序对")
    def inverse_pair(self):
        '''
        如果i<j n[i]>n[j],那么(i,j)为数组n中一组逆序对
        '''
        data=[5,3,4,2,1]
        inverse_pair_set=set()
        def split_inverse_pair( data):
            if len(data) == 1:
                return data
            elif len(data) == 2:
                if data[0]>data[1]:
                    inverse_pair_set.add(tuple(data))
                return [min(data), max(data)]
            else:
                mid_index = len(data) // 2
                left = data[:mid_index]
                right = data[mid_index:]
                return merge_inverse_pair(left, right)

        def merge_inverse_pair(left, right):
            merged = []
            left = split_inverse_pair(left)
            right = split_inverse_pair(right)
            left_index = right_index = 0
            while (left_index < len(left)) and (right_index < len(right)):
                if left[left_index] <= right[right_index]:
                    merged.append(left[left_index])

                    left_index += 1
                else:

                    inverse_pair_set.add((left[left_index],right[right_index]))
                    merged.append(right[right_index])
                    right_index += 1
            if left_index < len(left):
                merged += left[left_index:]
                for i in left[left_index:]:
                    for j in right:
                        inverse_pair_set.add((i,j))
            else:

                merged += right[right_index:]
            return merged

        split_inverse_pair(data)
        print(inverse_pair_set)

if __name__ == '__main__':
    a=MergeSorter()
    a.example('逆序对')

