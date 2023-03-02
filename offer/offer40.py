# author: tobebetter9527
# since: 2023/3/2 16:35
import heapq
from typing import List


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k == 0:
            return []
        hp = [-x for x in arr[0:k]]
        heapq.heapify(hp)
        for x in arr[k:]:
            if -hp[0] > x:
                heapq.heappop(hp)
                heapq.heappush(hp, -x)
        ans = [-x for x in hp]
        return ans
