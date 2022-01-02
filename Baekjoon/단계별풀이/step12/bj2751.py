import sys

n = int(sys.stdin.readline())
num = []
for i in range(n):
    num.append(int(sys.stdin.readline()))

result = sorted(num)
for i in result:
    print(i)

# 합병정렬을 직접 만들어서 쓰면 시간초과가 뜬다.
'''
def merge(list, left, mid, right):
    sort = []
    i = left
    j = mid + 1
    k = left

    while i <= mid and j <= right:
        if list[i] <= list[j]:
            sort.append(list[i])
            i += 1
        else:
            sort.append(list[j])
            j += 1
    if i > mid:
        while j <= right:
            sort.append(list[j])
            j += 1
    else:
        while i <= mid:
            sort.append(list[i])
            i += 1
    for v in sort:
        list[k] = v
        k += 1

def mergeSort(list, left, right):
    if left < right:
        mid = (left + right) // 2
        mergeSort(list, left, mid)
        mergeSort(list, mid + 1, right)
        merge(list, left, mid, right)

num = []
for i in range(n):
    num.append(int(sys.stdin.readline()))

mergeSort(num, 0, len(num) - 1)
for i in num:
    print(i)
'''