# This solution uses hashtable (dictionary)
# This solution is the most optimal.
# Runs in O(n) time and O(n) space
  # Because, we will traverse the array only once and we will have only one hashtable.
  # For better understanding, check time and space complexity for hashtables.

# Working
# y = target - x, where x is the current element
# If y is present in the hashtable, then solution is (x, y)

def twoNumberSum(array, targetNum):
  nums = {}
  for num in array:
    potentialMatch = targetNum - num
    if potentialMatch in nums:
      return [potentialMatch, num]
    else:
      nums[num] = True
  
  return []

def main():
  array = [3, 5, -4, 8, 11, 1, -1, 6]
  targetNum = 10
  print("Answer: ", twoNumberSum(array, targetNum))

if __name__ == "__main__":
  main()
