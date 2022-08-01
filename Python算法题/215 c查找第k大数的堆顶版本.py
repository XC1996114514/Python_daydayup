#，放在函数外边即可！
from heapq import *
class Solution:
    def findKthLargest(self, nums, k: int) -> int:

        heap = []
        heapify(heap)
        for num in nums:
            heappush(heap,num)
            if len(heap)>k:
                heappop(heap)
        return heap[0]

if __name__ == '__main__':

    a = [1,23,4123,51,56]
    b = Solution.findKthLargest(a,a,3)
    print(b)