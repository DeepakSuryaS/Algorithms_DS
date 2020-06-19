# Runs in O(nlog(n)) time and O(1) space.

def twoNumberSum(array, targetNum):
  array.sort()
  left = 0
  right = len(array) - 1
  while left < right:
    currentSum = array[left] + array[right]
    if currentSum == targetNum:
      return [array[left], array[right]]
    elif currentSum < targetNum:
      left += 1
    elif currentSum > targetNum:
      right -= 1
  
  return []

def main():
  array = [3, 5, -4, 8, 11, 1, -1, 6]
  targetNum = 10
  print("Two numbers that add up to the target number are: ", twoNumberSum(array, targetNum))

if __name__ == "__main__":
  main()