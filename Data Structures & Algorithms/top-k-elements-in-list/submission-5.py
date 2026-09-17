class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        arr = []
        for num in nums:
            if num not in hm:
                hm[num] = 1
            else:
                hm[num] += 1
            
        numbers = sorted(list(hm), key=hm.get, reverse=True)
        for i in range(k):
            arr.append(numbers[i])

        return arr
