# This solution uses hashtable (dictionary)
# This solution is the most optimal.
# Runs in O(n) time and O(n) space
  # Because, we will traverse the array only once and we will have only one hashtable.
  # For better understanding, check time and space complexity for hashtables.

def twoNumberSum(array, targetSum):
  nums = {}
  for num in array:
    potentialMatch = targetSum - num
    if potentialMatch in nums:
      return [potentialMatch, num]
    else:
      nums[num] = True
  
  return []
