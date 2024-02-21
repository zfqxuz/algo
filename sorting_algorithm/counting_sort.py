from sorting import Sorter

class CountingSorter(Sorter):
    def __init__(self):
        super(CountingSorter, self).__init__()

    def sort(self):
        temp=self.data.copy()

        base=min(temp)
        length=max(temp)-min(temp)+1
        counter=[0]*length

        for item in temp:
            counter[item-base]+=1

        rst=[]
        for i in range(length):
            for j in range(counter[i]):
                rst.append(i+base)
        self.data=rst


    def suggested(self):
        pass

if __name__ == '__main__':
    CountingSorter().run()