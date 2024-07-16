def count_occurrences(nums, target):
    def binary_search_left(nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def binary_search_right(nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return right

    start = binary_search_left(nums, target)
    end = binary_search_right(nums, target)
    
    if start <= end:
        return end - start + 1
    return 0

nums = [1, 1, 2, 2, 2, 2, 3]
target = 2
print(count_occurrences(nums, target)) 
