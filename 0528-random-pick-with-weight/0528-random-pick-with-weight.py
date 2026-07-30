import random
import bisect

class Solution:

    def __init__(self, w):
        self.prefix = []
        total = 0

        for num in w:
            total += num
            self.prefix.append(total)

        self.total = total

    def pickIndex(self):
        num = random.randint(1, self.total)
        return bisect.bisect_left(self.prefix, num)