# -*- coding: utf-8 -*-
import money
def send():
    save_money = money.saved_money + money.salary
    print(f"我的存款是{save_money}")

if __name__ == '__main__':
    send()