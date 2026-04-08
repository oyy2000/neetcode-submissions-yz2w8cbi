class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        m = {}

        for i in range(len(numbers)):
            if numbers[i] in m:
                return [m.get(numbers[i]) + 1, i + 1]
            else:
                diff = target - numbers[i]
                m[diff] = i
            print(m.keys())

