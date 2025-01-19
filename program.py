# Linear Search Implementation
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Binary Search Implementation
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Example execution
if __name__ == "__main__":
    data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    target = 40
    
    print(f"Linear Search result: {linear_search(data, target)}")
    print(f"Binary Search result: {binary_search(data, target)}")
