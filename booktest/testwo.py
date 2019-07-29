


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

    L[left] = pivotkey
    print("left:"+str(left))
    return left




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
    print(less)
    print(greater)
    print(base)
    # 递归调用
    return quicksort(less) + [base] + quicksort(greater)

if __name__ == '__main__':
    myList = [49, 38, 65, 97, 76, 13, 27, 49]
    print(myList)
    print(quicksort(myList))
