class Solution:
    def combinationSum(self, candidates, target):
        result = []
        candidates.sort()

        def backtrack(start, path, remaining):
            if remaining == 0:
                result.append(path.copy())
                return

            for i in range(start, len(candidates)):
                num = candidates[i]

                
                if num > remaining:
                    break

                path.append(num)

                
                backtrack(i, path, remaining - num)

                path.pop()

        backtrack(0, [], target)
        return result
                      

        