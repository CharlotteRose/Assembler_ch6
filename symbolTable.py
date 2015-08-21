__author__ = 'Cheech Wife'
# API:
# Look for symbols "(, ), @"
# add location for symbol into table
# update table (dictionary in this instance)

# PreAssigned memory location are as Follows:
# SP - (hex 00000, bin 0000000000000000)
# LCL - (hex 00001, bin 0000000000000001)
# ARG - (hex 00002, bin 0000000000000010)
# THIS - (hex 00003, bin 0000000000000011)
# THAT - (hex 0004, bin 0000000000000100)
# R0-R15 - (hex 000[0-15], bin 000000000000[0-1111])
# SCREEN - (hex 04000, bin 0100000000000000)
# KBD - (hex 06000, bin 0110000000000000)

class SymbolTable(object):  #attributes of symbolTable Class
    def __init__(self):  #initialize with preset values
        self.table = {'SP': bin(0), 'LCL': bin(1),
              'ARG': bin(2), 'THIS': bin(3),
              'THAT': bin(4), 'R0': bin(0),
              'R1': bin(1), 'R2': bin(2),
              'R3': bin(3), 'R4': bin(4),
              'R5': bin(5), 'R6': bin(6),
              'R7': bin(7), 'R8': bin(8),
              'R9': bin(9), 'R10': bin(10),
              'R11': bin(11), 'R12': bin(12),
              'R13': bin(13), 'R14': bin(14),
              'R15': bin(15), 'SCREEN': bin(16),
              'KBD': bin(17)}
        self.variableMemLocation = 16

    def __del__(self):
        print 'end'

    def getAddress(self, symbol):
        return self.table[symbol]

    def checkTable (self, line):
        inTable = line in self.table
        print (inTable, 'now in check')
        return inTable

    def addEntry (self, newSymbol, location):
        self.table [newSymbol] = bin(location)