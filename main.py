"""
Connor Cox
U3 Lab 4
Binary Search
"""

def binary_search(target, nums, pointer = 0):
  mid = int((len(nums)-1)/2)
  middle = int(nums[mid])

  pointer += mid

  if middle == target or len(nums) == 1:
    if middle == target:
      return pointer
    else:
      return None
  
  if middle < target:
    nums = nums[mid:]
    if len(nums) == 2:
      nums = [nums[1]]
      pointer += 1
  elif target < middle:
    nums = nums[:mid]
    pointer -= mid
    if len(nums) == 2:
      nums = [nums[0]]
      pointer += 1

  result = binary_search(target, nums, pointer)

  return result
  

def main():
    nums = [1,2,3,4,5,6,7,8,9]

    test1 = binary_search(2, nums)
    print("\n\nTest 1 - search for 2")
    print(f"Your returned index: {test1}\t")
    print(f"Test passed? {test1 == 1}\n\n")

    test2 = binary_search(7, nums)
    print("Test 2 - search for 7")
    print(f"Your returned index: {test2}")
    print(f"Test passed? {test2 == 6}\n\n")

    test3 = binary_search(9, nums)
    print("Test 3 - search for 9")
    print(f"Your returned index: {test3}")
    print(f"Test passed? {test3 == 8}\n\n")

    test4 = binary_search(99, nums)
    print("Test 4 - number doesn't exist")
    print(f"Your returned index: {test4}")
    print(f"Test passed? {test4 == None}\n\n")

if __name__ == "__main__":
    main()