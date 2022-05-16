from random import shuffle


class array_generator:
    def __init__(self, MIN, MAX, STEP=1):
        self.MIN = MIN
        self.MAX = MAX
        self.array = []
        self.array = [j for j in range(self.MIN, self.MAX, STEP)]

    def sorted(self):
        return self.array

    def reversed(self):
        return self.array[::-1]

    def unsorted(self):
        return shuffle(self.array)