class Gene:
    def __init__(self, Name, Nr__Nucleotide, Nr__ReadingFrame, Nucleotide, ReadingFrame):
        self.__Name = Name
        self.__Nr__Nucleotide = Nr__Nucleotide
        self.__Nr__ReadingFrame = Nr__ReadingFrame
        self._Nucleotide = Nucleotide
        self._ReadinFrame = ReadingFrame

A = Gene("GORAB", 15, 4, 8, 2)
print(A)
