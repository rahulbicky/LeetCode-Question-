class Solution:
    def majorityElement(self, nums):

        count = 0
        item = None
        for x in nums:
            if count == 0:
                item = x
            if x == item:
                count +=1
            else:
                count -=1
    
        return item