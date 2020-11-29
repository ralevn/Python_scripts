class dictionary_iter:
    def __init__(self, dictionary):
        self.dict = dictionary
        self.ld = len(self.dict)
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.ld:
            i = self.i
            self.i += 1
            lk = list(self.dict.keys())
            lv = list(self.dict.values())
            li = list(self.dict.items())
            return li[i]
        else:
            raise StopIteration()

result = dictionary_iter({1: "one", 2: "two", 3: "three", 4: "four", 5: "five"})
for x in result:
    print(x)