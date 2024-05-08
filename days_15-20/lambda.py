import time

from concurrent.futures import ThreadPoolExecutor


"""
资源竞争，没有资源锁，导致线程轮询中所做的变更被后来的线程不断更新，之前修改数据的成果被后续的修改覆盖掉了，得不到正确的结果。
"""
class Account(object):
    """银行账户"""

    def __init__(self):
        self.balance = 0.0

    def deposit(self, money):
        """存钱"""
        new_balance = self.balance + money
        time.sleep(0.01)
        self.balance = new_balance


def main():
    """主函数"""
    account = Account()
    with ThreadPoolExecutor(max_workers=10) as pool:
        for _ in range(100):
            pool.submit(account.deposit, 1)
    print(account.balance)


if __name__ == '__main__':
    main()