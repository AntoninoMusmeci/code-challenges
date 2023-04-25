# https://leetcode.com/problems/smallest-number-in-infinite-set/description/
class SmallestInfiniteSet:
    # Your SmallestInfiniteSet object will be instantiated and called as such:
    # obj = SmallestInfiniteSet()
    # param_1 = obj.popSmallest()
    # obj.addBack(num)
    def __init__(self):
        self.start = 1
        self.heap = []
        self.present = set()

    def popSmallest(self) -> int:
        if self.heap:

            num = heapq.heappop(self.heap)
            self.present.remove(num)
            return num
        self.start += 1
        return self.start - 1

    def addBack(self, num: int) -> None:
        if num < self.start and num not in self.present:
            heapq.heappush(self.heap, num)
            self.present.add(num)
