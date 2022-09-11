import tkinter as tk
import tkinter.font as font
import re


class Nucleotides:

    def __init__(self, ):
        self.__Name = Name
        self.__Nr__Nucleotide = Nr__Nucleotide
        self.__Nr__ReadingFrame = Nr__ReadingFrame
        self._Nucleotide = Nucleotide
        self._ReadinFrame = ReadingFrame


    def get_Name(self):
        return self.__Name
    def get_Nr__Nucleotide(self):
        return self.__Nr__Nucleotide
    def get_Nr__ReadingFrame(self):
        return self.__Nr__ReadingFrame
    def get_Nucleotide(self):
        return self.__Nucleotide
    def get_ReadingFrame(self):
        return self.__ReadingFrame

    def set_Nr__Nucleotide(self, cubic):
        if cubic <= 0:
            print("Erorr: Negative value for displacement")
        else:
            self.__Nr__Nucleotide = cubic
            print ("Nr__Nucleotide was not change")

    def __str__(self):
        printout = str("Name, Nr__Nucleotide, Nr__ReadingFrame, Nucleotide, ReadingFrame")
        return printout


A = Gene("GORAB", 15, 4, 8, 2)
print(A)
#print(Gene.get_Name())
#print(Gene.get_Nr__Nucleotide())
#print(Gene.get_Nr__ReadingFrame())
#print(Gene.et_Nucleotide())
#print(Gene.get_ReadingFrame())



















#def set_Nr__Nucleotide(self, cubic)
 #if cubic <= 0
    #print("Erorr: Negative value for displacement")
#else:
    #self.__Nr__Nucleotide = cubic
    #print ("Nr__Nucleotide was not change")
