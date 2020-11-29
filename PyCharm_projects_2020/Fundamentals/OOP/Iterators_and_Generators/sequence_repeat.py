class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.i = 0
        self.ls = len(list(sequence))

    def __iter__(self):
        return self

    def find_index_right(self, jump, listi):
        ind = jump
        if ind >= len(listi):
            while ind >= len(listi):
                ind -= len(listi)
        return ind

    def __next__(self):
        if self.i < self.number:
            i = self.i
            self.i += 1
            ind = self.find_index_right(i, self.sequence)
            return self.sequence[ind]
        else:
            raise StopIteration()


result = sequence_repeat('123*', 22)
for item in result:
    print(item, end ='')