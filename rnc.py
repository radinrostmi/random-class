import time

class random:
    def __init__(self, seed=None):
        if seed is None:
            seed = int(time.time() * 1000)  # auto seed

        self.index = 624
        self.mt = [0] * 624
        self.mt[0] = seed

        for i in range(1, 624):
            self.mt[i] = (1812433253 * (self.mt[i - 1] ^ (self.mt[i - 1] >> 30)) + i) & 0xffffffff

    def extract_number(self):
        if self.index >= 624:
            self.generate_numbers()

        y = self.mt[self.index]
        self.index += 1

        y ^= (y >> 11)
        y ^= (y << 7) & 0x9d2c5680
        y ^= (y << 15) & 0xefc60000
        y ^= (y >> 18)

        return y & 0xffffffff

    def generate_numbers(self):
        for i in range(624):
            y = (self.mt[i] & 0x80000000) + (self.mt[(i + 1) % 624] & 0x7fffffff)
            self.mt[i] = self.mt[(i + 397) % 624] ^ (y >> 1)

            if y % 2 != 0:
                self.mt[i] ^= 0x9908b0df

        self.index = 0

    def random(self):
        return self.extract_number() / 2**32

    def randint(self, a, b):
        return a + self.extract_number() % (b - a + 1)






