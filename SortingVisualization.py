import pygame
import random
import time

pygame.init()
window = pygame.display.set_mode((900, 650))
pygame.display.set_caption("SORTING VISUALISER")
# iconImg = pygame.image.load('Icon.png')
# pygame.display.set_icon(Icon.png)

done = True

array_size = 100  # 100 max

array = list(random.randint(1, 100) for x in range(array_size))
arr_clr = [(0, 255, 255)]*array_size
clr = [(0, 255, 255), (255, 0, 0), (0, 0, 200), (0, 200, 0)]
fnt = pygame.font.SysFont("calibri", 25)
fnt1 = pygame.font.SysFont("calibri", 15, bold=True)
fnt2 = pygame.font.SysFont("calibri", 10)


def generate(array):
    for i in range(len(array)):
        arr_clr[i] = clr[0]
        array[i] = random.randint(1, 100)


def refill():
    window.fill((0, 0, 0))
    draw(name)
    pygame.display.update()
    pygame.time.delay(10)

# Sorting Algorithm:
# Bubble Sort


def bubbleSort(arr):
    for i in range(len(array), -1, -1):
        noSwaps = True
        for j in range(0, i-1):
            pygame.event.pump()
            arr_clr[j] = clr[1]
            arr_clr[j+1] = clr[2]
            refill()
            arr_clr[j] = clr[0]
            arr_clr[j+1] = clr[0]
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                noSwaps = False

        if noSwaps:
            break
    for _ in range(len(array)):
        arr_clr[_] = clr[2]
        refill()
        arr_clr[_] = clr[3]

# Selection Sort


def selectionSort(arr):
    for i in range(len(arr)-1):
        noSwap = True
        for j in range(i+1, len(arr)):
            pygame.event.pump()
            arr_clr[i] = clr[1]
            arr_clr[j] = clr[2]
            refill()
            arr_clr[i] = clr[0]
            arr_clr[j] = clr[0]
            if arr[i] > arr[j]:
                noSwap = False
                arr[i], arr[j] = arr[j], arr[i]
        if noSwap:
            break
    for _ in range(len(array)):
        arr_clr[_] = clr[2]
        refill()
        arr_clr[_] = clr[3]

# Insertion Sort


def insertionSort(array):
    for i in range(1, len(array)):
        val = array[i]
        j = i-1
        while j >= 0 and array[j] > val:
            pygame.event.pump()
            arr_clr[i] = clr[1]
            arr_clr[j] = clr[2]
            refill()
            arr_clr[i] = clr[0]
            arr_clr[j] = clr[0]
            array[j+1] = array[j]
            j -= 1
        array[j+1] = val
    for _ in range(len(array)):
        arr_clr[_] = clr[2]
        refill()
        arr_clr[_] = clr[3]

# Merge Sort


def mergeSort(array, l, r):
    mid = (l + r)//2
    if l < r:
        mergeSort(array, l, mid)
        mergeSort(array, mid + 1, r)
        merge(array, l, mid,
              mid + 1, r)


def merge(array, x1, y1, x2, y2):
    i = x1
    j = x2
    temp = []
    pygame.event.pump()
    while i <= y1 and j <= y2:
        arr_clr[i] = clr[1]
        arr_clr[j] = clr[1]
        refill()
        arr_clr[i] = clr[0]
        arr_clr[j] = clr[0]
        if array[i] < array[j]:
            temp.append(array[i])
            i += 1
        else:
            temp.append(array[j])
            j += 1
    while i <= y1:
        arr_clr[i] = clr[1]
        refill()
        arr_clr[i] = clr[0]
        temp.append(array[i])
        i += 1
    while j <= y2:
        arr_clr[j] = clr[1]
        refill()
        arr_clr[j] = clr[0]
        temp.append(array[j])
        j += 1
    j = 0
    for i in range(x1, y2 + 1):
        pygame.event.pump()
        array[i] = temp[j]
        j += 1
        arr_clr[i] = clr[2]
        refill()
        if y2-x1 == len(array)-1:
            arr_clr[i] = clr[3]
        else:
            arr_clr[i] = clr[0]

# Quick sort


def pivot(arr, start, end):
    pygame.event.pump()
    p = arr[start]
    arr_clr[end] = clr[2]
    swapIdx = start
    for i in range(start+1, end+1):
        arr_clr[i] = clr[1]
        refill()
        arr_clr[end] = clr[2]
        arr_clr[i] = clr[0]
        arr_clr[swapIdx] = clr[0]
        if p > arr[i]:
            swapIdx += 1
            arr_clr[swapIdx] = clr[1]
            arr[swapIdx], arr[i] = arr[i], arr[swapIdx]
    refill()
    arr_clr[swapIdx] = clr[0]
    arr_clr[end] = clr[0]
    arr[swapIdx], arr[start] = arr[start], arr[swapIdx]
    return swapIdx


def quickSort(arr, left, right):
    if left < right:
        pivotIndex = pivot(arr, left, right)
        quickSort(arr, left, pivotIndex-1)
        refill()
        for i in range(pivotIndex+1):
            arr_clr[i] = clr[3]
        quickSort(arr, pivotIndex+1, right)

# Radix Sort


def getDigit(num, pos):
    num = str(num)
    num = list([num[i] for i in range(len(num))])
    num.reverse()
    for i in range(len(num)-1, -1, -1):
        if pos == i:
            return int(num[i])
    return 0


def digitCount(num):
    count = 0
    while num > 0:
        temp = num % 10
        count += 1
        num = round(num/10)
    return count


def mostDigits(nums):
    maxDigits = 0
    for i in range(len(nums)):
        maxDigits = max(maxDigits, digitCount(nums[i]))

    return maxDigits


def radixSort():
    global array
    maxCount = mostDigits(array)
    for k in range(maxCount):
        digitBuckets = list([[] for i in range(10)])
        for i in range(len(array)):
            pygame.event.pump()
            arr_clr[i] = clr[1]
            refill()
            arr_clr[i] = clr[0]
            digit = getDigit(array[i], k)
            digitBuckets[digit].append(array[i])
        array = [j for i in digitBuckets for j in i]
    for _ in range(len(array)):
        arr_clr[_] = clr[2]
        refill()
        arr_clr[_] = clr[3]


# Draw the array values
name = 'NONE'


def draw(name):
    naivelist = 'B-BUBBLE SORT | S-SELECTION SORT | I-INSERTION SORT'
    advlist = 'M-MERGE SORT | Q-QUICK SORT | X-RADIX SORT'
    txt = pygame.font.SysFont('calibri', 15).render(
        naivelist, 1, (255, 255, 255))
    window.blit(txt, (380, 20))
    txt1 = fnt.render(advlist, 1, (255, 255, 255))
    window.blit(txt1, (380, 35))
    name = "ALGORITHM: " + name
    txt2 = fnt1.render(name, 1, (255, 255, 255))
    window.blit(txt2, (380, 60))
    element_width = 8  # (width-150)//150
    boundry_arr = 900 // 150 + 3
    boundry_grp = 550 // 100
    pygame.draw.line(window, (255, 255, 255),
                     (0, 95), (900, 95), 8)
    for i in range(array_size):
        txt = str(array[i])
        pygame.draw.rect(
            window, arr_clr[i], (boundry_arr * i, 100, element_width, array[i]*boundry_grp))
        arr_txt = fnt2.render(txt, 1, (255, 255, 255))
        window.blit(arr_txt, (i*9, array[i]*boundry_grp+100))


while done:
    window.fill((0, 0, 0))
    event = pygame.event.wait()
    # Event handler stores all event
    # for event in pygame.event.get():
    # If we click Close button in window
    if event.type == pygame.QUIT:
        done = False
    pygame.draw.rect(window, (0, 125, 255), pygame.Rect(30, 30, 155, 30))
    b_txt = fnt1.render('GENERATE NEW ARRAY', 1, (255, 255, 255))
    window.blit(b_txt, (36, 38))
    pygame.draw.rect(window, (0, 125, 255), pygame.Rect(240, 30, 65, 30))
    b_txt = fnt1.render('TEST ALL', 1, (255, 255, 255))
    window.blit(b_txt, (248, 38))
    if event.type == pygame.MOUSEMOTION:
        if event.pos[0] in range(30, 182) and event.pos[1] in range(32, 60):
            pygame.draw.rect(window, clr[0],
                             pygame.Rect(30, 30, 155, 30))
            b_txt = fnt1.render('GENERATE NEW ARRAY', 1, (0, 0, 0))
            window.blit(b_txt, (36, 38))
        if event.pos[0] in range(240, 305) and event.pos[1] in range(32, 60):
            pygame.draw.rect(window, clr[0], pygame.Rect(240, 30, 65, 30))
            b_txt = fnt1.render('TEST ALL', 1, (0, 0, 0))
            window.blit(b_txt, (248, 38))

    if event.type == pygame.MOUSEBUTTONDOWN:
        # print(f'Button {event.button} Position {event.pos}')
        if event.button == 1 and event.pos[0] in range(30, 182) and event.pos[1] in range(32, 60):
            pygame.draw.rect(window, clr[0],
                             pygame.Rect(30, 30, 155, 30))
            b_txt = fnt1.render('GENERATE NEW ARRAY', 1, (255, 255, 255))
            window.blit(b_txt, (36, 38))
            generate(array)
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] in range(240, 305) and event.pos[1] in range(32, 60):
        name = 'BUBBLE SORT'
        bubbleSort(array)
        pygame.time.delay(30)
        generate(array)
        name = 'SELECTION SORT'
        selectionSort(array)
        pygame.time.delay(30)
        generate(array)
        name = 'INSERTION SORT'
        insertionSort(array)
        pygame.time.delay(30)
        generate(array)
        name = 'MERGE SORT'
        mergeSort(array, 0, len(array)-1)
        pygame.time.delay(30)
        generate(array)
        name = 'QUICK SORT'
        quickSort(array, 0, len(array)-1)
        pygame.time.delay(30)
        generate(array)
        name = 'RADIX SORT'
        radixSort()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_r:
            generate(array)
        # if event.key == pygame.K_ESCAPE:
        #     pygame.quit()
        if event.key == pygame.K_b:
            name = 'BUBBLE SORT'
            t1 = time.time()
            bubbleSort(array)
            t2 = time.time()
            totaltime = t2 - t1
            print(round(totaltime, 2))
        if event.key == pygame.K_s:
            name = 'SELECTION SORT'
            selectionSort(array)
        if event.key == pygame.K_m:
            name = 'MERGE SORT'
            t1 = time.time()
            mergeSort(array, 0, len(array)-1)
            t2 = time.time()
            totaltime = t2 - t1
            print(round(totaltime, 2))
        if event.key == pygame.K_i:
            name = 'INSERTION SORT'
            insertionSort(array)
        if event.key == pygame.K_q:
            name = 'QUICK SORT'
            quickSort(array, 0, len(array)-1)
        if event.key == pygame.K_x:
            name = 'RADIX SORT'
            radixSort()
    draw(name)
    pygame.display.update()

pygame.quit()
