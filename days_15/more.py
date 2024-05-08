# prices = {
#     'AAPL': 191.88,
#     'GOOG': 1186.96,
#     'IBM': 149.24,
#     'ORCL': 48.44,
#     'ACN': 166.89,
#     'FB': 208.09,
#     'SYMC': 21.29
# }

# prices2 = { key : value for key, value in prices.items() if value > 100 }

names = [
'guanyu',
'zhangfei',
'zhaoyun',
'machao',
'huangzhong'
]
coures = ['Chinese','Math','English']

scores = [[None] * len(coures) for _ in range(len(names))]
for row,name in enumerate(names):
    for col,coure in enumerate(coures):
        scores[row][col] = float(input(f'请输入{name}的{coure}成绩:'))
        print(scores)
