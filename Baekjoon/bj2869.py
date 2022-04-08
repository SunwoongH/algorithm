'''
Created by sunwoong on 2022/04/08
'''
day, night, goal = map(int, input().split())
print(2 + (goal - day) // (day - night) if (goal - day) % (day - night) != 0 else 1 + (goal - day) // (day - night) if day != goal else 1)