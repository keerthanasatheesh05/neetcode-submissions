class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        output = []
        left = 0
        right = len(numbers) - 1

        while left < right:
            sum = numbers[left] + numbers[right]

            if sum == target:
                output = [left + 1, right + 1]
                return output

            elif target < sum:
                right -= 1

            else:
                left += 1

        return output