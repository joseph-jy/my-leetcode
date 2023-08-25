class Solution:
	def isPalindrome(self, x: int) -> bool:
		return False if x < 0 else x == int(str(x)[::-1])
		
if __name__ == "__main__":
	solution = Solution()
	assert solution.isPalindrome(121), True
#	assert solution.isPalindrome(-121), False
