import queue


class MaxQueue:

    def __init__(self):
        self.q = queue.Queue()
        self.d = queue.deque()

    def max_value(self) -> int:
        return self.d[0] if self.d else -1

    def push_back(self, value: int) -> None:
        while self.d and self.d[-1] < value:
            self.d.pop()
        self.d.append(value)
        self.q.put(value)

    def pop_front(self) -> int:
        if self.q.empty():
            return -1
        ans = self.q.get()
        if ans == self.d[0]:
            self.d.popleft()
        return ans
