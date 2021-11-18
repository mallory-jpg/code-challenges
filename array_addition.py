from itertools import combinations

def ArrayAddition(arr):
"""
Given an array, return 'true' if any combination of numbers in the given array
(without the largest number) add up to the largest number. Return 'false' if no
combination satisfies this condition.
:param arr: array of positive and negative numbers
:return str: 'true' or 'false'
"""
  sorted_arr = sorted(arr)
  largest_num = sorted_arr.pop(-1)
  
  for i in range(1, len(sorted_arr) + 1):
    for x in combinations(sorted_arr, i):
      if largest_num == sum(x):
        return "true"
  return "false"
