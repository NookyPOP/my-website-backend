def select_sort(items, comp=lambda x, y: x > y):
    """简单选择排序"""
    """ 
    从第一个元素开始跟后面的元素比较，然后从第二个元素跟后面的元素比较
    正序：把最大的放在后面 
    反序：把最大的放在前面
    """

    items = items[:]
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i + 1, len(items)):
            if comp(items[j], items[min_index]):
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]
    return items


# print(select_sort([1, 3, 2]))


def bubble_sort(items, comp=lambda x, y: x > y):
    """冒泡排序"""
    """ 
    第一轮：从第一个元素跟第二个元素比较，交换把大放后面，然后第二个元素跟第三个元素比较，也是那个大放后面。。。，最后找到最大的那个元素
    第二轮：会少一个元素比较，就是最后一个元素；继续从第一个元素跟第二个元素比较，那个大放后面，然后第二个元素跟第三个元素比较，也是那个大放后面。。。，最后找到次之大的元素
    正序：一步一步把最大的交换到最后面
    """
    items = items[:]
    for i in range(len(items) - 1):
        swapped = False
        for j in range(len(items) - 1 - i):
            if comp(items[j], items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if not swapped:
            break
    return items


# print(bubble_sort([1, 3, 4, 2, 1]))


def bubble_sort(items, comp=lambda x, y: x > y):
    """搅拌排序(冒泡排序升级版)"""
    """
    第一轮：从左到右第一个元素与第二个元素比较，大者交换到后面，然后第二个与第三个元素比较，也是大者放在后面，最后总会找到那个大的元素
    然后，开始反向，把最后一个最大的元素忽略掉，然后从倒数第二个元素开始，然后步数为-1，开始比较，倒数第二个元素与倒数第三个元素比较，把小者交换到前面
     
    """
    items = items[:]
    for i in range(len(items) - 1):
        swapped = False
        for j in range(len(items) - 1 - i):
            if comp(items[j], items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if swapped:
            swapped = False
            for j in range(len(items) - 2 - i, i, -1):
                if comp(items[j - 1], items[j]):
                    items[j], items[j - 1] = items[j - 1], items[j]
                    swapped = True
        if not swapped:
            break
    return items


# print(bubble_sort([1, 3, 4, 2]))


def merge(items1, items2, comp=lambda x, y: x < y):
    """合并(将两个有序的列表合并成一个有序的列表)"""
    """ 将list分开后，然后再继续拆分，分到单个元素，然后比较单个元素，然后放在items"""
    items = []
    index1, index2 = 0, 0
    while index1 < len(items1) and index2 < len(items2):
        if comp(items1[index1], items2[index2]):
            items.append(items1[index1])
            index1 += 1
        else:
            items.append(items2[index2])
            index2 += 1
    items += items1[index1:]
    items += items2[index2:]
    return items


def merge_sort(items, comp=lambda x, y: x < y):
    return _merge_sort(list(items), comp)


def _merge_sort(items, comp):
    """归并排序"""
    if len(items) < 2:
        return items
    mid = len(items) // 2  # 中间的整数索引 // 整除运算符，返回商的整数部分；
    left = _merge_sort(items[:mid], comp)
    right = _merge_sort(items[mid:], comp)
    return merge(left, right, comp)


# merge_sort([1, 3, 1, 4, 2])


# 查找算法


def bin_search(items, key):
    """折半查找"""
    """ 如果key小于中间折半值，就往前推，然后再折半，然后再更中间值比较，如果继续小于继续推，如果大于中间折半值，就往后推 """
    start, end = 0, len(items) - 1
    while start <= end:
        mid = (start + end) // 2
        if key > items[mid]:
            start = mid + 1
        elif key < items[mid]:
            end = mid - 1
        else:
            return mid
    return -1


bin_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)
