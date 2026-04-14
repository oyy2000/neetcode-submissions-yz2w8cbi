class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        results = [0 for i in range(len(temperatures))]
        print(results)
        for i, temp in enumerate(temperatures):
            
            if not stack or temp <= stack[-1][0]:
                stack.append((temp, i))
            else:
                print(stack)
                while stack and temp > stack[-1][0]:
                    t, index = stack[-1]
                    stack.pop()
                    results[index] = i - index
                
                stack.append((temp, i))

        return results
