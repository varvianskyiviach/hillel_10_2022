class frange:
    def __init__(self, start, stop=None, step=None):
        self.start = start
        self.stop = stop
        self.step = step
        self.count_step = 0

        if stop is None:
            self.stop = self.start
            self.start = 0.0
        if step is None:
            self.step = 1.0

    def __next__(self):
        result = self.start + self.count_step * self.step
        if self.step > 0 and result >= self.stop:
            raise StopIteration("stop")
        elif self.step < 0 and result <= self.stop:
            raise StopIteration("stop")

        self.count_step += 1
        return result

    def __iter__(self):
        return self


assert list(frange(5)) == [0, 1, 2, 3, 4]
assert list(frange(2, 5)) == [2, 3, 4]
assert list(frange(2, 10, 2)) == [2, 4, 6, 8]
assert list(frange(10, 2, -2)) == [10, 8, 6, 4]
assert list(frange(2, 5.5, 1.5)) == [2, 3.5, 5]
assert list(frange(1, 5)) == [1, 2, 3, 4]
assert list(frange(0, 5)) == [0, 1, 2, 3, 4]
assert list(frange(0, 0)) == []
assert list(frange(100, 0)) == []

print("SUCCESS!")
