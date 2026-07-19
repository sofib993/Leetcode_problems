class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        y = nums[0]
        z = nums[-1]

        ls = []
        for num in range(1, y+1):
            if z % num == 0 and y % num == 0:
                ls.append(num)
                continue

        return ls[-1]