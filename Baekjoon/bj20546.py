'''
Created by sunwoong on 2022/09/17
'''
import sys

def bnp(money):
    count = 0
    for price in stock_prices:
        if price <= money:
            count += money // price
            money -= money // price * price
    return money + count * stock_prices[-1]

def timing(money):
    count = 0
    is_increase = 0
    is_decrease = 0
    prev_price = None
    for price in stock_prices:
        if prev_price:
            if prev_price < price:
                is_increase += 1
                is_decrease = 0
                if is_increase >= 3 and count > 0:
                    money += count * price
                    count = 0
            elif prev_price > price:
                is_increase = 0
                is_decrease += 1
                if is_decrease >= 3:
                    if price <= money:
                        count += money // price
                        money -= money // price * price
            else:
                is_increase = 0
                is_decrease = 1
        prev_price = price
    return money + count * stock_prices[-1]

money = int(sys.stdin.readline())
stock_prices = list(map(int, sys.stdin.readline().split()))
bnp_money = bnp(money)
timing_money = timing(money)
print("BNP") if bnp_money > timing_money else print("TIMING") if bnp_money != timing_money else print("SAMESAME")