import heapq

list1 = [34, 25, 12, 90, 87, 63, 58, 78, 88, 92]
list2 = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

print(heapq.nlargest(3,list1))   # 列表中最大的三个元素
print(heapq.nsmallest(3,list1))     # 列表中最小的三个元素
print(heapq.nlargest(2,list2,key=lambda x: x['price']))  # 按照列表内部元素的切片获取对应的最大元素
print(heapq.nsmallest(2,list2,key=lambda x:x['shares']))    # 按照列表内部元素的切片获取对应的最小元素
