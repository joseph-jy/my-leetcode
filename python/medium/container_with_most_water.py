from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left, right = 0, len(height)-1
        while left < right:
            max_area = max(max_area, (right-left)*min(height[left], height[right]))
            if height[left] < height[right]:
                left = left + 1
            else:
                right = right - 1
        return max_area

if __name__ == "__main__":
    solution = Solution()
    assert solution.maxArea([1,8,6,2,5,4,8,3,7]) == 49
    assert solution.maxArea([1,1]) == 1

