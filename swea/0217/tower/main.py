import sys
sys.stdin = open('input.txt', 'r')
##################################################
from collections import deque
import heapq
T = int(input())    # Testcase 개수를 받아오는 코드
for tc in range(1, T + 1):
    n,m = map(int,input().split())
    parking_weight = [int(input()) for _ in range(n)]
    car_weight = [int(input()) for _ in range(m)]
    wait_car = deque()
    park_wait_idx = [i for i in range(n)]
    heapq.heapify(park_wait_idx)
    park_car = [0]*m
    result = 0
    for _ in range(2*m):
        x = int(input())
        if x > 0:
            if park_wait_idx:
                index = heapq.heappop(park_wait_idx) # 주차장 인덱스
                park_car[x-1] = index
                result += parking_weight[index] * car_weight[x-1]
            else:
                wait_car.append(x)
        else:
            car_idx = abs(x) - 1
            park_idx = park_car[car_idx]
            heapq.heappush(park_wait_idx,park_idx)
            if wait_car:
                car_idx = wait_car.popleft() - 1
                park_idx = heapq.heappop(park_wait_idx)
                park_car[car_idx] = park_idx
                result += parking_weight[park_idx] * car_weight[car_idx]
    print(f'#{tc} {result}')