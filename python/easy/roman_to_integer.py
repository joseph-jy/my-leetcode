class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        total = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for symbol in s:
            total += roman[symbol]
        return total

def main():
    solution = Solution()
    assert solution.romanToInt("LVIII") == 58
    assert solution.romanToInt("III") == 3
    assert solution.romanToInt("MCMXCIV") == 1994
    print('success')

if __name__ == "__main__":
    main()
