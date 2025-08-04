class Solution(object):
    def moveZeroes(self, nums):
        j = 0

        # Move non-zero elements to the front
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j+= 1

        print(nums)


s = Solution()
a = [0, 0, 1]
s.moveZeroes(a)  # Output: [1, 0, 0]

s1 = Solution()
a = [1,2,0,8,9]
s1.moveZeroes(a)
