class calculator:

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        res = 0
        for i in range(len(V1)):
            res += V1[i] * V2[i]
        print(res)

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        res = [None] * len(V1)
        for i in range(len(V1)):
            res[i] = V1[i] + V2[i]
        print(res)

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        res = [None] * len(V1)
        for i in range(len(V1)):
            res[i] = V1[i] - V2[i]
        print(res)
