
'''
将数组中的每一位跟后面的序列进行比较，然后将最小的依次赋值给新数组，耗时较长；长度为n的数组  比较所需的次数为(n-1)+(n-2)+...+2+1=n*(n-1)/2
'''
def select_sort(items, comp=lambda x, y: x < y):
    """简单选择排序"""
    items = items[:]
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i + 1, len(items)):
            if comp(items[j], items[min_index]):
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]
    return items

