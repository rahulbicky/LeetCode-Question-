class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            # Step 1: target mil gaya
            if nums[mid] == target:
                return mid

            # Step 2: check kaunsa part sorted hai
            if nums[mid] <= nums[high]:  
                # right part sorted hai

                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

            else:
                # left part sorted hai

                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1

        return -1





            

