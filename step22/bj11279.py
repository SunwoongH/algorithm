import sys

heap = []
size = -1
    
def isEmpty():
    return size == -1
def insertMaxHeap(key):
    global heap
    global size
    size += 1
    heap.append(key)
    i = size

    while i != 0:
        if i % 2 == 0:
            if key > heap[i // 2 - 1]:
                heap[i] = heap[i // 2 - 1]
                i = i // 2 - 1
            else: break
        else:
            if key > heap[i // 2]:
                heap[i] = heap[i // 2]
                i //= 2
            else: break
    heap[i] = key
def deleteMaxHeap():
    if isEmpty():
        return False
    global heap
    global size

    removed = heap[0]
    tempKey = heap[size]
    size -= 1
    parent = 0
    child = 1

    while child <= size:
        if ((child < size) and (heap[child] < heap[child + 1])):
            child += 1
        if (tempKey >= heap[child]):
            break
        heap[parent] = heap[child]
        parent = child
        child = child * 2 + 1

    heap[parent] = tempKey
    return removed

n = int(sys.stdin.readline())

result = []
for i in range(0, n):
    num = int(sys.stdin.readline())
    if num == 0:
        temp = deleteMaxHeap()
        if temp == False:
            print(0)
        else:
            print(temp)
    else:
        insertMaxHeap(num)