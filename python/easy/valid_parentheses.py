class Solution:
	brackets = {"}":"{", ")":"(", "]":"[]"}
	def isValid(self, s: str):
		stack = []
		for bracket in s:
			if bracket in self.brackets.values():
				stack.append(bracket)
			else:
				if stack and self.brackets[bracket] == stack[-1]:
					stack.pop()
				else:
					return False
		
		if stack:
			return False
		return True

    	
if __name__ == '__main__':
	solution = Solution()
	assert solution.isValid("()"), True
	assert solution.isValid("()[]{}"), True
	assert solution.isValid("(]"), False
