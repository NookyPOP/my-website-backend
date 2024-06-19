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


print(bubble_sort([1, 3, 4, 2, 1]))
