# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# == solution ==

# --==-- Approach 1  --==--

def twoSum(self, nums, target):
        arr = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    arr = [i, j]
                    return arr 
                
                
# -- runtime 220 ms --
# -- memory 14.26 mb --


# ====================================
# --==-- Approach 2  --==--

def twoSum(self, nums, target):
        plain_dict = {}
        for i,num in enumerate(nums) :
            exist = target - num
            if exist in plain_dict :
                return [plain_dict[exist],i]
            plain_dict[num] = i
        return None

# -- runtime 31 ms --



def two_sumM(nums, target):
   
    nums_with_indices = [(num, i) for i, num in enumerate(nums)]
    
    nums_with_indices.sort()
   

    left, right = 0, len(nums) - 1

    while left < right:
        current_sum = nums_with_indices[left][0] + nums_with_indices[right][0]

        if current_sum == target:

            return [nums_with_indices[left][1], nums_with_indices[right][1]]
        elif current_sum < target:

            left += 1
        else:
            right -= 1

    return None



# -- runtime 28 ms --