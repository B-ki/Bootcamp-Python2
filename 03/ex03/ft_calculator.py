class calculator:
    def __init__(self, *args):
        assert len(args) == 1, "Only 1 parameter is required"
        assert isinstance(args[0], list), "Parameter must be a list"
        assert all(isinstance(i, (float, int)) for i in args[0]), "List of int\
                or float only"
        self.vector = args[0]

    def __add__(self, n):
        self.vector = [x + n for x in self.vector]
        print(self.vector)
        return self.vector

    def __sub__(self, n):
        self.vector = [x - n for x in self.vector]
        print(self.vector)
        return self.vector

    def __mul__(self, n):
        self.vector = [x * n for x in self.vector]
        print(self.vector)
        return self.vector

    def __truediv__(self, n):
        assert n != 0, "Can't divide by 0"
        self.vector = [x / n for x in self.vector]
        print(self.vector)
        return self.vector
