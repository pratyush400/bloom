__author__ = "Jolie, Emma, Pratyush"

from xxhash import xxh64


class BloomFilter:
    def __init__(self):
        self.bits = 0

    def add(self, key):
        h = abs(hash(key)) % (2 ** 32)
        h1 = h & 0xFFFF
        h2 = h >> 16
        self.bits |= (1 << h1)
        self.bits |= 1 << h2

    def might_contain(self, key):
        h = abs(hash(key)) % (2 ** 32)
        h1 = h & 0xFFFF
        h2 = h >> 16
        return (self.bits & (1 << h1)) != 0 and (self.bits & (1 << h2)) != 0  # & is bitwise and

    def _true_bits(self):
        return bin(self.bits).count('1')


class BloomFilter64:
    BIT_SIZE = 2 ** 20 # practical size for Python int
    def __init__(self):
        self.bits = 0

    def add(self, key):
        h_new = xxh64(key).intdigest()
        h1_new = (h_new & 0xFFFFFFFF) % self.BIT_SIZE
        h2_new = (h_new >> 32) % self.BIT_SIZE
        self.bits |= (1 << h1_new)
        self.bits |= (1 << h2_new)

    def might_contain(self, key):
        h_new = xxh64(key).intdigest()
        h1_new = (h_new & 0xFFFFFFFF) % self.BIT_SIZE
        h2_new = (h_new >> 32) % self.BIT_SIZE
        return (self.bits & (1 << h1_new)) != 0 and (self.bits & (1 << h2_new)) != 0

    def _true_bits(self):
        return bin(self.bits).count('1')
# only works if 2 news bits are added

    # If you've done that, compare various options such as using three 20-bit indices instead of two 32-bit indices.
    # What seems to be a good tradeoff between accuracy and space?
    """increasing the bits reduces false positives exponentially for fixed number of indices and number of inserted items.
    Increasing indices initially reduces false positives but stops after the optimal point. Which can be calculated as k(optimal)=(m/n)ln2.
    two 32-bit: bits = 2^32 = 4,294,966,296.(splitting 64 bit hash in half).
    three 20-bit: bits = 2^20 =1,048,576.   
    While the two 32-bit takes up more memory it also can store more items.
    The three 20-bits take up less memory, but has an increased chance of a false positive with large n.
    A good tradeoff just depends on if you need a small chance of a false positive or something to use limited memory.
    A rule of thumb is that bites needs to be proportional to number of element."""

