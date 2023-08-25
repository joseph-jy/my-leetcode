from typing import List

class Solution:
	def twoSum(self, nums: List[int], target: int) -> List[int]:
		hashmap = {}
		for i in range(len(nums)):
			hashmap[nums[i]] = i
		for i in range(len(nums)):
			complement = target - nums[i]
			if complement in hashmap and hashmap[complement] != i:
				return [i, hashmap[complement]]

def main():
	solution = Solution()
	assert solution.twoSum([2,7,8,9,11], 9), [0, 1]
	print ('success')

if __name__ == '__main__':
	main()
	
