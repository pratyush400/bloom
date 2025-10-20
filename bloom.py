class BloomFilter:
    def __init__(self, m, k):
        self.m = [False] * m
        self.k = k

    def add(self, key):
        k = [abs(hash(key)) % len(self.m)] * self.k
        if key in (len(self.m) - 1):
            self.m = True

    def _true_bits():
        return

    def might_contain(self, key):
        return