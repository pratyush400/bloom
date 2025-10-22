__author__ = "Jolie, Emma, Pratyush"

class BloomFilter:
    def __init__(self):
        self.bits = 0
        self.size = 2 ** 16  # 16 bits

    def add(self, key):
        h = abs(hash(key)) % (2 ** 32)
        h1 = h % (2 ** 16)  # lower 16 bits
        h2 = (h // (2 ** 16)) % (2 ** 16)  # upper 16 bits
        self.bits |= (1 << h1)
        self.bits |= (1 << h2)

    def might_contain(self, key):
        h = abs(hash(key)) % (2 ** 32)
        h1 = h % (2 ** 16)
        h2 = (h // (2 ** 16)) % (2 ** 16)
        return (self.bits & (1 << h1)) != 0 and (self.bits & (1 << h2)) != 0  # & is bitwise and

    def _true_bits(self):
        return bin(self.bits).count('1')  # only works if 2 news bits are added
