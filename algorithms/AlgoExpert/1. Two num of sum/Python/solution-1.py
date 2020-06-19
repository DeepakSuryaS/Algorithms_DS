# This solution uses hashtable (dictionary)
# This solution is the most optimal.
# Runs in O(n) time and O(n) space
  # Because, we will traverse the array only once and we will have only one hashtable.
  # For better understanding, check time and space complexity for hashtables.

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
  print("Two numbers that add up to the target number are: ", twoNumberSum(array, targetNum))

if __name__ == "__main__":
  main()
