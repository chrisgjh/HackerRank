#!/bin/python3

import sys


arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)
total = []
for i in range(4):
    for j in range(4):
        total_temp = 0
        total_temp += arr[i][j] + arr[i][j+1] + arr[i][j+2]
        total_temp += arr[i+1][j+1]
        total_temp += arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
        total.append(total_temp)
print(max(total))
