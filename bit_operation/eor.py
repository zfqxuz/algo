#查找出数组中重复奇数次的一个整数。空间复杂度O(1)
def odd_showup(data):
    eor=0
    for item in data:
        eor^=item
    #一个位上两个相同的值异或，结果为0 所以偶数个数字会相互抵消
    return eor

#查找出数组中重复奇数次的两个整数。空间复杂度O(1)
def odd_showup_two(data):
    eor1=0
    for item in data:
        eor1^=item
    oct2bin(eor1)
    rightmost_set_bit = eor1 & -eor1

    # 将结果转换为二进制字符串，然后找到最右侧的1的位置
    # 注意：二进制字符串是从左到右表示的，所以我们需要计算长度减去索引位置
    position = len(bin(rightmost_set_bit)) - 3
    print(position)
    eor2=0
    for item in data:
        oct2bin(item)
        if (item & rightmost_set_bit)==0:
            #通过两个数不同的位来筛选子集用于第二次筛选。子集中只包含num1或者num2,以及其他会抵消的数
            eor2^=item
    a=eor1
    b=eor2
    #a 是 num1 ^ num2
    #b 是 num1
    #b ^ a 是num1 ^ num1 ^ num2= num2
    print(b)
    print(b ^ a)

def oct2bin(num):
    print(format(num, "0{}b".format(32)))

if __name__ == '__main__':
    data=[1,2,1,3,2,1,3,1,3]
    print(odd_showup(data))
    data2=[11,20,32,11,20,32,11,20,32,11]
    odd_showup_two(data2)