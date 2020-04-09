class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

    def computeDifference(self):
        for i in range(len(self.__elements)):
            for j in range(i + 1, len(self.__elements)):
                if abs(self.__elements[i] - self.__elements[j]) > self.maximumDifference:
                    self.maximumDifference = abs(self.__elements[i] - self.__elements[j])
                else:
                    pass

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)