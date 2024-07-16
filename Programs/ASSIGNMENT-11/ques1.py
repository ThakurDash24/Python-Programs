def find_start_end_position(nums, target):
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
        return [start, end]
    return [-1, -1]

nums = [2, 7, 7, 8, 8, 16, 21]
target = 8
print(find_start_end_position(nums, target))  
