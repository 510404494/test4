import random

'''
排序方法
第一种 冒泡排序
第二种 选择排序
第三种 插入排序
第四种 希尔排序
第五种 快速排序
第六种 基数排序
第七种 归并排序
第八种 堆排序
'''

'''
    one
 冒泡排序 
 外循环：需要多少轮冒泡
 内循环：比较冒泡出来最大值或最小值
 比较相邻一位并把最大值放在末端
'''
def bubble_sort(arr):
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            if (arr[j-1]<arr[j]):
                arr[j-1],arr[j] = arr[j],arr[j-1]
    return arr
'''
    two
 选择排序 
 1.依次取出一个数
 2.比较后边的数 获取最大值，或最小值
'''
def select_sort(arr):
    for i in range(0,len(arr)):
        for j in range(i + 1, len(arr)):
            if(arr[i]<arr[j]):
                arr[i], arr[j] = arr[j], arr[i]
    return arr


'''
    three
 插入排序
 1.一次取出数据 进行比较 循环出来比较次数
 2.比较后边的数 获取最大值，或最小值
'''
def insert_sort(arr):
    for i in range(1,len(arr)):
        key= arr[i]
        j = i-1
        while j>=0 and key<arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print(arr)
    return arr
def insert_sort2(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        for j in range(0,i):
            if(key<arr[j]):
                key ,arr[j] =arr[j],key
        arr[i] = key
    return arr
'''
希尔排序
    four
 1.第一个for 分组次数 10个数应该分3组=== 5，3，1 （10/2）-2
 2.第二个for 循环分组对应的数据 与第一个for组成一对 对应 5后的数据
 3.第三个for 0与5 1与6 ...比较
'''
def shell_sort(arr):
    for n in range(len(arr)//2,0,-2):
        for i in range(n,len(arr)):
            for j in range(i - n, -1, -1):
                if (arr[j] > arr[i]):
                    arr[i], arr[j] = arr[j], arr[i]
    return arr
'''
基数排序
    five
 1.取出最大值
 2.第二个for 循环分组对应的数据 与第一个for组成一对 对应 5后的数据
 3.第三个for 0与5 1与6 ...比较
'''
def radix_sort(s):
    max_num = max(s)  # 最大值
    j = len(str(max_num))  # 记录最大值的位数
    for i in range(j):
        bucket_list =[[] for _ in range(10)] #初始化桶数组
        for x in s:
            bucket_list[int(x / (10**i)) % 10].append(x) # 找到位置放入桶数组
        s.clear()
        for x in bucket_list:   # 放回原序列
            for y in x:
                s.append(y)
    return s

'''
快速排序
    six
 1. 先从待排序数组中选出一个数作为基数（取第一个数即可）
 2. 将原来的数组划分为两部分 小于基数的放左边，大于基数的放右边
 3. 然后在对这两个部分进行递归
 4. 组成左子数+基数+右子数
'''

def quick_sort(L):
    return q_sort(L, 0, len(L) - 1)

def q_sort(L, left, right):
    if left < right:
        pivot = Partition(L, left, right)
        q_sort(L, left, pivot - 1)
        q_sort(L, pivot + 1, right)
    return L

def Partition(L, left, right):
    pivotkey = L[left]
    while left < right:
        while left < right and L[right] >= pivotkey:
            right -= 1
        L[left] = L[right]
        while left < right and L[left] <= pivotkey:
            left += 1
        L[right] = L[left]
        print(left)
        print(L)
    L[left] = pivotkey
    return left

'''
快速排序 方法二
    six
 1. 先从待排序数组中选出一个数作为基数（取第一个数即可）
 2. 将原来的数组划分为两部分 小于基数的放左边，大于基数的放右边
 3. 然后在对这两个部分进行递归
 4. 组成左子数+基数+右子数
'''
def quicksort(nums):
    if len(nums) <= 1:return nums
    # 左子数组,右子数组
    less , greater= [],[]
    # 基准数 --pop默认最后一个
    base = nums.pop()

    # 对原数组进行划分
    for x in nums:
        if x < base:
            less.append(x)
        else:
            greater.append(x)
    # 递归调用
    return quicksort(less) + [base] + quicksort(greater)

'''
归并排序
    seven
 1. 
 1. 获取序列中值数 进行拆分 
 2. 将原来的数组划分为两部分 小于基数的放左边，大于基数的放右边
 3. 然后在对这两个部分进行递归
 4. 组成左子数+基数+右子数
'''
def merge_sort(array):
    merge_cat(array,0,len(array)-1)
def merge_cat(array,start,end):
    if(start<end):
        middle = (start + end) // 2
        merge_cat(array, start, middle)
        merge_cat(array, middle+1, end)
        merge(array, start, middle, end)
def merge(array,low,middle,high):
    temp = array[low:high + 1]
    print(temp)
    i = low
    j = middle + 1
    index = 0
    if (len(temp) > 1):
        while (i <= middle and j <= high):
            if (array[i] < array[j]):
                temp[index] = array[i]
                i += 1
            else:
                temp[index] = array[j]
                j += 1
            index += 1

        while (j <= high):
            temp[index] = array[j]
            index += 1
            j += 1
        while (i <= middle):
            temp[index] = array[i]
            index += 1
            i += 1

    for k in range(0, len(temp)):
        array[low + k] = temp[k]

'''
堆排序
    eight
 1. 
 1. 获取序列中值数 进行拆分 
 2. 将原来的数组划分为两部分 小于基数的放左边，大于基数的放右边
 3. 然后在对这两个部分进行递归
 4. 组成左子数+基数+右子数
'''

def heap(array):
    start = len(array)//2-1
    for i in range(start,-1,-1):
        heapSort(array,len(array),i)
    for i in range(len(array)-1,0,-1):
        array[i],array[0] = array[0],array[i]
        heapSort(array,i,0)

def heapSort(array,size,index):
    max = index
    leftNode = 2*index+1
    rightNode = 2*index+2
    if(leftNode<size and array[leftNode]>array[max]):
        max = leftNode
    if(rightNode<size and array[rightNode]>array[max]):
        max = rightNode
    if(max!=index):
        array[max],array[index] = array[index],array[max]
        heapSort(array,size,max)


if __name__ == '__main__':

    array = [random.randint(1,999) for i in range(10)]
    #array = [49, 38, 65, 97, 76, 13, 27, 49]
    print(array)
    heap(array)
    print(array)
