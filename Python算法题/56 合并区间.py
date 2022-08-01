from typing import List


class Solution:
    def deleteDuplicatedElementFromList(self, listA):
        return sorted(set(listA), key=listA.index)

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        list = sum(intervals, [])

        length = len(list)
        start = [0] * (int(length / 2))
        end = [0] * (int(length / 2))
        for i in range(0, len(start)):
            start[i] = list[i * 2]
            end[i] = list[i * 2 + 1]
        for start_pointer in range(1, i):
            for end_pointer in range(0, i - 1):
                if end[end_pointer] <= start[start_pointer]:
                    start[start_pointer] = start[start_pointer - 1]
                    end[end_pointer] = end[end_pointer + 1]

        start = self.deleteDuplicatedElementFromList(start)
        end = self.deleteDuplicatedElementFromList(end)
        result = [[0 for i in range(2)] for j in range(i)]
        for i in range(0, i):
            result[i][0] = start[i]
            result[i][1] = end[i]

        print (result)
if __name__ == '__main__':
    Solution.merge(self,[[1,4],[5,6]])