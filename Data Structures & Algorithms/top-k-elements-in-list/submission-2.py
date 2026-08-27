class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count ={}
        group =[]

        for num in nums:
            count[num] = count.get(num, 0)+1

        for i in range (k):
            maximum = max(count.values())

            for num in count:
                if count[num]== maximum:
                    group.append(num)
                    del count[num]
                    break
        return group

