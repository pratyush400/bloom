class BloomFilter:
    def __init__(self):
        self.bits = 0
        # self.k = 2

    def add(self, key):
        h = abs(hash(key)) % (2 ** 32)
        h1 = h & 0xFFFF
        h2 = h >> 16
        self.bits |= (1 << h1)
        self.bits |= 1 << h2

    def _true_bits():
        return

    def might_contain(self, key):
        h = abs(hash(key)) % (2 ** 32)
        h1 = h & 0xFFFF
        h2 = h >> 16
        if self.bits & (1 << h1) != 0:
            return True
        if self.bits & (1 << h2) != 0:
            return True