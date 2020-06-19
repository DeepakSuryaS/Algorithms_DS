# This solution uses two for loops. So, it's obviously the least optimum.
# Runs in O(n^2) time and in O(1) space.

def twoNumberSum(array, targetNum):
  for i in range(len(array) - 1):
    firstNum = array[i]
    for j in range(i + 1, len(array)):
      secondNum = array[j]
      if firstNum + secondNum == targetNum:
        return [firstNum, secondNum]
  return []

def main():
  array = [3, 5, -4, 8, 11, 1, -1, 6]
  targetNum = 10
  print("Two numbers that add up to the target number are: ", twoNumberSum(array, targetNum))

if __name__ == "__main__":
  main()