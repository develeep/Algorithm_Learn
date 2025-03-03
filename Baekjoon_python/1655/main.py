import sys
sys.stdin = open("input.txt", "r")

###########################################################
import heapq
nums = []
heapq.heappush(nums, 12)
heapq.heappush(nums, 15)
heapq.heappush(nums, -14)
heapq.heappush(nums, 2)
heapq.heappush(nums, 5)

print(nums)
