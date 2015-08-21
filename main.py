#Assembler for cs271
#tutorialspoint.com for syntax reference

__author__ = 'Cheech Wife'
import symbolTable
import Parser

#newTable = symbolTable.SymbolTable()
#newTable.__init__()
newFile = Parser.Parser('Max.asm', 'Max.txt')
newFile.advanceInFile()